import numpy as np
from skimage.transform import resize
from sklearn.model_selection import train_test_split
from pathlib import Path
from tqdm import tqdm

IMAGE_SIZE = (224, 224)
NORMALIZATION_RANGE = (0.0, 1.0)

def preprocess_image(image, image_size=IMAGE_SIZE):
    """
    Resize an MRI image and normalize pixel values to [0, 1].
    """

    image = np.asarray(image, dtype=np.float32)

    if image.ndim != 2:
        raise ValueError("MRI image must be 2D")

    if not np.isfinite(image).all():
        raise ValueError("Image contains NaN or infinite values")

    # Resize image to 224x224
    resized_image = resize(
        image,
        image_size,
        order=1,
        preserve_range=True,
        anti_aliasing=True
    )

    # Normalize individual image to [0, 1]
    min_value = resized_image.min()
    max_value = resized_image.max()

    if max_value > min_value:
        normalized_image = (
            resized_image - min_value
        ) / (max_value - min_value)
    else:
        normalized_image = np.zeros_like(resized_image)

    return normalized_image.astype(np.float32)

def preprocess_mask(mask, image_size=IMAGE_SIZE):
    """
    Resize tumor mask while preserving its original values.
    """

    mask = np.asarray(mask)

    if mask.ndim != 2:
        raise ValueError("Tumor mask must be 2D")
    if not np.isfinite(mask).all():
        raise ValueError("Mask contains NaN or infinite values")

    if not np.isin(mask, [0, 1]).all():
        raise ValueError("Mask must contain only 0 and 1")

    # Resize mask using nearest-neighbor interpolation
    resized_mask = resize(
        mask,
        image_size,
        order=0,
        preserve_range=True,
        anti_aliasing=False
    )

    return resized_mask.astype(np.uint8)


def create_patient_splits(
    patient_ids,
    labels,
    random_state=42
):
    """
    Create stratified train, validation and test splits
    at patient level to prevent data leakage.
    """

    patient_ids = np.asarray(patient_ids)
    labels = np.asarray(labels)

    if len(patient_ids) != len(labels):
        raise ValueError(
            "Patient IDs and labels must have equal length"
        )

    if len(patient_ids) == 0:
        raise ValueError("Dataset is empty")

    # Create a mapping of each patient to their label
    patient_label_map = {}

    for patient_id, label in zip(patient_ids, labels):
        if patient_id in patient_label_map:
            if patient_label_map[patient_id] != label:
                raise ValueError(
                    f"Patient {patient_id} has multiple labels"
                )
        else:
            patient_label_map[patient_id] = label

    unique_patients = np.array(
        list(patient_label_map.keys())
    )

    patient_labels = np.array([
        patient_label_map[patient_id]
        for patient_id in unique_patients
    ])

    # First split: 70% train, 30% temporary
    train_patients, temp_patients = train_test_split(
        unique_patients,
        test_size=0.30,
        random_state=random_state,
        stratify=patient_labels
    )

    # Get labels for temporary patients
    temp_labels = np.array([
        patient_label_map[patient_id]
        for patient_id in temp_patients
    ])

    # Second split: 15% validation, 15% test
    val_patients, test_patients = train_test_split(
        temp_patients,
        test_size=0.50,
        random_state=random_state,
        stratify=temp_labels
    )

    # Convert patient splits into image indices
    splits = {
        "train": np.where(
            np.isin(patient_ids, train_patients)
        )[0],

        "validation": np.where(
            np.isin(patient_ids, val_patients)
        )[0],

        "test": np.where(
            np.isin(patient_ids, test_patients)
        )[0]
    }

    return splits


def save_processed_dataset(dataset, splits, output_dir="data/processed"):
    """
    Preprocess and save MRI images and masks
    into train, validation and test directories.
    """

    output_dir = Path(output_dir)

    for split_name, indices in splits.items():
        image_dir = output_dir / split_name / "images"
        mask_dir = output_dir / split_name / "masks"

        image_dir.mkdir(parents=True, exist_ok=True)
        mask_dir.mkdir(parents=True, exist_ok=True)

        for index in tqdm(indices, desc=f"Processing {split_name}"):

            image = preprocess_image(dataset["images"][index])
            mask = preprocess_mask(dataset["masks"][index])

            filename = f"image_{index:04d}.npy"

            np.save(image_dir / filename, image)
            np.save(mask_dir / filename, mask)

    print("\nDataset preprocessing completed!")

