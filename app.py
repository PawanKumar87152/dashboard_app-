import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Ultra Pro Dashboard", layout="wide")

st.title("📊 ULTRA PRO Power BI Style Dashboard")

# ---------------- UPLOAD ----------------
file = st.file_uploader("Upload CSV or Excel file", type=["csv", "xlsx"])

if file is not None:

    # Read data
    if file.name.endswith("csv"):
        df = pd.read_csv(file)
    else:
        df = pd.read_excel(file)

    # ---------------- SIDEBAR NAVIGATION ----------------
    st.sidebar.title("📌 Navigation")

    page = st.sidebar.radio(
        "Go to",
        ["📊 Overview", "📈 Trend Analysis", "🔥 Correlation", "🧠 Insights"]
    )

    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns

    # ---------------- PAGE 1: OVERVIEW ----------------
    if page == "📊 Overview":

        st.subheader("📊 KPI Dashboard")

        col1, col2, col3 = st.columns(3)

        col1.metric("Rows", len(df))
        col2.metric("Columns", len(df.columns))
        col3.metric("Numeric Columns", len(numeric_cols))

        st.divider()

        st.subheader("📄 Data Preview")
        st.dataframe(df)

    # ---------------- PAGE 2: TREND ----------------
    elif page == "📈 Trend Analysis":

        st.subheader("📈 Trend Analysis")

        x_col = st.selectbox("Select X-Axis", df.columns)
        y_col = st.selectbox("Select Y-Axis", df.columns)

        data = df[[x_col, y_col]].dropna()
        data[y_col] = pd.to_numeric(data[y_col], errors='coerce')
        data = data.dropna()

        fig, ax = plt.subplots()
        ax.plot(data[x_col], data[y_col], marker="o", color="green")
        ax.set_title("Trend Analysis")
        plt.xticks(rotation=45)

        st.pyplot(fig)

    # ---------------- PAGE 3: CORRELATION ----------------
    elif page == "🔥 Correlation":

        st.subheader("🔥 Correlation Heatmap")

        if len(numeric_cols) > 1:
            fig, ax = plt.subplots()
            sns.heatmap(df[numeric_cols].corr(), annot=True, cmap="coolwarm", ax=ax)
            st.pyplot(fig)
        else:
            st.warning("Not enough numeric columns for correlation")

    # ---------------- PAGE 4: INSIGHTS ----------------
    elif page == "🧠 Insights":

        st.subheader("🧠 Auto Insights")

        st.info(f"""
        📌 Total Rows: {len(df)}  
        📌 Total Columns: {len(df.columns)}  
        📌 Missing Values: {df.isnull().sum().sum()}  
        📌 Duplicate Rows: {df.duplicated().sum()}  
        """)

        if len(numeric_cols) > 0:
            col = numeric_cols[0]

            st.success(f"""
            📊 {col} Stats:
            - Max: {df[col].max()}  
            - Min: {df[col].min()}  
            - Avg: {df[col].mean()}  
            """)

    # ---------------- DOWNLOAD ----------------
    st.divider()

    st.download_button(
        "⬇ Download Report",
        df.to_csv(index=False),
        "ultra_pro_dashboard.csv",
        "text/csv"
    )

else:
    st.info("👆 Upload file to start Ultra Pro Dashboard")
