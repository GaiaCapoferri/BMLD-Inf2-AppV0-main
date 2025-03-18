# ====== Start Login Block ======
from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py') 
# ====== End Login Block ======

import streamlit as st
from functions.bmi_calculator import calculate_bmi
from utils.data_manager import DataManager

st.title("BMI-Rechner")

st.write("Dieser Rechner berechnet den BMI einer Person und bestimmt anhand einer Tabelle, ob die Person normalgewichtig ist oder nicht.")

# Formular für die BMI-Berechnung
with st.form(key='bmi_form'):
    height = st.slider("Größe in Metern:", min_value=0.0, max_value=2.5, value=1.75, step=0.01)
    weight = st.slider("Gewicht in Kilogramm:", min_value=0.0, max_value=200.0, value=70.0, step=0.1)
    
    submit_button = st.form_submit_button("BMI berechnen")

# Verarbeitung nach Absenden des Formulars
if submit_button:
    result = calculate_bmi(height, weight)
    st.write(f'Ihr BMI ist: {result["bmi"]}')
    st.write(f'Berechnet am: {result["timestamp"].strftime("%d.%m.%Y %H:%M:%S")}')
    st.write(f'Kategorie: {result["category"]}')

    # update data in session state and save to persistent storage
    DataManager().append_record(session_state_key='data_df', record_dict=result)  
