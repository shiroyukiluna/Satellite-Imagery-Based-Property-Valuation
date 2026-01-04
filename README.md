🛰️ Satellite Imagery Based Property Valuation
A Multimodal Machine Learning Framework
1. Introduction

Accurate property valuation is a core problem in real estate analytics. Traditional models rely heavily on structured attributes such as floor area, number of rooms, and geographic coordinates. While effective, these features often fail to capture neighborhood-level spatial context, such as greenery, road structure, and urban density.

This project proposes a multimodal learning approach that integrates tabular property data with satellite imagery to enhance predictive performance and improve model interpretability.

2. Project Objectives

Predict property prices using structured tabular data

Incorporate satellite imagery to capture neighborhood context

Compare tabular-only and multimodal models

Interpret visual model behavior using Grad-CAM

Perform inference on an unseen test dataset


4. Dataset Description
4.1 Tabular Data

Each property includes:

Bedrooms

Bathrooms

Living area (sqft_living)

Latitude and Longitude

Target variable: price

4.2 Satellite Imagery

Source: Mapbox Static Images API

One satellite image per property

Fixed zoom level and resolution

Consistent spatial scale across all images

5. Satellite Image Acquisition

Satellite images were downloaded programmatically using property latitude and longitude.

Key Characteristics:

Automated API-based retrieval

Parallelized downloads using ThreadPoolExecutor

Skipping already-downloaded images

Separate train and test image folders to prevent data leakage

This pipeline ensures scalability and reproducibility.

6. Exploratory Data Analysis (EDA)
6.1 Univariate Analysis

Price distribution is highly right-skewed

Log transformation applied to stabilize variance

Bedrooms and bathrooms are discrete

Living area is continuous and right-skewed

6.2 Bivariate Analysis
6.2.1 Feature–Price Relationships

Living area shows a strong upward trend with price

Bathrooms show moderate correlation

Bedrooms exhibit high variance and weaker predictive power

6.2.2 Correlation Analysis

Living area has the strongest correlation with price

Bathrooms show moderate correlation

Latitude and longitude show weak linear correlation but strong spatial influence

6.3 Geospatial and Satellite Insights

High-priced properties cluster spatially

Satellite imagery reveals greener, less dense neighborhoods for expensive properties

Low-priced properties exhibit dense and irregular layouts

7. Feature Engineering
7.1 Tabular Feature Engineering

Derived features:

sqft_per_bedroom

bath_per_bedroom

rooms_total

sqft_per_room

bathroom_ratio

Target transformation:

price_log = log1p(price)

7.2 CNN-Based Image Features

Pretrained ResNet-18 used as a fixed feature extractor

Final classification layer removed

Produces a 512-dimensional embedding per image

7.3 Dimensionality Reduction

Principal Component Analysis (PCA)

Retained 95% variance

Reduced feature size from 512 → ~279

7.4 Multimodal Feature Fusion

Final feature set:

Engineered Tabular Features + PCA-reduced Image Features


Merged using property ID for alignment.

8. Modeling and Methodology
8.1 Tabular Baseline Models

Random Forest Regressor

XGBoost Regressor

8.2 Multimodal Models

Same model architectures trained on fused features

Enables fair comparison between tabular-only and multimodal learning

8.3 Training Setup

Train–validation split: 80–20

Evaluation metrics: RMSE, R²

Target variable: log-transformed price

9. Model Explainability with Grad-CAM

Grad-CAM was applied to the CNN feature extractor to visualize influential regions.

Observations:

High-priced properties emphasize:

Green cover

Open spaces

Wide road networks

Low-priced properties emphasize:

Dense building clusters

Irregular layouts

Limited greenery

This confirms that the CNN learns meaningful neighborhood-level cues.

10. Test Set Prediction
Inference Pipeline:

Apply identical tabular feature engineering

Extract satellite image embeddings

Apply trained Random Forest model

Convert predictions back to original price scale

Output:
outputs/Predicted_test_prices.csv

11. Results Summary
Model	RMSE	R²
Tabular XGBoost	~0.153	~0.915
Tabular Random Forest	~0.106	~0.956
Multimodal RF	~0.212	~0.843
Multimodal XGBoost	~0.207	~0.850
12. Conclusion

Tabular features provide strong predictive performance

Satellite imagery improves interpretability and spatial understanding

Grad-CAM validates meaningful visual learning

Multimodal learning is especially valuable when structured data is limited

13. Future Work

End-to-end multimodal deep learning

Attention-based fusion strategies

Higher-resolution satellite imagery

Integration of road and land-use data

Cross-city generalization analysis

14. References

Breiman, L. (2001). Random Forests

Chen & Guestrin (2016). XGBoost

He et al. (2016). ResNet

Selvaraju et al. (2017). Grad-CAM

Jolliffe (2002). PCA

Mapbox Static Images API

15. Author

Chetan Agarwal
Multimodal Machine Learning | Computer Vision | Applied ML

If you want next, I can:

Add figures directly into README

Create academic abstract

Prepare conference-ready paper formatting

Optimize README for GitHub stars & recruiters

Just say the word 🚀
