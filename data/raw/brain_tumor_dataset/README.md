# Brain Tumor Dataset - Raw Data

## Dataset Information
- Dataset Name: Brain Tumor Dataset (Jun Cheng)
- Author: Jun Cheng
- Source: Figshare
- DOI: https://doi.org/10.6084/m9.figshare.1512427
- Dataset Version: https://figshare.com/articles/dataset/brain_tumor_data-set/1512427/5
- License: CC BY 4.0
- Modality: T1-weighted contrast-enhanced MRI

## Dataset Statistics
- Total Images: 3,064
- Total Patients: 233
- Meningioma: 708 images
- Glioma: 1,426 images
- Pituitary Tumor: 930 images

## Acquisition Details
- Downloaded from the official Figshare Version 5 dataset.
- Downloaded four ZIP archives containing 766 MATLAB files each.
- Downloaded `cvind.mat` and the original `README.txt`.
- Extracted all 3,064 `.mat` image files into this directory.
- All 3,064 image files were verified after extraction.
- Original ZIP archives were retained separately in the Downloads folder.
- Acquisition Date: 22 November 2026.

## Raw Data Policy
- Original dataset files must remain unchanged.
- No resizing, normalization, augmentation, or preprocessing in this directory.
- All transformations must be performed in data/interim or data/processed.
- Raw dataset files should not be committed to Git without team approval.
- The raw dataset is excluded from Git tracking through `.gitignore`.

## Important Note
This dataset contains three tumor categories and does not contain a healthy/no-tumor class.
It is intended for research and educational purposes, not clinical diagnosis.