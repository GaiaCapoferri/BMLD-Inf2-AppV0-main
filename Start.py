import streamlit as st
import pandas as pd

st.title("Meine erste Streamlit App")

# !! WICHTIG: Eure Emails müssen in der App erscheinen!!

# Streamlit über den Text unten direkt in die App - cool!
"""
Diese App wurde von folgenden Personen entwickelt:
- Gaia Capoferri (capofgai@students.zhaw.ch)

Diese App ist das leere Gerüst für die App-Entwicklung im Modul Informatik 2 (BMLD/ZHAW)
"""

# Navigation zu anderen Seiten
if st.button("Gehe zum BMI-Rechner"):
    st.switch_page("pages/BMI_Rechner.py")

if st.button("Gehe zu Unterseite B"):
    st.switch_page("pages/2_Unterseite B.py")

if st.button("Gehe zu Unterseite C"):
    st.switch_page("pages/3_Unterseite C.py")