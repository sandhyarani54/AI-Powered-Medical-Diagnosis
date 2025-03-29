import streamlit as st
import pickle
import time
from streamlit_option_menu import option_menu

# Change Name & Logo
st.set_page_config(
    page_title="Disease Prediction",
    page_icon="⚕️",
    layout="wide"
)

# Hiding Streamlit add-ons and improving overall styling
hide_st_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* Custom styling */
.stSelectbox > div > div {background-color: rgba(255,255,255,0.9);}
.stNumberInput > div > div > input {background-color: rgba(255,255,255,0.9);}
.stTextInput > div > div > input {background-color: rgba(255,255,255,0.9);}
.stButton > button {
    border: 2px solid #4CAF50;
    border-radius: 5px;
    color: white;
    background-color: #4CAF50;
    padding: 8px 16px;
    font-size: 16px;
    font-weight: bold;
    transition: all 0.3s;
}
.stButton > button:hover {
    background-color: #45a049;
    border-color: #45a049;
    transform: scale(1.05);
}
.css-1aumxhk {
    background-color: rgba(255, 255, 255, 0.1);
    border-radius: 10px;
    padding: 20px;
}
</style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

# Adding improved Background Image with overlay
background_image_url = "https://www.strategyand.pwc.com/m1/en/strategic-foresight/sector-strategies/healthcare/ai-powered-healthcare-solutions/img01-section1.jpg"

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] {{
    background-image: url({background_image_url});
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
    background-color: rgba(0, 0, 0, 0.7);
}}

[data-testid="stAppViewContainer"]::before {{
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: linear-gradient(135deg, rgba(0, 119, 182, 0.8) 0%, rgba(0, 180, 216, 0.7) 100%);
    opacity: 0.9;
}}

[data-testid="stHeader"] {{
    background-color: rgba(0, 0, 0, 0.5);
}}

[data-testid="stToolbar"] {{
    right: 2rem;
}}

/* Card styling */
.custom-card {{
    background-color: rgba(255, 255, 255, 0.95);
    border-radius: 15px;
    padding: 25px;
    box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
    margin-bottom: 20px;
    border-left: 5px solid #4CAF50;
}}

.custom-card h2 {{
    color: #2c3e50;
    border-bottom: 2px solid #f0f0f0;
    padding-bottom: 10px;
}}

/* Result styling */
.result-success {{
    color: #28a745;
    font-weight: bold;
    font-size: 18px;
    padding: 15px;
    background-color: rgba(40, 167, 69, 0.1);
    border-radius: 5px;
    border-left: 5px solid #28a745;
}}

.result-warning {{
    color: #ffc107;
    font-weight: bold;
    font-size: 18px;
    padding: 15px;
    background-color: rgba(255, 193, 7, 0.1);
    border-radius: 5px;
    border-left: 5px solid #ffc107;
}}

