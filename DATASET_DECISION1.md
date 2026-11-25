# Dataset Decision Record

**Prepared by:** Shankar Savalgi
**Project:** Healthcare Image Classification
**Task:** Select a public diagnostic image dataset with a verified source and licence

---

## 1. Selected Dataset

| Field | Details |
|---|---|
| Name | Brain Tumor Dataset (Jun Cheng) |
| Author | Jun Cheng |
| Host | Figshare |
| DOI | https://doi.org/10.6084/m9.figshare.1512427 |
| Modality | MRI |
| Sequence | T1-weighted contrast-enhanced (T1-CE) |
| Total images | 3,064 slices |
| Patients | 233 |
| Image size | Mixed: 512 x 512 and 256 x 256 |
| Planes | Axial, coronal, sagittal |
| File format | MATLAB (.mat) |
| Annotations | Tumor mask and tumor border for each slice |
| Licence | CC BY 4.0 |

## 2. Source and Origin

- Hosted on Figshare by Jun Cheng (first posted 2015; Figshare lists
  multiple versions, so record the version you download).
- Data was collected at Nanfang Hospital and Tianjin Medical
  University General Hospital, China (2005-2010).
- Tumors are pathologically confirmed.

## 3. Classes

| Label | Class | Slices | Patients |
|---|---|---|---|
| 1 | Meningioma | 708 | 82 |
| 2 | Glioma | 1,426 | 89 |
| 3 | Pituitary tumor | 930 | 62 |
| | **Total** | **3,064** | **233** |

Class imbalance: glioma is about 47% of the data; meningioma about 23%.

## 4. Licence and Permitted Use

**Licence:** Creative Commons Attribution 4.0 International (CC BY 4.0)
https://creativecommons.org/licenses/by/4.0/

**Allowed:**
- Download and use the data
- Train machine learning / deep learning models
- Preprocess, augment, and modify the images
- Academic, research, and commercial use

**Conditions:**
- Credit the original author (Jun Cheng)
- Link to the source and the licence
- State if you changed the data
- Do not imply endorsement by the author

## 5. Why This Dataset

1. Official, citable source (Figshare DOI)
2. Clear open licence (CC BY 4.0)
3. Three documented classes with known counts
4. Expert-confirmed labels with tumor masks
5. Widely used benchmark, so results are comparable with published work
6. Supports classification now and segmentation later

## 6. Limitations

- **No healthy / no-tumor class.** All images contain a tumor, so a
  model trained here cannot detect "no tumor".
- **Class imbalance** (see section 3).
- **Small patient count** (233), so risk of overfitting.
- **Mixed image sizes** (512 and 256); resize to one fixed size.
- **Single sequence (T1-CE) and two Chinese hospitals.** Results may
  not generalise to other scanners or populations.
- **Research and education only.** Not for clinical diagnosis.

## 7. Data Leakage Warning (Important)

The 3,064 slices come from only 233 patients, so several slices can
belong to one patient. A random image-level split puts the same
patient in both train and test, which inflates accuracy.

**Rule:** split by patient, not by image.

Planned split (patient-level, stratified by class):
- Train: 70%
- Validation: 15%
- Test: 15%

## 8. Planned Preprocessing

1. Load .mat files and extract image, label, and mask
2. Resize all images to one size (for example 224 x 224)
3. Normalize intensities
4. Convert to 3 channels if using a pretrained model
5. Augment the training set only (flip, small rotation, brightness)
6. Handle imbalance (class weights or weighted sampling)

## 9. Decision

**Approved** for use in this project.

## 10. Citation

Cheng, Jun. (2017). Brain tumor dataset. Figshare.
https://doi.org/10.6084/m9.figshare.1512427

Papers that introduced the dataset:
- Cheng, J. et al. "Enhanced Performance of Brain Tumor
  Classification via Tumor Region Augmentation and Partition."
  PLOS ONE 10(10), 2015.
- Cheng, J. et al. "Retrieval of Brain Tumors by Adaptive Spatial
  Pooling and Fisher Vector Representation." PLOS ONE, 2016.

## 11. Links

| Item | Link |
|---|---|
| Official dataset (DOI) | https://doi.org/10.6084/m9.figshare.1512427 |
| Figshare page | https://figshare.com/articles/dataset/brain_tumor_data-set/1512427/5 |
| Licence (CC BY 4.0) | https://creativecommons.org/licenses/by/4.0/ |
| Project branch | https://github.com/nikeetagurve/healthcare-image-classification/tree/feat/shankar-features-model |

Note: Figshare lists several versions of this dataset. Record the
version you download.
