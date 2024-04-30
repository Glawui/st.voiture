# les imports
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# le df
link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df = pd.read_csv(link)


# Configuration initiale
st.set_page_config(
    page_title="dataset cars",
    layout="centered",
    initial_sidebar_state="expanded"
)


# la page
st.title('Good morning the wild ! Welcome to my streamlit!')

st.header("I'm studying to be a data analyst and one of my work is to make an analyse on this data frame:")
st.write('https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv')

st.write("let's see an eventutal correlation")



df_num = df.select_dtypes('number')
correlation_matrix = df_num.corr()

# Créer le heatmap annoté
viz_heatmap = plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Heatmap of correlation between cars variables")
st.pyplot(viz_heatmap.figure)

st.write('We can see there is a correlation between "cylinders", "cubicinches", "house power", and "weightbs" ')

st.write('You can now go to the page Analysis on the left bar')