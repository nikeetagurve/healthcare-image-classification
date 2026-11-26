
# Preprocessing Pipeline Settings

## 1. Image Resizing
- Original image size: 512 x 512
- Target image size: 224 x 224
- Interpolation: Bilinear (order=1)
- Anti-aliasing: Enabled

## 2. Image Normalization
- Method: Per-image Min-Max Normalization
- Minimum pixel value: 0.0
- Maximum pixel value: 1.0
- Output data type: float32

## 3. Tumor Mask Preprocessing
- Target size: 224 x 224
- Interpolation: Nearest Neighbor (order=0)
- Anti-aliasing: Disabled
- Output data type: uint8
- Mask values: 0 and 1

## 4. Dataset Splitting
- Strategy: Patient-level stratified split
- Training: 70%
- Validation: 15%
- Testing: 15%
- Random state: 42
- Total patients: 233
- Total images: 3064

## 5. Data Leakage Prevention
- All images belonging to one patient are assigned to the same split.
- No patient overlap exists between training, validation and testing sets.

## 6. Split Summary

| Split | Patients | Images |
|---|---:|---:|
| Train | 163 | 2124 |
| Validation | 35 | 499 |
| Test | 35 | 441 |
| Total | 233 | 3064 |
