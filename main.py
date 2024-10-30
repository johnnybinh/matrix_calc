import streamlit as st

st.title("Matrix Calculator Project")
st.text("Open the sidebar to navigate, or chose one of the option bellow")

option = st.selectbox("Chose page to navigate to", ("Calulator", "RREF", "Inverse"))

if st.button("Go"):
    if option == "Calculator":
        st.switch_page("pages/matrix_calculator.py")
    elif option == "RREF":
        st.switch_page("pages/rref.py")
    elif option == "Inverse":
        st.switch_page("pages/inverse.py")
