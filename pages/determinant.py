import streamlit as st
import numpy as np
import pandas as pd
from sympy import Matrix

st.title("Determinant Calculator")

matrix_input = st.text_area("Enter your matrix (rows separated by newlines, columns by spaces):")
submit = st.button("Submit")

if submit and matrix_input:
  matrix = [list(map(float, row.split())) for row in matrix_input.split('\n') if row]
  st.write("Your matrix is: ")
  st.write(np.matrix(matrix))
  st.write("Determinant: ")
  det = np.linalg.det(matrix)
  st.markdown(f"<h2 style='text-align: center; color: white;'>{det:.3f}</h2>", unsafe_allow_html=True)