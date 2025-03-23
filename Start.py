# ====== Start Init Block ======
# This needs to copied on top of the entry point of the app (Start.py)

import pandas as pd
from utils.data_manager import DataManager
from utils.login_manager import LoginManager

# initialize the data manager
data_manager = DataManager(fs_protocol='webdav', fs_root_folder="BMLD_App_DB")  # switch drive 

# initialize the login manager
login_manager = LoginManager(data_manager)
login_manager.login_register()  # open login/register page

# load the data from the persistent storage into the session state
data_manager.load_user_data(
    session_state_key='data_df', 
    file_name='data.csv', 
    initial_value = pd.DataFrame(), 
    parse_dates = ['timestamp']
    )
# ====== End Init Block ======

import streamlit as st
import pandas as pd

st.title("Meine erste Streamlit App")

# !! WICHTIG: Eure Emails müssen in der App erscheinen!!

# Streamlit über den Text unten direkt in die App - cool!
"""
Diese App wurde von der folgenden Person entwickelt:
- Gaia Capoferri (capofgai@students.zhaw.ch)
"""

st.markdown("Der BMI ist eine Zahl, die als Verhältnis zwischen Gewicht und dem Quadrat der Körpergröße einer Person ausgedrückt wird und als Indikator für das Gesundheitsgewicht dient.")

st.info("Dieser Index wird häufig nur grob verwendet, da er das Geschlecht, den Körperbau und andere Faktoren nicht berücksichtigt. Für eine korrekte Diagnose ist es daher notwendig, einen Spezialisten zu konsultieren, der alle notwendigen Faktoren berücksichtigt.")

# Navigation zu anderen Seiten
if st.button("Gehe zum BMI-Rechner"):
    st.switch_page("pages/1_BMI-Rechner.py")

if st.button("Gehe zum BMI-Daten"):
    st.switch_page("pages/2_BMI-Daten.py")

if st.button("Gehe zum BMI-Grafik"):
    st.switch_page("pages/3_BMI-Grafik.py")