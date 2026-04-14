# ==============================================================================
# Library
# ==============================================================================

import streamlit as st 
import numpy as np 
import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 

# """
# When building UI we look at two key things: 
# - Elements (What do i show them?)
# - Layout (how do i arrange stuff?)
# """
# approach 1 in laying texts/ data
# """
# # Welcome to Multi-line String classs!
# """

# 3 + 5
# 10  + 20 
# 12 + 12
# 13 + 13
# {
#     "name":"John Doe",
#     "age": 12,
#     "course":"coloring"
# }

#  approach 2
# st.write(" Hello World!")
# st.write("# Hello World!")
# st.write("## Hello World!")
# st.write("### Hello World!")
# st.write("#### Hello World!")
# st.write("##### Hello World!")
# st.write("##### Hello World!")


# column => layout structure 
# col1, col2, col3 = st.columns(3)

# with col1:
#     st.write("# Hello World!")
# with col2:
#     st.write("# Hello World!")
# with col3:
#     st.write("# Hello World!")


# print("=============================================")
# #  Button element
# btn1 = st.button("click me")
# print(f"BUTTON 1: {btn1}")
# btn2 = st.button("click me again")
# print(f"BUTTON 2: {btn2}")
# print("=============================================")


## texts
# print("=============================================")
st.divider()
st.title("Welcome to DSA online")
st.header("This is a simple header!")
st.subheader("This is a simple header!") 
st.markdown("# Hello World!")
st.markdown("## Hello World!")
st.markdown("### Hello World!")
st.markdown("#### Hello World!")
st.markdown("##### Hello World!")
st.markdown("##### Hello World!")
st.caption("Tuesday @2102HRS" )
st.divider()