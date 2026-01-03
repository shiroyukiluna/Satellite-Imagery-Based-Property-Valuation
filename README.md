# Satellite-Imagery-Based-Property-Valuation

## Project Overview
Real estate valuation traditionally relies on **tabular property attributes** such as area, number of rooms, location-based indicators, etc. However, such data often fails to capture **spatial and neighborhood context**.

This project explores **property price prediction** using:
1. **Tabular property features**
2. **Satellite imagery**
3. A **multimodal learning approach** that combines both sources

The objective is to study whether incorporating satellite image information improves prediction performance compared to tabular-only models.


## Objectives
- Build a strong baseline using tabular data
- Extract meaningful features from satellite images
- Combine tabular and image features for multimodal prediction
- Compare model performance across different settings
- Analyze the impact of visual information on property valuation


## Methodology & Workflow

### 1️⃣ Data Understanding
**Tabular Data**
- Numerical features (e.g., size, price indicators)
- Categorical features (encoded where required)

**Satellite Images**
- Images corresponding to property locations
- Provide spatial, infrastructure, and neighborhood context


### 2️⃣ Data Preprocessing

#### Tabular Data
- Missing value handling
- Feature scaling (StandardScaler)
- Train–test split

#### Image Data
- Image loading using OpenCV
- Resizing to uniform dimensions
- Normalization
- Conversion to numerical feature vectors
  

### 3️⃣ Feature Engineering

- Tabular feature transformation
- Image feature extraction using:
  - Color statistics
  - Texture-based descriptors
  - Flattened image representations
- Feature alignment between tabular and image samples


### 4️⃣ Model Development

#### Tabular Models
- Random Forest Regressor
- XGBoost

  
#### Multimodal Models
- Concatenation of:
  - Tabular features
  - Image-derived features
- Regression models trained on combined feature space


### 5️⃣ Model Evaluation
- Root Mean Squared Error (RMSE)
- Coefficient of Determination (R^2)
- Comparative analysis:
  - Tabular-only vs Multimodal models
  



