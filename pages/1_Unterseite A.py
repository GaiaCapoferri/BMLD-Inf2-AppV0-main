import streamlit as st

st.title("BMI-Rechner")

st.write("Dieser Rechner berechnet den BMI einer Person und bestimmt anhand einer Tabelle, ob die Person normalgewichtig ist oder nicht.")

# Eingabe der Größe
height = st.slider("Größe in Metern:", min_value=0.0, max_value=2.5, value=1.75, step=0.01)

# Eingabe des Gewichts
weight = st.slider("Gewicht in Kilogramm:", min_value=0.0, max_value=200.0, value=70.0, step=0.1)

# Farben für die Gewichtskategorien auswählen
underweight_color = st.color_picker("Farbe für Untergewicht:", "#ff020f")
normalweight_color = st.color_picker("Farbe für Normalgewicht:", "#37ff2d")
overweight_color = st.color_picker("Farbe für Übergewicht:", "#ff020f")

# Berechnung des BMI
if st.button("BMI berechnen"):
    if height > 0 and weight > 0:
        bmi = weight / (height ** 2)
        st.write(f"Ihr BMI beträgt: {bmi:.2f}")
        
        # Bestimmung des Gewichtsstatus
        if bmi < 18.5:
            st.write("Sie sind untergewichtig.")
        elif 18.5 <= bmi < 24.9:
            st.write("Sie haben ein normales Gewicht.")
        elif 25 <= bmi < 29.9:
            st.write("Sie sind übergewichtig.")
        else:
            st.write("Sie sind fettleibig.")
    else:
        st.write("Bitte geben Sie eine gültige Größe und ein gültiges Gewicht ein.")

# Tabelle mit BMI-Werten und Gewichtskategorien
st.write("### BMI-Werte und Gewichtskategorien")
bmi_data = {
    "Kategorie": ["Untergewicht", "Normalgewicht", "Übergewicht", "Adipositas"],
    "BMI-Bereich": ["< 18.5", "18.5 - 24.9", "25 - 29.9", ">= 30"]
}

bmi_table = st.table(bmi_data)

# Farbliche Hervorhebung der Kategorien
st.markdown(f"""
<style>
    .stTable tbody tr:nth-child(1) {{background-color: {underweight_color};}}
    .stTable tbody tr:nth-child(2) {{background-color: {normalweight_color};}}
    .stTable tbody tr:nth-child(3) {{background-color: {overweight_color};}}
    .stTable tbody tr:nth-child(4) {{background-color: {overweight_color};}}
</style>
""", unsafe_allow_html=True)