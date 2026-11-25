"""
Brain Tumor MRI Dataset Loader
Dataset: Jun Cheng Figshare Brain Tumor Dataset

Original labels:
1 - Meningioma
2 - Glioma
3 - Pituitary Tumor

Mapped labels:
0 - Meningioma
1 - Glioma
2 - Pituitary Tumor

Supports MATLAB v7.3 files using h5py.
"""

from pathlib import Path

import h5py
import numpy as np


# Original labels to zero-indexed labels
LABEL_MAP = {
    1: 0,
    2: 1,
    3: 2
}

CLASS_NAMES = {
    0: "Meningioma",
    1: "Glioma",
    2: "Pituitary"
}


def map_label(original_label):
    """Convert original dataset label to zero-indexed label."""

    original_label = int(original_label)

    if original_label not in LABEL_MAP:
        raise ValueError(
            f"Invalid tumor label: {original_label}"
        )

    return LABEL_MAP[original_label]


def load_mat_file(file_path):
    """Load and validate one MRI sample from a MATLAB v7.3 file."""

    file_path = Path(file_path)

    if not file_path.is_file():
        raise FileNotFoundError(
            f"File not found: {file_path}"
        )

    if file_path.suffix.lower() != ".mat":
        raise ValueError("Expected a .mat file")

    try:
        with h5py.File(file_path, "r") as data:

            if "cjdata" not in data:
                raise KeyError(
                    "Missing 'cjdata' variable in MAT file"
                )

            sample = data["cjdata"]

            required_fields = [
                "image",
                "label",
                "tumorMask"
            ]

            for field in required_fields:
                if field not in sample:
                    raise KeyError(
                        f"Missing field '{field}' in cjdata"
                    )

            image = np.asarray(
                sample["image"],
                dtype=np.float32
            )

            original_label = int(
                np.asarray(
                    sample["label"]
                ).squeeze()
            )

            mask = np.asarray(
                sample["tumorMask"]
            )

    except (OSError, KeyError) as error:
        raise ValueError(
            f"Unable to read MAT file: {file_path}: {error}"
        ) from error

    if image.ndim != 2:
        raise ValueError("MRI image must be 2D")

    if image.size == 0:
        raise ValueError("MRI image is empty")

    if mask.ndim != 2:
        raise ValueError("Tumor mask must be 2D")

    if mask.shape != image.shape:
        raise ValueError(
            "MRI image and tumor mask dimensions do not match"
        )

    if not np.isfinite(image).all():
        raise ValueError(
            "MRI image contains NaN or infinite values"
        )

    label = map_label(original_label)

    return {
        "image": image,
        "mask": mask,
        "label": label,
        "original_label": original_label,
        "class_name": CLASS_NAMES[label]
    }


def load_dataset(dataset_dir):
    """
    Load all individual MRI MAT files recursively.

    Excludes cvind.mat because it contains cross-validation
    indices rather than an individual MRI sample.
    """

    dataset_dir = Path(dataset_dir)

    if not dataset_dir.exists():
        raise FileNotFoundError(
            f"Dataset directory not found: {dataset_dir}"
        )

    if not dataset_dir.is_dir():
        raise NotADirectoryError(
            f"Expected a directory: {dataset_dir}"
        )

    files = sorted(
        file for file in dataset_dir.rglob("*.mat")
        if file.name.lower() != "cvind.mat"
    )

    if not files:
        raise ValueError(
            "No individual MRI MAT files found"
        )

    images = []
    masks = []
    labels = []
    valid_files = []
    errors = []

    for file in files:

        try:
            sample = load_mat_file(file)

            images.append(sample["image"])
            masks.append(sample["mask"])
            labels.append(sample["label"])
            valid_files.append(file)

        except (ValueError, KeyError, OSError) as error:
            errors.append((file, str(error)))

    if not images:
        raise ValueError(
            "No valid MRI samples could be loaded"
        )

    return {
        "images": images,
        "masks": masks,
        "labels": np.asarray(labels, dtype=np.int64),
        "files": valid_files,
        "errors": errors
    }


def validate_dataset(dataset_dir):
    """Validate the extracted brain tumor dataset."""

    dataset = load_dataset(dataset_dir)

    images = dataset["images"]
    masks = dataset["masks"]
    labels = dataset["labels"]

    print("\n======================================")
    print("       BRAIN TUMOR DATASET REPORT")
    print("======================================")

    print(f"Valid MRI samples : {len(images)}")
    print(f"Invalid files     : {len(dataset['errors'])}")

    print("\nTumor Class Distribution:")

    for index, name in CLASS_NAMES.items():

        count = int(np.sum(labels == index))

        print(f"{name}: {count}")

    print("\nImage Shape Examples:")

    for image in images[:5]:
        print(image.shape)

    print("\nValidation Checks:")

    print(
        "Image dimensions:",
        all(image.ndim == 2 for image in images)
    )

    print(
        "Mask dimensions:",
        all(mask.ndim == 2 for mask in masks)
    )

    print(
        "Finite image values:",
        all(np.isfinite(image).all() for image in images)
    )

    print(
        "Valid labels:",
        bool(np.isin(labels, [0, 1, 2]).all())
    )

    if dataset["errors"]:

        print("\nInvalid File Details:")

        for file, error in dataset["errors"][:10]:
            print(f"{file}: {error}")

    print("\n======================================")
    print("       VALIDATION COMPLETED")
    print("======================================")

    return dataset