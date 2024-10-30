import streamlit as st
import numpy as np


with st.form("Matrix calculator"):
    st.title("Matrix calculator")
    st.text("Input each item seperate by space, each row by ;")
    m1 = st.text_area("Input 1st matrix", placeholder="1 2 3;\n1 2 3;\n1 2 3")
    operation = st.selectbox("Chose operation", ("Plus +", "Minus -", "Multiply *"))
    m2 = st.text_area("Input 2st matrix", placeholder="1 2 3;\n1 2 3;\n1 2 3")
    submit_button = st.form_submit_button("submit")

    if submit_button:
        col1, col2, col3 = st.columns(3)
        # st.write("mat1 " + operation + " mat2")
        if operation == "Plus +":
            mat1 = np.matrix(m1)
            mat2 = np.matrix(m2)
            if mat1.size != mat2.size:
                st.warning("not same size")
                res = "undefined"
            else:
                res = mat1 + mat2

        if operation == "Minus -":
            mat1 = np.matrix(m1)
            mat2 = np.matrix(m2)
            if mat1.size != mat2.size:
                st.warning("not same size")
                res = "undefined"
            else:
                res = mat1 - mat2

        if operation == "Multiply *":
            mat1 = np.matrix(m1)
            mat2 = np.matrix(m2)
            try:
                res = mat1 * mat2
            except ValueError as e:
                st.warning(e)
                pass

        # output
        with col1:
            st.write("Matrix 1")
            st.write(mat1)
        with col2:
            st.write("Matrix 2")
            st.write(mat2)
        with col3:
            st.write("Result: ")
            st.write(res)
