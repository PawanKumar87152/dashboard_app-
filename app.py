import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 Simple Dashboard Generator (Matplotlib)")

# File upload
file = st.file_uploader("Upload CSV or Excel file", type=["csv", "xlsx"])

if file is not None:

    # Read file
    if file.name.endswith("csv"):
        df = pd.read_csv(file)
    else:
        df = pd.read_excel(file)

    st.subheader("📄 Data Preview")
    st.dataframe(df)

    # Select column
    column = st.selectbox("Select Column", df.columns)

    chart_type = st.selectbox("Select Chart Type", ["Bar", "Line", "Histogram"])

    data = df[column].dropna()

    # 📊 BAR CHART
    if chart_type == "Bar":
        fig, ax = plt.subplots()
        ax.bar(range(len(data)), data)
        ax.set_title("Bar Chart")
        st.pyplot(fig)

    # 📈 LINE CHART
    elif chart_type == "Line":
        fig, ax = plt.subplots()
        ax.plot(data.values)
        ax.set_title("Line Chart")
        st.pyplot(fig)

    # 📊 HISTOGRAM
    elif chart_type == "Histogram":
        fig, ax = plt.subplots()
        ax.hist(data, bins=10)
        ax.set_title("Histogram")
        st.pyplot(fig)

    # Download data
    st.download_button(
        "Download CSV",
        df.to_csv(index=False),
        "data.csv",
        "text/csv"
    )

else:
    st.info("👆 Please upload a file to generate dashboard")
