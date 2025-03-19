# ====== Start Login Block ======
from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py') 
# ====== End Login Block ======

import streamlit as st

st.title('BMI Verlauf')

data_df = st.session_state['data_df']
if data_df.empty:
    st.info('Keine BMI Daten vorhanden. Berechnen Sie Ihren BMI auf der Startseite.')
    st.stop()

# Weight over time using area chart
st.area_chart(data=data_df.set_index('timestamp')['weight'], 
              use_container_width=True)
st.caption('Gewicht über Zeit (kg)')

# Height over time 
st.line_chart(data=data_df.set_index('timestamp')['height'],
              use_container_width=True)
st.caption('Größe über Zeit (m)')

# BMI over time using scatter chart
st.scatter_chart(data=data_df.set_index('timestamp')['bmi'],
                 use_container_width=True)
st.caption('BMI über Zeit')

if st.button("Gehe zu Startseite"):
    st.switch_page("Start.py")
    