.result-danger {{
    color: #dc3545;
    font-weight: bold;
    font-size: 18px;
    padding: 15px;
    background-color: rgba(220, 53, 69, 0.1);
    border-radius: 5px;
    border-left: 5px solid #dc3545;
}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# Add custom header with logo
st.markdown("""
<div style="display: flex; align-items: center; margin-bottom: 20px;">
    <h1 style="color: white; margin: 0; font-size: 2.5rem;">Medical Diagnosis System</h1>
    <span style="margin-left: auto; color: white; font-size: 1.2rem;">Advanced Disease Prediction System</span>
</div>
""", unsafe_allow_html=True)

# Load the saved models with error handling
try:
    models = {
        'diabetes': pickle.load(open('Models/diabetes_model.sav', 'rb')),
        'heart_disease': pickle.load(open('Models/heart_disease_model.sav', 'rb')),
        'parkinsons': pickle.load(open('Models/parkinsons_model.sav', 'rb')),
        'lung_cancer': pickle.load(open('Models/lungs_disease_model.sav', 'rb')),
        'thyroid': pickle.load(open('Models/Thyroid_model.sav', 'rb'))
    }
except Exception as e:
    st.error(f"Error loading models: {str(e)}")
    st.stop()

# Sidebar with navigation and info
with st.sidebar:
    st.markdown("""
    <div style="background-color: rgba(0, 119, 182, 0.9); padding: 20px; border-radius: 10px; margin-bottom: 20px;">
        <h3 style="color: white; text-align: center;">About This AI Model</h3>
        <p style="color: white;">This application uses machine learning models to predict potential health conditions based on your input data. Please consult with a healthcare professional for accurate diagnosis.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="background-color: rgba(255, 255, 255, 0.9); padding: 15px; border-radius: 10px;">
        <h4 style="color: #2c3e50; text-align: center;">Quick Links</h4>
        <ul style="color: #2c3e50;">
            <li><a href="#diabetes-prediction" style="color: #2c3e50;">Diabetes Prediction</a></li>
            <li><a href="#heart-disease-prediction" style="color: #2c3e50;">Heart Disease Prediction</a></li>
            <li><a href="#parkinsons-prediction" style="color: #2c3e50;">Parkinson's Prediction</a></li>
            <li><a href="#lung-cancer-prediction" style="color: #2c3e50;">Lung Cancer Prediction</a></li>
            <li><a href="#thyroid-prediction" style="color: #2c3e50;">Thyroid Prediction</a></li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# Create a dropdown menu for disease prediction with icons
selected = option_menu(
    menu_title=None,
    options=['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Prediction', 
             'Lung Cancer Prediction', 'Hypo-Thyroid Prediction'],
    icons=['droplet', 'heart-pulse', 'person-walking', 'lungs', 'activity'],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "rgba(255,255,255,0.7)"},
        "icon": {"color": "orange", "font-size": "18px"}, 
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#4CAF50"},
    }
)

def display_input(label, tooltip, key, type="text", min_value=None, max_value=None):
    """Enhanced input field with validation and better styling"""
    col1, col2 = st.columns([1, 3])
    with col1:
        st.markdown(f"<p style='color: white; font-weight: bold;'>{label}</p>", unsafe_allow_html=True)
    with col2:
        if type == "text":
            return st.text_input(label, key=key, help=tooltip, label_visibility="collapsed")
        elif type == "number":
            # Determine step based on min_value type
            if min_value is not None and isinstance(min_value, float):
                step = 0.01
            else:
                step = 1
            
            # Ensure consistent types
            if min_value is not None and max_value is not None:
                if isinstance(min_value, float) or isinstance(max_value, float):
                    min_value = float(min_value)
                    max_value = float(max_value)
                    step = float(step)
                else:
                    min_value = int(min_value) if min_value is not None else None
                    max_value = int(max_value) if max_value is not None else None
                    step = int(step)
            
            return st.number_input(
                label, 
                key=key, 
                help=tooltip, 
                step=step,
                min_value=min_value, 
                max_value=max_value, 
                label_visibility="collapsed"
            )

def show_result(message, is_positive):
    """Show result with appropriate styling"""
    if is_positive:
        st.markdown(f'<div class="result-warning">{message}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="result-success">{message}</div>', unsafe_allow_html=True)

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    with st.container():
        st.markdown('<div class="custom-card">', unsafe_allow_html=True)
        st.markdown("<h2 id='diabetes-prediction'>Diabetes Risk Assessment</h2>", unsafe_allow_html=True)
        st.write("Please enter your health metrics to assess your risk for diabetes.")
        
        col1, col2 = st.columns(2)
        
        with col1:
            Pregnancies = display_input('Number of Pregnancies', 'Enter number of times pregnant', 'Pregnancies', 'number', 0, 20)
            Glucose = display_input('Glucose Level (mg/dL)', 'Enter glucose level (normal range: 70-99 mg/dL)', 'Glucose', 'number', 0, 300)
            BloodPressure = display_input('Blood Pressure (mmHg)', 'Enter blood pressure value (normal: <120/80 mmHg)', 'BloodPressure', 'number', 0, 200)
            SkinThickness = display_input('Skin Thickness (mm)', 'Enter skin thickness value', 'SkinThickness', 'number', 0, 100)
        
        with col2:
            Insulin = display_input('Insulin Level (μU/mL)', 'Enter insulin level (normal: 2-25 μU/mL)', 'Insulin', 'number', 0, 1000)
            BMI = display_input('BMI Value', 'Enter Body Mass Index value (normal: 18.5-24.9)', 'BMI', 'number', 10, 60)
            DiabetesPedigreeFunction = display_input('Diabetes Pedigree Function', 'Enter diabetes pedigree function value', 'DiabetesPedigreeFunction', 'number', 0.0, 2.5)
            Age = display_input('Age', 'Enter age of the person', 'Age', 'number', 0, 120)
        
        if st.button('Assess Diabetes Risk', key='diabetes_btn'):
            with st.spinner('Analyzing your data...'):
                time.sleep(1)  # Simulate processing time
                diab_prediction = models['diabetes'].predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
                if diab_prediction[0] == 1:
                    show_result('The model indicates a potential risk for diabetes. Please consult with a healthcare professional for further evaluation.', True)
                    st.warning("Disclaimer: This is a predictive model, not a diagnosis. Always consult with a healthcare provider.")
                else:
                    show_result('The model indicates no significant risk for diabetes based on the provided information.', False)
                st.balloons()
        
        st.markdown('</div>', unsafe_allow_html=True)

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':
    with st.container():
        st.markdown('<div class="custom-card">', unsafe_allow_html=True)
        st.markdown("<h2 id='heart-disease-prediction'>Heart Disease Risk Assessment</h2>", unsafe_allow_html=True)
        st.write("Please enter your cardiovascular health metrics to assess your risk for heart disease.")
        
        col1, col2 = st.columns(2)
        
        with col1:
            age = display_input('Age', 'Enter age of the person', 'age', 'number', 0, 120)
            sex = display_input('Sex (1 = male; 0 = female)', 'Enter sex of the person', 'sex', 'number', 0, 1)
            cp = display_input('Chest Pain types (0-3)', '0: Typical angina, 1: Atypical angina, 2: Non-anginal pain, 3: Asymptomatic', 'cp', 'number', 0, 3)
            trestbps = display_input('Resting Blood Pressure (mmHg)', 'Enter resting blood pressure (normal: <120 mmHg)', 'trestbps', 'number', 50, 250)
            chol = display_input('Serum Cholesterol (mg/dL)', 'Enter serum cholesterol (desirable: <200 mg/dL)', 'chol', 'number', 100, 600)
            fbs = display_input('Fasting Blood Sugar > 120 mg/dl', '1 = true; 0 = false', 'fbs', 'number', 0, 1)
            restecg = display_input('Resting ECG results (0-2)', '0: Normal, 1: ST-T wave abnormality, 2: Probable or definite left ventricular hypertrophy', 'restecg', 'number', 0, 2)
        
        with col2:
            thalach = display_input('Maximum Heart Rate', 'Enter maximum heart rate achieved', 'thalach', 'number', 60, 220)
            exang = display_input('Exercise Induced Angina', '1 = yes; 0 = no', 'exang', 'number', 0, 1)
            oldpeak = display_input('ST Depression', 'ST depression induced by exercise relative to rest', 'oldpeak', 'number', 0.0, 6.2)
            slope = display_input('Slope of Peak Exercise ST', '0: Upsloping, 1: Flat, 2: Downsloping', 'slope', 'number', 0, 2)
            ca = display_input('Major Vessels (0-3)', 'Number of major vessels colored by fluoroscopy', 'ca', 'number', 0, 3)
            thal = display_input('Thalassemia', '0 = normal; 1 = fixed defect; 2 = reversible defect', 'thal', 'number', 0, 2)
        
        if st.button('Assess Heart Disease Risk', key='heart_btn'):
            with st.spinner('Analyzing your cardiovascular data...'):
                time.sleep(1)
                heart_prediction = models['heart_disease'].predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
                if heart_prediction[0] == 1:
                    show_result('The model indicates a potential risk for heart disease. Please consult with a cardiologist for further evaluation.', True)
                    st.warning("Important: This prediction should not replace professional medical advice.")
                else:
                    show_result('The model indicates no significant risk for heart disease based on the provided information.', False)
                st.balloons()
        
        st.markdown('</div>', unsafe_allow_html=True)

# Parkinson's Prediction Page
if selected == "Parkinsons Prediction":
    with st.container():
        st.markdown('<div class="custom-card">', unsafe_allow_html=True)
        st.markdown("<h2 id='parkinsons-prediction'>Parkinson's Disease Risk Assessment</h2>", unsafe_allow_html=True)
        st.write("Please enter voice measurement data to assess risk for Parkinson's disease.")
        
        col1, col2 = st.columns(2)
        
        with col1:
            fo = display_input('MDVP:Fo(Hz)', 'Average vocal fundamental frequency', 'fo', 'number', 80, 260)
            fhi = display_input('MDVP:Fhi(Hz)', 'Maximum vocal fundamental frequency', 'fhi', 'number', 100, 600)
            flo = display_input('MDVP:Flo(Hz)', 'Minimum vocal fundamental frequency', 'flo', 'number', 70, 250)
            Jitter_percent = display_input('MDVP:Jitter(%)', 'Measure of frequency variation', 'Jitter_percent', 'number', 0.0, 0.1)
            Jitter_Abs = display_input('MDVP:Jitter(Abs)', 'Absolute jitter measure', 'Jitter_Abs', 'number', 0.0, 0.0001)
            RAP = display_input('MDVP:RAP', 'Relative amplitude perturbation', 'RAP', 'number', 0.0, 0.1)
            PPQ = display_input('MDVP:PPQ', 'Five-point period perturbation quotient', 'PPQ', 'number', 0.0, 0.1)
            DDP = display_input('Jitter:DDP', 'Average absolute difference of differences between cycles', 'DDP', 'number', 0.0, 0.1)
        
        with col2:
            Shimmer = display_input('MDVP:Shimmer', 'Measure of amplitude variation', 'Shimmer', 'number', 0.0, 0.2)
            Shimmer_dB = display_input('MDVP:Shimmer(dB)', 'Shimmer in decibels', 'Shimmer_dB', 'number', 0.0, 1.0)
            APQ3 = display_input('Shimmer:APQ3', 'Three-point amplitude perturbation quotient', 'APQ3', 'number', 0.0, 0.2)
            APQ5 = display_input('Shimmer:APQ5', 'Five-point amplitude perturbation quotient', 'APQ5', 'number', 0.0, 0.2)
            APQ = display_input('MDVP:APQ', 'Amplitude perturbation quotient', 'APQ', 'number', 0.0, 0.2)
            DDA = display_input('Shimmer:DDA', 'Average absolute difference between consecutive differences', 'DDA', 'number', 0.0, 0.2)
            NHR = display_input('NHR', 'Noise-to-harmonics ratio', 'NHR', 'number', 0.0, 0.5)
            HNR = display_input('HNR', 'Harmonics-to-noise ratio', 'HNR', 'number', 0, 40)
        
        col3, col4 = st.columns(2)
        
        with col3:
            RPDE = display_input('RPDE', 'Nonlinear dynamical complexity measure', 'RPDE', 'number', 0.0, 1.0)
            DFA = display_input('DFA', 'Signal fractal scaling exponent', 'DFA', 'number', 0.4, 0.9)
        
        with col4:
            spread1 = display_input('Spread1', 'Nonlinear measure of fundamental frequency variation', 'spread1', 'number', -10.0, 0.0)
            spread2 = display_input('Spread2', 'Nonlinear measure of fundamental frequency variation', 'spread2', 'number', 0.0, 0.5)
            PPE = display_input('PPE', 'Pitch period entropy', 'PPE', 'number', 0.0, 0.5)
        
        if st.button("Assess Parkinson's Risk", key='parkinsons_btn'):
            with st.spinner('Analyzing voice measurement data...'):
                time.sleep(1)
                parkinsons_prediction = models['parkinsons'].predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, PPE]])
                if parkinsons_prediction[0] == 1:
                    show_result("The model indicates potential signs of Parkinson's disease. Please consult with a neurologist for further evaluation.", True)
                    st.warning("Note: This assessment is based on voice analysis and should be confirmed with clinical evaluation.")
                else:
                    show_result("The model indicates no significant signs of Parkinson's disease based on the provided information.", False)
                st.balloons()
        
        st.markdown('</div>', unsafe_allow_html=True)

# Lung Cancer Prediction Page
if selected == "Lung Cancer Prediction":
    with st.container():
        st.markdown('<div class="custom-card">', unsafe_allow_html=True)
        st.markdown("<h2 id='lung-cancer-prediction'>Lung Cancer Risk Assessment</h2>", unsafe_allow_html=True)
        st.write("Please answer the following questions to assess your risk for lung cancer.")
        
        col1, col2 = st.columns(2)
        
        with col1:
            GENDER = display_input('Gender (1 = Male; 0 = Female)', 'Enter gender of the person', 'GENDER', 'number', 0, 1)
            AGE = display_input('Age', 'Enter age of the person', 'AGE', 'number', 0, 120)
            SMOKING = display_input('Smoking (1 = Yes; 0 = No)', 'Enter if the person smokes', 'SMOKING', 'number', 0, 1)
            YELLOW_FINGERS = display_input('Yellow Fingers (1 = Yes; 0 = No)', 'Enter if the person has yellow fingers', 'YELLOW_FINGERS', 'number', 0, 1)
            ANXIETY = display_input('Anxiety (1 = Yes; 0 = No)', 'Enter if the person has anxiety', 'ANXIETY', 'number', 0, 1)
            PEER_PRESSURE = display_input('Peer Pressure (1 = Yes; 0 = No)', 'Enter if the person is under peer pressure', 'PEER_PRESSURE', 'number', 0, 1)
            CHRONIC_DISEASE = display_input('Chronic Disease (1 = Yes; 0 = No)', 'Enter if the person has a chronic disease', 'CHRONIC_DISEASE', 'number', 0, 1)
        
        with col2:
            FATIGUE = display_input('Fatigue (1 = Yes; 0 = No)', 'Enter if the person experiences fatigue', 'FATIGUE', 'number', 0, 1)
            ALLERGY = display_input('Allergy (1 = Yes; 0 = No)', 'Enter if the person has allergies', 'ALLERGY', 'number', 0, 1)
            WHEEZING = display_input('Wheezing (1 = Yes; 0 = No)', 'Enter if the person experiences wheezing', 'WHEEZING', 'number', 0, 1)
            ALCOHOL_CONSUMING = display_input('Alcohol Consuming (1 = Yes; 0 = No)', 'Enter if the person consumes alcohol', 'ALCOHOL_CONSUMING', 'number', 0, 1)
            COUGHING = display_input('Coughing (1 = Yes; 0 = No)', 'Enter if the person experiences coughing', 'COUGHING', 'number', 0, 1)
            SHORTNESS_OF_BREATH = display_input('Shortness Of Breath (1 = Yes; 0 = No)', 'Enter if the person experiences shortness of breath', 'SHORTNESS_OF_BREATH', 'number', 0, 1)
            SWALLOWING_DIFFICULTY = display_input('Swallowing Difficulty (1 = Yes; 0 = No)', 'Enter if the person has difficulty swallowing', 'SWALLOWING_DIFFICULTY', 'number', 0, 1)
            CHEST_PAIN = display_input('Chest Pain (1 = Yes; 0 = No)', 'Enter if the person experiences chest pain', 'CHEST_PAIN', 'number', 0, 1)
        
        if st.button("Assess Lung Cancer Risk", key='lung_btn'):
            with st.spinner('Evaluating risk factors...'):
                time.sleep(1)
                lungs_prediction = models['lung_cancer'].predict([[GENDER, AGE, SMOKING, YELLOW_FINGERS, ANXIETY, PEER_PRESSURE, CHRONIC_DISEASE, FATIGUE, ALLERGY, WHEEZING, ALCOHOL_CONSUMING, COUGHING, SHORTNESS_OF_BREATH, SWALLOWING_DIFFICULTY, CHEST_PAIN]])
                if lungs_prediction[0] == 1:
                    show_result("The model indicates potential risk factors for lung cancer. Please consult with a pulmonologist for further evaluation.", True)
                    st.warning("Important: Early detection is crucial. This prediction should prompt professional medical consultation.")
                else:
                    show_result("The model indicates no significant risk factors for lung cancer based on the provided information.", False)
                st.balloons()
        
        st.markdown('</div>', unsafe_allow_html=True)

# Hypo-Thyroid Prediction Page
if selected == "Hypo-Thyroid Prediction":
    with st.container():
        st.markdown('<div class="custom-card">', unsafe_allow_html=True)
        st.markdown("<h2 id='thyroid-prediction'>Hypo-Thyroid Risk Assessment</h2>", unsafe_allow_html=True)
        st.write("Please enter your thyroid-related health metrics to assess your risk for hypo-thyroidism.")
        
        col1, col2 = st.columns(2)
        
        with col1:
            age = display_input('Age', 'Enter age of the person', 'age', 'number', 0, 120)
            sex = display_input('Sex (1 = Male; 0 = Female)', 'Enter sex of the person', 'sex', 'number', 0, 1)
            on_thyroxine = display_input('On Thyroxine (1 = Yes; 0 = No)', 'Enter if the person is on thyroxine medication', 'on_thyroxine', 'number', 0, 1)
            tsh = display_input('TSH Level (mIU/L)', 'Thyroid Stimulating Hormone level (normal: 0.4-4.0 mIU/L)', 'tsh', 'number', 0.0, 100.0)
        
        with col2:
            t3_measured = display_input('T3 Measured (1 = Yes; 0 = No)', 'Enter if T3 was measured', 't3_measured', 'number', 0, 1)
            t3 = display_input('T3 Level (ng/dL)', 'Triiodothyronine level (normal: 80-200 ng/dL)', 't3', 'number', 0, 500)
            tt4 = display_input('TT4 Level (μg/dL)', 'Total Thyroxine level (normal: 4.5-12.5 μg/dL)', 'tt4', 'number', 0, 50)
        
        if st.button("Assess Thyroid Risk", key='thyroid_btn'):
            with st.spinner('Analyzing thyroid function...'):
                time.sleep(1)
                thyroid_prediction = models['thyroid'].predict([[age, sex, on_thyroxine, tsh, t3_measured, t3, tt4]])
                if thyroid_prediction[0] == 1:
                    show_result("The model indicates potential signs of hypo-thyroidism. Please consult with an endocrinologist for further evaluation.", True)
                    st.warning("Note: Thyroid conditions require blood tests for accurate diagnosis.")
                else:
                    show_result("The model indicates no significant signs of hypo-thyroidism based on the provided information.", False)
                st.balloons()
        
        st.markdown('</div>', unsafe_allow_html=True)

# Footer with disclaimer
st.markdown("""
<div style="background-color: rgba(0, 0, 0, 0.7); padding: 20px; border-radius: 10px; margin-top: 30px;">
    <p style="color: white; text-align: center;"><strong>Disclaimer:</strong> This application provides predictive assessments only and should not be used as a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of your physician or other qualified health provider with any questions you may have regarding a medical condition.</p>
    <p style="color: white; text-align: center;">&copy; 2023 Sandhya. All rights reserved.</p>
</div>
""", unsafe_allow_html=True)