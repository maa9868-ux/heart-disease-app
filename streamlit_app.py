## Step 00 - Import of the packages

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import numpy as np


st.set_page_config(
    page_title="Heart Disease Dashboard 🫀",
    layout="centered",
    page_icon="🫀",
)


## Step 01 - Setup
st.sidebar.title("CDC - Heart Disease Study 🫀")
page = st.sidebar.selectbox(
    "Select Page",
    ["Introduction 📘", "Visualization 📊", "Automated Report 📑"]
)


#st.video("video.mp4")

st.image("heart.png")

st.write("   ")
st.write("   ")
st.write("   ")

df = pd.read_csv("heart_2020.csv")


## Step 02 - Load dataset
if page == "Introduction 📘":

    st.subheader("01 Introduction 📘")

    st.markdown("##### Data Preview")
    rows = st.slider("Select a number of rows to display", 5, 20, 5)
    st.dataframe(df.head(rows))

    st.markdown("##### Missing values")
    missing = df.isnull().sum()
    st.write(missing)

    if missing.sum() == 0:
        st.success("✅ No missing values found")
    else:
        st.warning("⚠️ you have missing values")

    st.markdown("##### 📈 Summary Statistics")
    if st.button("Show Describe Table"):
        st.dataframe(df.describe())


elif page == "Visualization 📊":

    ## Step 03 - Data Viz
    st.subheader("02 Data Viz")

    col_x = st.selectbox(
        "Select X-axis variable",
        df.columns,
        index=0
    )

    col_y = st.selectbox(
        "Select Y-axis variable",
        df.select_dtypes(include=np.number).columns,
        index=0
    )

    chart_df = df.groupby(col_x)[col_y].mean()

    tab1, tab2, tab3 = st.tabs(
        ["Bar Chart 📊", "Line Chart 📈", "Correlation Heatmap 🔥"]
    )

    with tab1:
        st.subheader("Bar Chart")
        st.bar_chart(
            chart_df,
            use_container_width=True
        )

    with tab2:
        st.subheader("Line Chart")
        st.line_chart(
            chart_df,
            use_container_width=True
        )

    with tab3:
        st.subheader("Correlation Matrix")

        df_numeric = df.select_dtypes(include=np.number)

        fig_corr, ax_corr = plt.subplots(figsize=(18, 14))

        # create the plot, in this case with seaborn
        sns.heatmap(
            df_numeric.corr(),
            annot=True,
            fmt=".2f",
            cmap="coolwarm"
        )

        ## render the plot in streamlit
        st.pyplot(fig_corr)


elif page == "Automated Report 📑":

    st.subheader("03 Automated Report 📑")
    st.write("Automated report will be added next.")