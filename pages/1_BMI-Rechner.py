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

# Zwei Spalten für Farbauswahl und Tabelle
col1, col2 = st.columns([1, 1])

with col1:
    underweight_color = st.color_picker("Farbe für Untergewicht:", "#ff020f")
    normalweight_color = st.color_picker("Farbe für Normalgewicht:", "#37ff2d")
    overweight_color = st.color_picker("Farbe für Übergewicht:", "#ff020f")

with col2:
    st.write("### BMI-Werte und Gewichtskategorien")
    table_html = f"""
    <table>
        <tr><th>Kategorie</th><th>BMI-Bereich</th></tr>
        <tr style='background-color: {underweight_color};'><td>Untergewicht</td><td>< 18.5</td></tr>
        <tr style='background-color: {normalweight_color};'><td>Normalgewicht</td><td>18.5 - 24.9</td></tr>
        <tr style='background-color: {overweight_color};'><td>Übergewicht</td><td>25 - 29.9</td></tr>
        <tr style='background-color: {overweight_color};'><td>Adipositas</td><td>>= 30</td></tr>
    </table>
    """
    st.markdown(table_html, unsafe_allow_html=True)


if st.button("Gehe zu Startseite"):
    st.switch_page("Start.py")
