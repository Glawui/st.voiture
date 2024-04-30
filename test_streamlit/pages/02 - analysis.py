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
    page_title="analysis",
    layout="centered",
    initial_sidebar_state="expanded"
)

# menu sidebar
with st.sidebar:
    st.write("You can select a years: ")
    start, end = st.slider("year: ", 1971,1983, (1971,1983))
    st.write("You can select a continents: ")
    with st.popover("Continents: "):
        continents_list = df["continent"].unique()
        continents = st.multiselect("Continents :", continents_list, continents_list)

st.title("Analysis:")
st.write('You can check the dataframe here :')
with st.popover("Dataframe"):
    df_filtered = df[(df["year"] >= start) & (df["year"] <= end)]
    df_filtered_cont = df_filtered["continent"].apply(lambda x:x in continents)
    df_filtered = df_filtered[df_filtered_cont]
    df_filtered

st.header("Scatter Miles per Gallon and car weights")
# Create the scatter plot
viz_scatterplot = sns.scatterplot(data=df_filtered, x='mpg', y='weightlbs', hue="continent")
plt.xlabel('Miles Per Gallon (MPG)')
plt.ylabel('Weight (WT)')
st.pyplot(viz_scatterplot.figure)

st.header("Boxplot Miles per Gallon and cylinders")
plt.figure(figsize=(8, 6))
viz_boxplot = sns.boxplot(data=df_filtered, x='cylinders', y='mpg',hue="continent")
plt.xlabel('Cylinders')
plt.ylabel('Miles Per Gallon (MPG)')
st.pyplot(viz_boxplot.figure)

st.header("Distribution of car horsepower")
plt.figure(figsize=(8, 6))
viz_histplot = sns.histplot(data=df_filtered, x='hp',hue="continent", bins=10, kde=True)
plt.xlabel('Horsepower (HP)')
plt.ylabel('Count')
st.pyplot(viz_histplot.figure)

