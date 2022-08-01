import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image

# Core Pkgs
import streamlit as st 

# EDA Pkgs
import pandas as pd 
import numpy as np 


# Data Viz Pkg
import matplotlib.pyplot as plt 
import matplotlib
matplotlib.use("Agg")
import seaborn as sns 
import itables 


import base64

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
        background-size: cover;
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
    
add_bg_from_local("images/pic1.jpg") 


#def local_css(file_name):
#     with open(file_name) as f:
#         st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# def remote_css(url):
#     st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)    

# def icon(icon_name):
#     st.markdown(f'<i class="material-icons">{icon_name}</i>', unsafe_allow_html=True)
#local_css("style.css")


#st.set_page_config(page_title='Free plot and insight for Excel, txt, csv ')
st.header('Free plot and insight for Excel, txt, csv')
st.subheader('No need of knowledge of coding, just drag and drop! ')
st.subheader('Do you have large data to process ?')



uploaded_file = st.file_uploader("Upload a Dataset", type=["csv", "txt", "xlsx"])




if uploaded_file is not None:
        sheet_name = uploaded_file.name
   
        df = pd.read_excel(uploaded_file)

        df.dropna(inplace=True)
        
        st.dataframe(df.head())

        if st.checkbox("Show Shape"):
                st.write(df.shape)

        if st.checkbox("Show Columns"):
                all_columns = df.columns.to_list()
                st.write(all_columns)
                
        if st.checkbox("Show Columns types "):
                st.write(df.dtypes(str))

        if st.checkbox("Summary"):
                st.write(df.describe())

        if st.checkbox("Show Selected Columns"):
                selected_columns = st.multiselect("Select Columns",all_columns)
                new_df = df[selected_columns]
                st.dataframe(new_df)

        if st.checkbox("Show Value Counts"):
                for column in df.columns:
                        st.write(df[column].value_counts())
                        bar_chart = px.histogram(df, x=column, barmode='group')
                        st.plotly_chart(bar_chart)

        if st.checkbox("Correlation Plot(Matplotlib)"):
                plt.matshow(df.corr())
                st.pyplot()

        if st.checkbox("Correlation Plot(Seaborn)"):
                st.write(sns.heatmap(df.corr(),annot=True))
                st.pyplot()


        if st.checkbox("Pie Plot"):
                all_columns = df.columns.to_list()
                column_to_plot = st.selectbox("Select 1 Column",all_columns)
                pie_plot = df[column_to_plot].value_counts().plot.pie(autopct="%1.1f%%")
                st.write(pie_plot)
                st.pyplot()