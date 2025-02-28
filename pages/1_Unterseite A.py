import streamlit as st

st.title("BMI-Rechner")

st.write("Dieser Rechner berechnet den BMI einer Person und bestimmt anhand einer Tabelle, ob die Person normalgewichtig ist oder nicht.")

# Eingabe der Größe und des Gewichts in einer Tabelle
col1, col2 = st.columns(2)

with col1:
    height = st.slider("Größe in Metern:", min_value=0.0, max_value=2.5, value=1.75, step=0.01)

with col2:
    weight = st.slider("Gewicht in Kilogramm:", min_value=0.0, max_value=200.0, value=70.0, step=0.1)

# Berechnung des BMI
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