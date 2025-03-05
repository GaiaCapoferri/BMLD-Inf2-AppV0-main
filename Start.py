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
if st.button("Gehe zu Unterseite A"):
    st.switch_page("1_Unterseite A")

if st.button("Gehe zu Unterseite B"):
    st.switch_page("2_Unterseite B")
