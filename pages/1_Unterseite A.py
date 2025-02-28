import streamlit as st

st.title("BMI-Rechner")

st.write("Dieser Rechner berechnet den BMi einer Person und bestimmt anhand einer Tabelle, ob die Person normalgewichtig ist oder nicht.")

height = st.number_input("Geben Sie Ihre Größe in Metern ein:", min_value=0.0, format="%.2f")

weight = st.number_input("Geben Sie Ihr Gewicht in Kilogramm ein:", min_value=0.0, format="%.1f")

if height > 0:
    bmi = weight / (height ** 2)
    st.write(f"Ihr BMI beträgt: {bmi:.2f}")
else:
    st.write("Bitte geben Sie eine gültige Größe ein.")