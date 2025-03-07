import streamlit as st

st.title("Übungen")

st.write("Diese Seite ist eine Unterseite der Startseite.")
st.write("Übung Vorlesung 3.")

# Zähler für die Anzahl der Klicks
if 'count' not in st.session_state:
    st.session_state.count = 0

# Funktion zum Erhöhen des Zählers
def increment_counter():
    st.session_state.count += 1

# Knopf zum Erhöhen des Zählers
if st.button("Klick mich!"):
    increment_counter()

# Anzeige der Anzahl der Klicks
st.write(f"Der Knopf wurde {st.session_state.count} mal gedrückt.")

# Knopf zum Wechseln zur Startseite
if st.button("Gehe zu Startseite"):
    st.switch_page("Start.py")