import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import time


st.header("UNDERSTAND YOUR DATA")


# Create a file uploader widget
uploaded_file = st.file_uploader("UPLOAD YOUR DATA:")


if uploaded_file == None:
    st.write(" ")
    st.warning("UPLOAD ONLY .CSV FILE.")
else:
    #navbar
    rad = st.sidebar.radio("Navigation", ["HOME", "VISUALIZATION: UNIVARIATE", "VISUALIZATION: MULTIVARIATE"])
    

    if rad=="HOME":
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
        
    if rad=="VISUALIZATION: UNIVARIATE":
        st.header("VISUALIZATION CHARTS")
        
        data = pd.read_csv(uploaded_file)
        st.dataframe(data)
        
        st.title("UNIVARIATE ANALYSIS")
        st.write("")
        st.subheader("NUMERICAL COLUMN")
        num_cor = data.select_dtypes(include=["int","float"]).columns        
        
        #HISTOGRAM
        st.write("HISTOGRAM")
        st.write("")
        col1 = st.selectbox("COLUMN 1",num_cor)
        sns.histplot(data[col1], kde=True)
        st.pyplot()
        st.write("")
        st.write("")
        #DISTRIBUTION PLOT
        st.write("DISTPLOT")
        st.write("")
        col2 = st.selectbox("COLUMN 2",num_cor)
        sns.boxplot(data=data[col2])
        st.pyplot()
        
        st.subheader("CATEGORICAL COLUMN")
        num_cor2 = data.select_dtypes(exclude=["int","float"]).columns
        
        #COUNTPLOT
        st.write("COUNTPLOT")
        st.write("")
        col3 = st.selectbox("COLUMN 3", num_cor2)
        sns.countplot(x=data[col3])
        st.pyplot()
        st.write("")
        st.write("")
    
    if rad=="VISUALIZATION: MULTIVARIATE":
        data = pd.read_csv(uploaded_file)
        st.dataframe(data)
        st.title("MULTIVARIATE ANALYSIS")
        st.write("")
        st.subheader("NUMERICAL COLUMN")
        st.write(" ")
        st.write("SCATTERPLOT")
        num_cor3 = data.select_dtypes(include=["int","float"]).columns
        col4 = st.selectbox("COLUMN 4", num_cor3)
        col5 = st.selectbox("COLUMN 5", num_cor3)
        st.write(" ")
        # Create a scatter plot
        plt.scatter(data[col4], data[col5])
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Scatter Plot')
        st.pyplot()
        
        # Create a 3D scatter plot
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        col6 = st.selectbox("COLUMN 6", num_cor3)
        col7 = st.selectbox("COLUMN 7", num_cor3)
        col8 = st.selectbox("COLUMN 8", num_cor3)
        ax.scatter(data[col6], data[col7], data[col8])
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_title('3D Scatter Plot')
        st.pyplot(fig)
        
  



        