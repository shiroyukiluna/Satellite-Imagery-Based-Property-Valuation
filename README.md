# Satellite Imagery Based Property Valuation
### A Multimodal Machine Learning Framework
## 1. Introduction

Accurate property valuation is a core problem in real estate analytics. Traditional models rely heavily on structured attributes such as floor area, number of rooms, and geographic coordinates. While effective, these features often fail to capture neighborhood-level spatial context, such as greenery, road structure, and urban density.

This project proposes a multimodal learning approach that integrates tabular property data with satellite imagery to enhance predictive performance and improve model interpretability.

## 2. Project Objectives

Predict property prices using structured tabular data

Incorporate satellite imagery to capture neighborhood context

Compare tabular-only and multimodal models

Interpret visual model behavior using Grad-CAM

Perform inference on an unseen test dataset

## 3. Dataset Description
### 3.1 Tabular Data

Each property includes:

1. Bedrooms
2. Bathrooms
3. Living area (sqft_living)
4. Latitude and Longitude
5. Target variable: price

### 3.2 Satellite Imagery

Source: Mapbox Static Images API

One satellite image per property

Fixed zoom level and resolution

Consistent spatial scale across all images

## 4. Satellite Image Acquisition

Satellite images were downloaded programmatically using property latitude and longitude.

Key Characteristics:

1. Automated API-based retrieval
2. Parallelized downloads using ThreadPoolExecutor
3. Skipping already-downloaded image
4. Separate train and test image folders to prevent data leakage

This pipeline ensures scalability and reproducibility.

## 5. Exploratory Data Analysis (EDA)
### 5.1 Univariate Analysis

1. Price distribution is highly right-skewed
2. Log transformation applied to stabilize variance
3. Bedrooms and bathrooms are discrete
4. Living area is continuous and right-skewed

### 5.2 Bivariate Analysis
#### 5.2.1 Feature–Price Relationships

1. Living area shows a strong upward trend with price
2. Bathrooms show moderate correlation
3. Bedrooms exhibit high variance and weaker predictive power

#### 5.2.2 Correlation Analysis

1. Living area has the strongest correlation with price
2. Bathrooms show moderate correlation
3. Latitude and longitude show weak linear correlation but strong spatial influence

### 5.3 Geospatial and Satellite Insights

1. High-priced properties cluster spatially
2. Satellite imagery reveals greener, less dense neighborhoods for expensive properties
3. Low-priced properties exhibit dense and irregular layouts

## 6. Feature Engineering
### 6.1 Tabular Feature Engineering

Derived features:

1. sqft_per_bedroom
2. bath_per_bedroom
3. rooms_total
4. sqft_per_room
5. bathroom_ratio

Target transformation: price_log = log1p(price)

### 6.2 CNN-Based Image Features

1. Pretrained ResNet-18 used as a fixed feature extractor
2. Final classification layer removed
3. Produces a 512-dimensional embedding per image

### 6.3 Dimensionality Reduction

1. Principal Component Analysis (PCA)
2. Retained 95% variance
3. Reduced feature size from 512 → ~279


### 6.4 Multimodal Feature Fusion

Final feature set:

Engineered Tabular Features + PCA-reduced Image Features

Merged using property ID for alignment.

## 7. Modeling and Methodology
### 7.1 Tabular Baseline Models

Random Forest Regressor

XGBoost Regressor

### 7.2 Multimodal Models

Same model architectures trained on fused features

Enables fair comparison between tabular-only and multimodal learning

### 7.3 Training Setup

Train–validation split: 80–20

Evaluation metrics: RMSE, R²

Target variable: log-transformed price

## 8. Model Explainability with Grad-CAM

Grad-CAM was applied to the CNN feature extractor to visualize influential regions.

Observations:

1. High-priced properties emphasize:
2. Green cover
3. Open spaces
4. Wide road networks

Low-priced properties emphasize:

1. Dense building clusters
2. Irregular layouts
3. Limited greenery

This confirms that the CNN learns meaningful neighborhood-level cues.

## 9. Test Set Prediction
Inference Pipeline:

1. Apply identical tabular feature engineering
2. Extract satellite image embeddings
3. Apply trained Random Forest model
4. Convert predictions back to original price scale

Output:
outputs/Predicted_test_prices.csv

## 10. Results Summary
Model	RMSE	R²
Tabular XGBoost	~0.153	~0.915
Tabular Random Forest	~0.106	~0.956
Multimodal RF	~0.212	~0.843
Multimodal XGBoost	~0.207	~0.850

## 11. Conclusion

1. Tabular features provide strong predictive performance
2. Satellite imagery improves interpretability and spatial understanding
3. Grad-CAM validates meaningful visual learning
4. Multimodal learning is especially valuable when structured data is limited

## 12. Future Work

1. End-to-end multimodal deep learning
2. Attention-based fusion strategies
3. Higher-resolution satellite imagery
4. Integration of road and land-use data
5. Cross-city generalization analysis

## 13. References

1. Breiman, L. (2001). Random Forests
2. Chen & Guestrin (2016). XGBoost
3. He et al. (2016). ResNet
4. Selvaraju et al. (2017). Grad-CAM
5. Jolliffe (2002). PCA
6. Mapbox Static Images API

## 14. Author

Chetan Agarwal
