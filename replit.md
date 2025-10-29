# Drug Discovery Prediction Web Application

## Overview
A Flask-based machine learning web application for college project that predicts whether a chemical compound is an Active or Inactive drug based on molecular properties.

## Purpose
This application uses a RandomForestClassifier to predict drug activity based on four key molecular features:
- Molecular Weight (g/mol)
- LogP Value (lipophilicity)
- Number of Hydrogen Donors
- Number of Hydrogen Acceptors

## Current State
The application is fully functional with:
- Flask backend running on port 5000
- Trained RandomForest model with 84% accuracy
- Orange-themed responsive web interface
- Real-time predictions with confidence scores

## Recent Changes (October 29, 2025)
- Initial project setup with Flask, scikit-learn, pandas, and numpy
- Created synthetic drug compound dataset (500 samples)
- Implemented RandomForestClassifier model training
- Built clean orange-themed UI with HTML/CSS
- Added prediction endpoint with confidence display
- Configured Flask workflow to run on port 5000

## Project Architecture

### Backend (app.py)
- **Dataset Generation**: Creates 500 synthetic compound samples with realistic molecular properties
- **Model Training**: RandomForestClassifier (100 estimators) trained on startup
- **API Endpoints**:
  - GET `/`: Serves the main web interface
  - POST `/predict`: Accepts JSON with molecular features, returns prediction and confidence

### Frontend
- **templates/index.html**: Single-page application with input form and results display
- **static/style.css**: Orange gradient theme with responsive design
- **JavaScript**: Handles form submission and dynamic result display

### Dependencies
- Flask: Web framework
- scikit-learn: Machine learning (RandomForestClassifier)
- pandas: Data manipulation
- numpy: Numerical operations

## Features
1. User-friendly input form with validation
2. Real-time prediction without page reload
3. Visual feedback (green for Active, red for Inactive)
4. Prediction confidence percentage
5. Clean, professional orange-themed design
6. Responsive layout for mobile and desktop

## Model Details
- Algorithm: RandomForestClassifier
- Training samples: 400 (80% of dataset)
- Test samples: 100 (20% of dataset)
- Accuracy: ~84%
- Features used: 4 molecular properties
- Output: Binary classification (Active/Inactive)

## How to Use
1. Enter molecular property values in the input fields
2. Click the "Predict" button
3. View the prediction result and confidence score
4. Try different values to see how the model responds

## Example Input Values
- **Active Drug Example**: MW=350, LogP=2.5, H-Donors=3, H-Acceptors=6
- **Inactive Drug Example**: MW=600, LogP=6, H-Donors=7, H-Acceptors=12
