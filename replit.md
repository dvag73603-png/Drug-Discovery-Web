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

## Recent Changes (October 30, 2025)
- **Major UI Redesign**: Completely redesigned the landing page with modern professional layout
- **Horizontal Input Layout**: Changed input fields from vertical to horizontal grid layout
- **Molecular Illustrations**: Added custom SVG molecular structure graphics and animations
- **About Section**: Implemented comprehensive About section with three cards explaining ML, Lipinski's Rule, and drug candidates
- **Visual Enhancements**: Added floating molecule decorations, pulsing animations, and hover effects
- **White & Orange Theme**: Redesigned color scheme with white background and orange accents
- **Responsive Design**: Enhanced mobile and tablet responsiveness with breakpoints
- **Professional Landing Page**: Transformed into a real-world web application appearance

Previous Changes (October 29, 2025):
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
- **templates/index.html**: Modern landing page with:
  - SVG molecular illustrations (floating decorations and icons)
  - Horizontal 4-column input grid
  - About section with three informational cards
  - Result display area with animations
  - Information banner explaining how it works
- **static/style.css**: Professional white & orange theme with:
  - CSS animations (floating, pulsing, bouncing)
  - Hover effects on cards and buttons
  - Gradient backgrounds and shadows
  - Responsive grid layouts with media queries
  - Modern typography and spacing
- **JavaScript**: Handles form submission, API calls, and dynamic result display with smooth animations

### Dependencies
- Flask: Web framework
- scikit-learn: Machine learning (RandomForestClassifier)
- pandas: Data manipulation
- numpy: Numerical operations

## Features
1. **Modern Landing Page**: Professional design with molecular illustrations
2. **Horizontal Input Layout**: Four input fields in a clean row
3. **Real-Time Predictions**: AJAX-based predictions without page reload
4. **Visual Feedback**: Green for Active Drug, Red for Inactive Drug
5. **Confidence Scores**: Percentage confidence displayed with results
6. **Animated Graphics**: SVG molecules with floating and pulsing animations
7. **About Section**: Educational content about drug discovery and Lipinski's Rule
8. **Fully Responsive**: Mobile, tablet, and desktop optimized
9. **Hover Effects**: Interactive elements with smooth transitions
10. **Clean White & Orange Theme**: Professional pharmaceutical aesthetic

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
