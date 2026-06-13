import streamlit as st
import json
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="AURA Dashboard",
    layout="wide"
)

with open("assets/aura.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# --------------------
# Header
# --------------------

st.markdown(
    """
    <div class="main-title">
        AURA
    </div>

    <div class="subtitle">
        LUXURY TREND INTELLIGENCE
    </div>
    """,
    unsafe_allow_html=True
)

# --------------------
# Load Data
# --------------------

trend = {}
analysis = ""

try:
    with open("data/trend_report.json") as f:
        trend = json.load(f)
except:
    pass

try:
    with open("data/analysis_report.txt") as f:
        analysis = f.read()
except:
    pass

# --------------------
# Executive Briefing
# --------------------

st.markdown(
    '<div class="section-title">Executive Briefing</div>',
    unsafe_allow_html=True
)

st.markdown(
    f"""
    <div class="aura-card">
        {analysis if analysis else "Luxury market intelligence will appear here."}
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")

# --------------------
# KPI Row
# --------------------

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Top Trend",
        trend.get("trend", "N/A")
    )

with col2:
    st.metric(
        "Change",
        trend.get("change", "N/A")
    )

with col3:
    st.metric(
        "Status",
        trend.get("status", "N/A")
    )

st.write("")
st.divider()

# --------------------
# Emerging Trends
# --------------------

st.markdown(
    '<div class="section-title">Emerging Signals</div>',
    unsafe_allow_html=True
)

try:

    with open("data/discovered_trends.json") as f:
        discovered = json.load(f)

    df = pd.DataFrame(discovered)

    st.dataframe(
        df,
        use_container_width=True
    )

except:
    st.info("No discovered trends available.")

st.divider()

# --------------------
# Trend History
# --------------------

st.markdown(
    '<div class="section-title">Trend Momentum</div>',
    unsafe_allow_html=True
)

try:

    with open("data/trend_history.json") as f:
        history = json.load(f)

    df = pd.DataFrame(history)

    if len(df) > 0 and "current" in df.columns:

        fig = px.line(
            df,
            x="date",
            y="current",
            markers=True
        )

        fig.update_layout(
            paper_bgcolor="#F8F4EE",
            plot_bgcolor="#FFFFFF",
            font_color="#111111"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

except:
    st.info("Need more historical data.")

st.divider()

# --------------------
# Forecast Section
# --------------------

st.markdown(
    '<div class="section-title">Forecast</div>',
    unsafe_allow_html=True
)

try:

    with open("data/trend_history.json") as f:
        history = json.load(f)

    if len(history) >= 3:

        latest = history[-1]["current"]
        previous = history[-2]["current"]
        older = history[-3]["current"]

        growth1 = latest - previous
        growth2 = previous - older

        avg_growth = (growth1 + growth2) / 2

        forecast = latest + avg_growth

        st.success(
            f"Projected Next Score: {round(forecast,2)}"
        )

    else:
        st.warning(
            "Need at least 3 historical records."
        )

except:
    st.warning(
        "Forecast unavailable."
    )

st.divider()

st.caption(
    "AURA • Luxury Trend Intelligence Platform"
)