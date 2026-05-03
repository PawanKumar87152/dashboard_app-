import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Power BI Style Dashboard", layout="wide")

st.title("📊 Power BI Style Dashboard (Python)")

# Upload file
file = st.file_uploader("Upload CSV or Excel file", type=["csv", "xlsx"])

if file is not None:

    # Read file
    if file.name.endswith("csv"):
        df = pd.read_csv(file)
    else:
        df = pd.read_excel(file)

    # ---------------- KPI SECTION ----------------
    st.subheader("📌 Key Metrics")

    col1, col2, col3 = st.columns(3)

    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns

    if len(numeric_cols) > 0:
        first_num = numeric_cols[0]

        col1.metric("Total Rows", len(df))
        col2.metric("Columns", len(df.columns))
        col3.metric(f"Sum ({first_num})", df[first_num].sum())

    st.divider()

    # ---------------- DATA PREVIEW ----------------
    st.subheader("📄 Data Preview")
    st.dataframe(df)

    st.divider()

    # ---------------- FILTERS ----------------
    st.subheader("🎛 Filters")

    col_a, col_b = st.columns(2)

    x_col = col_a.selectbox("Select X-Axis", df.columns)
    y_col = col_b.selectbox("Select Y-Axis (Numeric)", df.columns)

    chart_type = st.selectbox("Select Chart Type", ["Bar", "Line"])

    # Clean data
    data = df[[x_col, y_col]].dropna()
    data[y_col] = pd.to_numeric(data[y_col], errors='coerce')
    data = data.dropna()

    st.divider()

    # ---------------- CHART SECTION ----------------
    st.subheader("📊 Visualization")

    fig, ax = plt.subplots()

    if chart_type == "Bar":
        ax.bar(data[x_col], data[y_col], color="steelblue")
        ax.set_title("Bar Chart")

    elif chart_type == "Line":
        ax.plot(data[x_col], data[y_col], marker="o", color="green")
        ax.set_title("Line Chart")

    ax.set_xlabel(x_col)
    ax.set_ylabel(y_col)
    plt.xticks(rotation=45)

    st.pyplot(fig)

    # ---------------- DOWNLOAD ----------------
    st.download_button(
        "⬇ Download Data",
        df.to_csv(index=False),
        "dashboard_data.csv",
        "text/csv"
    )

else:
    st.info("👆 Upload file to generate Power BI style dashboard")
