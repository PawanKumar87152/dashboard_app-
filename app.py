import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

st.title("📊 CRM Style Dashboard")

# ---------------- SAMPLE DATA (replace with upload later) ----------------
df = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Tickets": [30, 50, 40, 60, 80, 70],
    "Resolved": [20, 40, 30, 50, 65, 60]
})

# ---------------- SIDEBAR ----------------
st.sidebar.title("📌 Menu")
page = st.sidebar.radio("Go to", ["Dashboard", "Analytics"])

# ---------------- DASHBOARD ----------------
if page == "Dashboard":

    st.subheader("📊 KPI Overview")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Avg First Reply", "30 min", "▲ 2%")
    col2.metric("Avg Resolve Time", "22 min", "▼ 5%")
    col3.metric("Messages", "1.2K", "▲ 20%")
    col4.metric("Emails", "900", "▲ 33%")

    st.divider()

    # ---------------- CHARTS ----------------
    col1, col2 = st.columns([2,1])

    with col1:
        fig = px.line(df, x="Month", y=["Tickets", "Resolved"], title="Tickets Trend")
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        fig2 = px.pie(df, names="Month", values="Tickets", title="Tickets Share")
        st.plotly_chart(fig2, use_container_width=True)

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        fig3 = px.bar(df, x="Month", y="Tickets", title="Tickets per Month")
        st.plotly_chart(fig3, use_container_width=True)

    with col2:
        fig4 = px.line(df, x="Month", y="Resolved", title="Resolved Trend")
        st.plotly_chart(fig4, use_container_width=True)

# ---------------- ANALYTICS PAGE ----------------
elif page == "Analytics":

    st.subheader("📈 Detailed Analytics")

    st.write(df.describe())

    fig = px.bar(df, x="Month", y="Tickets")
    st.plotly_chart(fig, use_container_width=True)
