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
    if height > 0 and weight > 0:
        bmi = weight / (height ** 2)
        st.markdown(f"**Ihr BMI beträgt: {bmi:.2f}**")
        
        if bmi < 18.5:
            st.markdown("**Sie sind untergewichtig.**")
        elif 18.5 <= bmi < 24.9:
            st.markdown("**Sie haben ein normales Gewicht.**")
        elif 25 <= bmi < 29.9:
            st.markdown("**Sie sind übergewichtig.**")
        else:
            st.markdown("**Sie sind fettleibig.**")
    else:
        st.write("Bitte geben Sie eine gültige Größe und ein gültiges Gewicht ein.")

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