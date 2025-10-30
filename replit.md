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

### Latest Update: Medicine Search Feature ✨
- **Medicine Database Search**: Added search box to look up any medicine by name
- **Auto-Fill Functionality**: Automatically populates molecular properties from PubChem database
- **PubChem API Integration**: Connected to world's largest free chemistry database (100M+ compounds)
- **Real-Time Data**: Fetches Molecular Weight, LogP, H-Donors, and H-Acceptors instantly
- **Error Handling**: Clear error messages for medicine not found or connection issues
- **Rate Limiting**: Implemented proper API rate limiting (5 requests/second)
- **Enter Key Support**: Press Enter to search for quicker interaction

### Earlier Updates: UI Redesign
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
- **Lipinski's Rule of Five Implementation**: Direct rule-based prediction for drug-likeness
- **PubChem API Integration**: Queries PubChem database for compound molecular properties
- **API Endpoints**:
  - GET `/`: Serves the main web interface
  - POST `/search`: Searches PubChem database by medicine name, returns molecular properties
  - POST `/predict`: Accepts JSON with molecular features, returns prediction and confidence based on Lipinski's Rule

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
- requests: HTTP library for PubChem API calls
- Python 3.11: Programming language

## Features
1. **Medicine Database Search** 🔍: Search any medicine name to auto-fill molecular properties from PubChem
2. **Auto-Fill from Database**: Instantly populate all four fields with real compound data
3. **Modern Landing Page**: Professional design with molecular illustrations
4. **Horizontal Input Layout**: Four input fields in a clean row
5. **Real-Time Predictions**: AJAX-based predictions without page reload
6. **Visual Feedback**: Green for Active Drug, Red for Inactive Drug
7. **Lipinski's Rule of Five**: Evidence-based prediction algorithm used in pharmaceutical research
8. **Animated Graphics**: SVG molecules with floating and pulsing animations
9. **About Section**: Educational content about drug discovery and Lipinski's Rule
10. **Fully Responsive**: Mobile, tablet, and desktop optimized
11. **Hover Effects**: Interactive elements with smooth transitions
12. **Clean White & Orange Theme**: Professional pharmaceutical aesthetic
13. **Error Handling**: Clear feedback for search errors and invalid inputs

## Prediction Model Details
- **Algorithm**: Lipinski's Rule of Five (rule-based system)
- **Basis**: Pharmaceutical industry standard for drug-likeness evaluation
- **Rules Evaluated**:
  - Molecular Weight ≤ 500 Da
  - LogP ≤ 5 (lipophilicity)
  - Hydrogen Bond Donors ≤ 5
  - Hydrogen Bond Acceptors ≤ 10
- **Decision Criteria**: Compound must satisfy 3 out of 4 rules to be classified as "Active Drug"
- **Confidence Score**: Based on percentage of rules satisfied (0-100%)
- **Output**: Binary classification (Active/Inactive) with confidence percentage

## How to Use

### Method 1: Search Medicine Database (Recommended)
1. Enter a medicine name in the search box (e.g., "Aspirin", "Ibuprofen", "Paracetamol")
2. Click "Search" or press Enter
3. The four molecular properties will automatically fill in
4. Click "Predict" to see if it's an Active or Inactive drug
5. View the prediction result and confidence score

### Method 2: Manual Entry
1. Manually enter molecular property values in the four input fields
2. Click the "Predict" button
3. View the prediction result and confidence score

## Example Medicines to Search
- **Aspirin**: Common pain reliever
- **Ibuprofen**: Anti-inflammatory drug
- **Paracetamol**: Pain and fever reducer (also known as Acetaminophen)
- **Caffeine**: Stimulant found in coffee and tea
- **Metformin**: Diabetes medication
- **Atorvastatin**: Cholesterol-lowering drug (Lipitor)

## Example Manual Input Values
- **Active Drug Example**: MW=350, LogP=2.5, H-Donors=3, H-Acceptors=6
- **Inactive Drug Example**: MW=600, LogP=6, H-Donors=7, H-Acceptors=12
