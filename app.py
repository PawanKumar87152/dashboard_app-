import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 Dashboard Generator")

# STEP 1: File upload
file = st.file_uploader("Upload CSV or Excel file", type=["csv", "xlsx"])

# STEP 2: Check file uploaded or not
if file is not None:

    # Read file
    if file.name.endswith("csv"):
        df = pd.read_csv(file)
    else:
        df = pd.read_excel(file)

    st.success("File uploaded successfully!")

    # Show data
    st.dataframe(df)

    # Select column
    column = st.selectbox("Select Column", df.columns)

    # Chart type
    chart = st.selectbox("Chart Type", ["Bar", "Line", "Pie"])

    # BAR
    if chart == "Bar":
        st.plotly_chart(px.bar(df, y=column))

    # LINE
    elif chart == "Line":
        st.plotly_chart(px.line(df, y=column))

    # PIE
    else:
        st.plotly_chart(px.pie(df, names=df.index, values=column))

# STEP 3: If no file uploaded
else:
    st.info("👆 Please upload a file to generate dashboard")