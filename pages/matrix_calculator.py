import streamlit as st
import numpy as np


st.title("Matrix Calculator")

with st.form("Matrix calculator"):
    st.title("Matrix calculator")
    m1 = st.text_area("Input 1st matrix")
    operation = st.selectbox("Chose operation", ("Plus +", "Minus -", "Multiply *"))
    m2 = st.text_area("Input 2st matrix")
    submit_button = st.form_submit_button("submit")

    if submit_button:
        if operation == "Plus +":
            st.write("plus")
        st.write()
        st.write(m2)
