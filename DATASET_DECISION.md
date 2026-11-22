# Dataset Decision Record

**Prepared by:** Shankar Savalgi

## Selected Dataset
Brain Tumor MRI Dataset

## Original Source
Jun Cheng – Figshare

https://doi.org/10.6084/m9.figshare.1512427

## Dataset Description
The dataset contains 3,064 T1-weighted
contrast-enhanced brain MRI image slices
collected from 233 patients.

## Classes
1. Meningioma – 708 images
2. Glioma – 1,426 images
3. Pituitary Tumor – 930 images

## Licence
Creative Commons Attribution 4.0 International
(CC BY 4.0).

## Permitted Usage
- Academic research
- Machine learning and deep learning
- Image classification
- Image preprocessing and augmentation
- Tumor segmentation using provided annotations

Attribution to the original author and dataset
source is required.

## Decision
Selected because the dataset has an official
research repository, documented image classes,
a clear reuse licence and MRI images suitable
for medical image analysis.

## Important Limitation
The dataset contains tumor-positive images only.
It does not include a healthy/no-tumor class.
It is intended for research and educational
purposes, not standalone clinical diagnosis.

## Evaluation Note
Images come from only 233 patients, so multiple
slices can belong to one patient. Use a
patient-level train/test split to avoid data leakage.

## Citation
Cheng, Jun. Brain tumor dataset. Figshare.
https://doi.org/10.6084/m9.figshare.1512427
