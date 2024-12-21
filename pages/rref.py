import streamlit as st
import numpy as np
import pandas as pd
from sympy import Matrix

st.title("RREF Calculator")

matrix_input = st.text_area("Enter your matrix (rows separated by newlines, columns by spaces):")
submit = st.button("Submit")

if submit and matrix_input:
    matrix = [list(map(float, row.split())) for row in matrix_input.split('\n') if row]
    
    np.set_printoptions(precision=3, suppress=True)

    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.write("Your matrix is:")
        st.write(np.matrix(matrix))
    
    with col2:
        st.write("Your matrix in REF")
        ref_matrix = Matrix(matrix).echelon_form()
        st.write(pd.DataFrame(np.array(ref_matrix).astype(float)))
    
    
    with col3:
        st.write("Your matrix in RREF")
        rref_matrix = Matrix(matrix).rref()[0]
        st.write(pd.DataFrame(np.array(ref_matrix).astype(float)))
    