import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Loading the saved models with corrected paths
diabetes_model = pickle.load(open(r"D:\Enviroment\MLops\diabetes_model.sav", 'rb'))
heart_disease_model = pickle.load(open(r"D:\Enviroment\MLops\heart_disease_model.sav", 'rb'))
parkinsons_model = pickle.load(open(r"D:\Enviroment\MLops\parkinsons_model.sav", 'rb'))

# Sidebar for navigation
with st.sidebar:
    selected = option_menu(
        'Multiple Disease Prediction System',
        ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Prediction'],
        menu_icon='hospital-fill',
        icons=['activity', 'heart', 'person'],
        default_index=0
    )

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using ML')
    
    # Getting the input data from the user
    col1, col2, col3 = st.columns(3)
    with col1:
        Pregnancies = st.number_input('Number of Pregnancies', min_value=0, max_value=20, value=0)
    with col2:
        Glucose = st.number_input('Glucose Level', min_value=0, max_value=300, value=0)
    with col3:
        BloodPressure = st.number_input('Blood Pressure value', min_value=0, max_value=200, value=0)
    with col1:
        SkinThickness = st.number_input('Skin Thickness value', min_value=0, max_value=100, value=0)
    with col2:
        Insulin = st.number_input('Insulin Level', min_value=0, max_value=1000, value=0)
    with col3:
        BMI = st.number_input('BMI value', min_value=0.0, max_value=100.0, value=0.0)
    with col1:
        DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function value', min_value=0.0, max_value=2.5, value=0.0)
    with col2:
        Age = st.number_input('Age of the Person', min_value=0, max_value=120, value=0)
    
    # Prediction
    diab_diagnosis = ''
    if st.button('Diabetes Test Result'):
        try:
            user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
            diab_prediction = diabetes_model.predict([user_input])
            diab_diagnosis = 'The person is diabetic' if diab_prediction[0] == 1 else 'The person is not diabetic'
            st.success(diab_diagnosis)
        except Exception as e:
            st.error(f"An error occurred: {e}")

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')
    # Add input fields and prediction logic for heart disease here

# Parkinson's Prediction Page
if selected == 'Parkinsons Prediction':
    st.title('Parkinsons Prediction using ML')
    # Add input fields and prediction logic for Parkinson's here