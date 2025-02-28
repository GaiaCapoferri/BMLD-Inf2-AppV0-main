import streamlit as st

st.title("BMI-Rechner")

st.write("Dieser Rechner berechnet den BMI einer Person und bestimmt anhand einer Tabelle, ob die Person normalgewichtig ist oder nicht.")

height = st.number_input("Geben Sie Ihre Größe in Metern ein:", min_value=0.0, format="%.2f", step=0.01)

weight = st.number_input("Geben Sie Ihr Gewicht in Kilogramm ein:", min_value=0.0, format="%.1f", step=0.1)

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