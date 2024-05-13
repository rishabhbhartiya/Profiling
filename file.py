import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.header("UNDERSTAND YOUR DATA")


# Create a file uploader widget
uploaded_file = st.file_uploader("UPLOAD YOUR DATA:")


if uploaded_file == None:
    st.write(" ")
    st.warning("UPLOAD ONLY .CSV FILE.")
else:
    data = pd.read_csv(uploaded_file)

    st.dataframe(data)
    
    st.write("\n")
    st.write("\n")

    st.title("Understanding your Data:")
    
    st.write("\n")
    st.write("\n")

    st.subheader("How big is the data?")
    st.write(data.shape)
    
    st.write("\n")

    st.subheader("How does the data look like?")
    st.write(data.head(5))
    
    st.write("\n")

    st.subheader("What is the data type of columns?")
    st.write(data.dtypes)
    
    st.write("\n")

    st.subheader("Are there any missing values?")
    st.write(data.isnull().sum())
    
    st.write("\n")

    st.subheader("How does the data look mathematically?")
    st.write(data.describe())
    
    st.write("\n")

    st.subheader("Are there any duplicate values?")
    st.write(data.duplicated().sum())

    st.write("\n")

    st.subheader("How is the correlation between the columns?")
    st.text("This is the numerical columns for the correlation.")
    num_cor = data.select_dtypes(include=["int","float"])
    st.write(num_cor)
    
    st.write("\n")
    
    st.subheader('Correlation: ')
    correlation_matrix = num_cor.corr()
    st.write(correlation_matrix.corr())
    
    st.write("\n")

    st.subheader('Correlation Matrix: ')
    sns.heatmap(correlation_matrix, annot=True)
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()
