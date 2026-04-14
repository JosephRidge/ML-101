# Loading Libraries
import pandas as pd 
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st 

# Load the data 
df = pd.read_csv("data/Smartphone_Usage_And_Addiction_Analysis_7500_Rows.csv")


#  perform data understanding
def  glimpseOfData():
    st.markdown("##### First 5 rows of the data")
    st.table(df.head())

def dimensions():
    # dimensions
    records, features = df.shape
    output = f"The data set has {records} records and {features} features" 
    col1, col2  = st.columns(2)
    with col1:
        st.header("No.Of recorded data")
        st.subheader(records)

    with col2:
        st.header("No. Of Attributes")
        st.subheader(features)

def descriptiveStatNumerical():
    # st.table(df.describe())
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.badge("Average Age")
        st.subheader(f"{df['age'].mean():.2f} yrs")
    with col2:
        st.badge("Average Screen time(hrs)")
        st.subheader(f"{df['daily_screen_time_hours'].mean():.2f} Hours")
    with col3:
        st.badge("Avg time on Social Media")
        st.subheader(f"{df['social_media_hours'].mean():.2f} Hours")
    with col4:
        st.badge("Avg Gaming hours")
        st.subheader(f"{df['gaming_hours'].mean():.2f} Hours")

    st.divider()
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.badge("Average Work/Study(hrs)")
        st.subheader(f"{df['work_study_hours'].mean():.2f} yrs")
    with col2:
        st.badge("Average Sleep(hrs)")
        st.subheader(f"{df['sleep_hours'].mean():.2f} Hours")
    with col3:
        st.badge("Avg notifications per day")
        st.subheader(f"{df['notifications_per_day'].mean():.2f} Hours")
    with col4:
        st.badge("Avg app opens per day")
        st.subheader(f"{df['app_opens_per_day'].mean():.2f} Hours")



def aboutSection():
    st.subheader("About Project and Data")
    glimpseOfData()
    st.markdown("""
    *About Dataset*
        This dataset contains detailed information about smartphone usage patterns and addiction indicators collected from 7,500 individuals. It includes variables such as daily screen time, number of app opens, time spent on social media, sleep duration, productivity levels, and frequency of phone checking. The dataset may also include demographic attributes like age, gender, and occupation, allowing for deeper analysis of how different groups interact with smartphones. Overall, the data provides a structured view of user behavior related to mobile device usage.

    *Source:*
        [Data source](https://www.kaggle.com/datasets/jimarahman/smartphone-usage-and-addiction-analysis-dataset)
    
    """)

# INTERFACE

def main():
    st.set_page_config(layout='wide')
    st.title("Smartphone Usage and Addiction Analysis Dataset")
    st.divider()
    st.caption("Summary of the analysis")
    dimensions()
    descriptiveStatNumerical()
    st.divider()
    aboutSection()


if __name__ == '__main__':
    main()
