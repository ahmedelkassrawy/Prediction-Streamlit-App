# Multiple Disease Prediction System

This project is a Streamlit-based web application for predicting the likelihood of three medical conditions: Diabetes, Heart Disease, and Parkinson's Disease, using machine learning models. The application provides an interactive interface for users to input relevant medical data and receive predictions based on pre-trained models.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Directory Structure](#directory-structure)
- [Model Details](#model-details)
- [Customization](#customization)
- [Contributing](#contributing)
- [License](#license)

## Overview
The Multiple Disease Prediction System is a user-friendly web application built with Streamlit. It leverages pre-trained machine learning models to predict the likelihood of Diabetes, Heart Disease, and Parkinson's Disease based on user-provided medical data. The app features a sidebar for easy navigation between different prediction modules and a dark-themed interface for better user experience.

## Features
- **Diabetes Prediction**: Predicts whether a person is diabetic based on inputs like Pregnancies, Glucose, Blood Pressure, Skin Thickness, Insulin, BMI, Diabetes Pedigree Function, and Age.
- **Heart Disease Prediction**: (To be implemented) Predicts the likelihood of heart disease based on relevant medical inputs.
- **Parkinson's Prediction**: (To be implemented) Predicts the likelihood of Parkinson's disease based on relevant medical inputs.
- **Interactive UI**: Built with Streamlit, featuring a sidebar for navigation and a responsive input form.
- **Customizable Theme**: Configured with a dark theme via `.streamlit/config.toml`.

## Installation
To run this project locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/ahmedelkassrawy-prediction-streamlit-app.git
   cd ahmedelkassrawy-prediction-streamlit-app
   ```

2. **Set Up a Virtual Environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   Ensure you have Python 3.8+ installed. Then, install the required packages:
   ```bash
   pip install streamlit streamlit-option-menu scikit-learn
   ```

4. **Update Model Paths**:
   The `mlops.py` file contains hardcoded paths to the model files (`diabetes_model.sav`, `heart_disease_model.sav`, `parkinsons_model.sav`). Update these paths in `mlops.py` to match the location of the `.sav` files on your system. For example:
   ```python
   diabetes_model = pickle.load(open("path/to/diabetes_model.sav", 'rb'))
   heart_disease_model = pickle.load(open("path/to/heart_disease_model.sav", 'rb'))
   parkinsons_model = pickle.load(open("path/to/parkinsons_model.sav", 'rb'))
   ```

## Usage
1. **Run the Application**:
   After updating the model paths, start the Streamlit app by running:
   ```bash
   streamlit run mlops.py
   ```
   Alternatively, use the full path to the `mlops.py` file:
   ```bash
   streamlit run /path/to/mlops.py
   ```

2. **Interact with the App**:
   - Open your web browser and navigate to `http://localhost:8501`.
   - Use the sidebar to select a prediction module (e.g., Diabetes Prediction).
   - Enter the required medical data in the input fields.
   - Click the prediction button (e.g., "Diabetes Test Result") to view the result.

## Directory Structure
```
ahmedelkassrawy-prediction-streamlit-app/
├── README.md                    # Project documentation
├── diabetes_model.sav           # Pre-trained model for diabetes prediction
├── heart_disease_model.sav      # Pre-trained model for heart disease prediction
├── parkinsons_model.sav         # Pre-trained model for Parkinson's prediction
├── mlops.py                     # Main Streamlit application script
├── streamlit.txt                # Command to run the Streamlit app
└── .streamlit/
    └── config.toml              # Streamlit theme configuration
```

## Model Details
- **Diabetes Model**: A pre-trained model (`diabetes_model.sav`) that uses 8 features (Pregnancies, Glucose, Blood Pressure, Skin Thickness, Insulin, BMI, Diabetes Pedigree Function, Age) to predict diabetes.
- **Heart Disease Model**: A pre-trained model (`heart_disease_model.sav`) for heart disease prediction (input fields and logic to be implemented).
- **Parkinson's Model**: A pre-trained model (`parkinsons_model.sav`) for Parkinson's disease prediction (input fields and logic to be implemented).
- The models are saved in `.sav` format using Python's `pickle` module and were likely trained with scikit-learn.

## Customization
- **Model Paths**: Update the file paths in `mlops.py` to match the location of the `.sav` files on your system.
- **Theme**: Modify the `.streamlit/config.toml` file to customize the app's appearance (e.g., change `primaryColor`, `backgroundColor`, etc.).
- **Additional Features**: Extend the `mlops.py` script to add input fields and prediction logic for the Heart Disease and Parkinson's modules.

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m "Add feature"`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

Please ensure your code follows the project's structure and includes appropriate documentation.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
