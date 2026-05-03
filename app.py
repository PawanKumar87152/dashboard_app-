import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="PRO BI Dashboard", layout="wide")

st.title("📊 PRO Power BI Style Dashboard (Python)")

# ---------------- UPLOAD ----------------
file = st.file_uploader("Upload CSV or Excel file", type=["csv", "xlsx"])

if file is not None:

    # Read file
    if file.name.endswith("csv"):
        df = pd.read_csv(file)
    else:
        df = pd.read_excel(file)

    # ---------------- SIDEBAR FILTER ----------------
    st.sidebar.header("🎛 Filters")

    columns = df.columns.tolist()

    x_col = st.sidebar.selectbox("Select X-Axis", columns)
    y_col = st.sidebar.selectbox("Select Y-Axis (Numeric)", columns)

    chart_type = st.sidebar.selectbox("Chart Type", ["Bar", "Line"])

    # Category filter (if exists)
    cat_col = st.sidebar.selectbox("Filter Column (Optional)", ["None"] + columns)

    if cat_col != "None":
        selected_value = st.sidebar.multiselect(
            "Select Values",
            df[cat_col].dropna().unique()
        )
        if selected_value:
            df = df[df[cat_col].isin(selected_value)]

    # ---------------- KPI SECTION ----------------
    st.subheader("📌 Key Performance Indicators")

    col1, col2, col3 = st.columns(3)

    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns

    if len(numeric_cols) > 0:
        col1.metric("Rows", len(df))
        col2.metric("Columns", len(df.columns))
        col3.metric("Total (First Numeric)", df[numeric_cols[0]].sum())

    st.divider()

    # ---------------- DATA ----------------
    st.subheader("📄 Data Preview")
    st.dataframe(df)

    st.divider()

    # ---------------- CHART ----------------
    st.subheader("📊 Visualization")

    data = df[[x_col, y_col]].dropna()
    data[y_col] = pd.to_numeric(data[y_col], errors='coerce')
    data = data.dropna()

    fig, ax = plt.subplots()

    if chart_type == "Bar":
        ax.bar(data[x_col], data[y_col], color="#1f77b4")
        ax.set_title("Bar Chart")

    else:
        ax.plot(data[x_col], data[y_col], marker="o", color="green")
        ax.set_title("Line Chart")

    ax.set_xlabel(x_col)
    ax.set_ylabel(y_col)
    plt.xticks(rotation=45)

    st.pyplot(fig)

    # ---------------- INSIGHTS ----------------
    st.subheader("🧠 Auto Insights")

    st.info(f"""
    📌 Total Records: {len(df)}  
    📌 Columns: {len(df.columns)}  
    📌 Max Value in {y_col}: {df[y_col].max()}  
    📌 Min Value in {y_col}: {df[y_col].min()}  
    📌 Average: {df[y_col].mean()}
    """)

    # ---------------- DOWNLOAD ----------------
    st.download_button(
        "⬇ Download Clean Data",
        df.to_csv(index=False),
        "pro_dashboard.csv",
        "text/csv"
    )

else:
    st.info("👆 Upload file to generate PRO dashboard")
