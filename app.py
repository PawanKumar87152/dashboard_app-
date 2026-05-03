import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 X-Y Axis Dashboard Generator")

file = st.file_uploader("Upload CSV or Excel file", type=["csv", "xlsx"])

if file is not None:

    # Read file
    if file.name.endswith("csv"):
        df = pd.read_csv(file)
    else:
        df = pd.read_excel(file)

    st.subheader("📄 Data Preview")
    st.dataframe(df)

    # 🟢 Select X and Y columns
    x_col = st.selectbox("Select X-Axis Column", df.columns)
    y_col = st.selectbox("Select Y-Axis Column (Numeric)", df.columns)

    chart_type = st.selectbox("Select Chart Type", ["Bar", "Line"])

    # Clean data
    x = df[x_col]
    y = pd.to_numeric(df[y_col], errors='coerce')

    # Drop null values
    data = pd.DataFrame({x_col: x, y_col: y}).dropna()

    # 📊 BAR CHART
    if chart_type == "Bar":
        fig, ax = plt.subplots()
        ax.bar(data[x_col], data[y_col])
        ax.set_xlabel(x_col)
        ax.set_ylabel(y_col)
        ax.set_title("Bar Chart (X vs Y)")
        plt.xticks(rotation=45)
        st.pyplot(fig)

    # 📈 LINE CHART
    elif chart_type == "Line":
        fig, ax = plt.subplots()
        ax.plot(data[x_col], data[y_col], marker='o')
        ax.set_xlabel(x_col)
        ax.set_ylabel(y_col)
        ax.set_title("Line Chart (X vs Y)")
        plt.xticks(rotation=45)
        st.pyplot(fig)

    # Download
    st.download_button(
        "Download Data",
        df.to_csv(index=False),
        "data.csv",
        "text/csv"
    )

else:
    st.info("👆 Upload file to generate dashboard")
