import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 X-Y Dashboard Generator")

# Upload file
file = st.file_uploader("Upload CSV or Excel file", type=["csv", "xlsx"])

if file is not None:

    # Read data
    if file.name.endswith("csv"):
        df = pd.read_csv(file)
    else:
        df = pd.read_excel(file)

    st.subheader("📄 Data Preview")
    st.dataframe(df)

    # Select columns
    x_col = st.selectbox("Select X-Axis Column", df.columns)
    y_col = st.selectbox("Select Y-Axis Column", df.columns)

    chart_type = st.selectbox("Select Chart Type", ["Bar", "Line"])

    # Clean data
    data = df[[x_col, y_col]].dropna()
    data[y_col] = pd.to_numeric(data[y_col], errors='coerce')
    data = data.dropna()

    st.subheader("📊 Generated Chart")

    # 📊 BAR CHART
    if chart_type == "Bar":
        fig, ax = plt.subplots()
        ax.bar(data[x_col], data[y_col], color="skyblue")
        ax.set_xlabel(x_col)
        ax.set_ylabel(y_col)
        ax.set_title(f"{y_col} vs {x_col} (Bar Chart)")
        plt.xticks(rotation=45)
        st.pyplot(fig)

    # 📈 LINE CHART
    elif chart_type == "Line":
        fig, ax = plt.subplots()
        ax.plot(data[x_col], data[y_col], marker="o", color="green")
        ax.set_xlabel(x_col)
        ax.set_ylabel(y_col)
        ax.set_title(f"{y_col} vs {x_col} (Line Chart)")
        plt.xticks(rotation=45)
        st.pyplot(fig)

    st.success("✅ Chart generated successfully!")

else:
    st.info("👆 Please upload a file first")
