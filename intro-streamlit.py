"""
Loading libraries
"""
import streamlit as st 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

# TEXT
st.title("Welcome to DSA 101")
st.header("This is a header!")
st.subheader("This is a sub-header!")
st.markdown("# This is *Markdown*")
st.markdown("## This is *Markdown*")
st.markdown("### This is *Markdown*")
st.markdown("#### This is *Markdown*")
st.markdown("##### This is *Markdown*")
st.markdown("###### This is *Markdown*")
st.caption("DSA 101")
st.divider() 

code_snippet = """
def smile():
    print("I am smiling!")

"""
st.code(code_snippet)
st.divider() 