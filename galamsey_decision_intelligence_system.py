# Ghana Beyond Galamsey Project

# ================================
# IMPORT LIBRARIES
# ================================
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# ================================
# PAGE CONFIGURATION
# ================================
st.set_page_config(
    page_title="Galamsey Decision Intelligence System",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ================================
# DATA LOADING
# ================================
data = {
    "River": [
        "River Oda", "River Birim", "River Pra Twifo", "River Ankobra", "River Subri",
        "River Anuru", "River Offin", "River Ashrey", "River Butre", "River Tano",
        "River Pra Daboase", "Galamsey Pit"
    ],
    "Arsenic (As)": [0.364, 0.372, 0.305, 0.221, 0, 0.444, 0.216, 0.367, 0.341, 0.346, 0.288, 0.291],
    "Cadmium (Cd)": [0, 0, 0, 0, 0.013, 0, 0, 0, 0, 0, 0, 0],
    "Chromium (Cr)": [0.103, 0.037, 0.115, 0.293, 1.607, 0.15, 0.411, 0.096, 0.147, 0.187, 0.186, 0.021],
    "Lead (Pb)": [0.073, 0.065, 0.133, 0.119, 0.208, 0.062, 0.148, 0.079, 0.066, 0.086, 0.057, 0.051],
    "pH": [5.93, 5.96, 5.65, 5.7, 5.25, 5.64, 6.46, 6.12, 5.67, 5.69, 5.62, 3.21]
}
df = pd.DataFrame(data)

# ================================
# APP TITLE
# ================================
st.title("\U0001F30A The Galamsey Decision Intelligence System")
st.markdown("---")

# Overview stats
st.header("Water Pollution Snapshot")
col1, col2, col3 = st.columns(3)
col1.metric("Most Polluted River (Cr)", "River Subri", "1.607 mg/L")
col2.metric("Highest Arsenic Level", "River Anuru", "0.444 mg/L")
col3.metric("Lowest pH", "Galamsey Pit", "pH 3.21")

# ================================
# TABS LAYOUT
# ================================
tab1, tab2, tab3 = st.tabs(["\U0001F4CA Heavy Metal Levels", "\U0001F321 pH Analysis", "\U0001F4A1 Recommendations"])

# ================================
# TAB 1 - Heavy Metal Levels
# ================================
with tab1:
    st.header("Heavy Metal Concentrations by River")
    selected_metals = st.multiselect("Select metals to visualize:", df.columns[1:5], default=["Arsenic (As)", "Chromium (Cr)", "Lead (Pb)"])
    
    df_melted = df.melt(id_vars="River", value_vars=selected_metals, var_name="Metal", value_name="Concentration")

    with st.spinner('Generating metal concentration plots...'):
        fig, ax = plt.subplots(figsize=(12, 5))
        sns.barplot(data=df_melted, x="River", y="Concentration", hue="Metal", ax=ax)
        plt.xticks(rotation=45)
        plt.title("Heavy Metal Levels in Rivers")
        st.pyplot(fig)

# ================================
# TAB 2 - pH Analysis
# ================================
with tab2:
    st.header("pH Levels Across Rivers")
    with st.spinner('Plotting pH levels...'):
        fig2, ax2 = plt.subplots(figsize=(10, 4))
        sns.lineplot(data=df, x="River", y="pH", marker="o", ax=ax2)
        plt.xticks(rotation=45)
        plt.title("pH Levels of River Water Samples")
        st.pyplot(fig2)

# ================================
# TAB 3 - Recommendations
# ================================
with tab3:
    st.header("Prescriptive Insight")
    selected_river = st.selectbox("Choose a river for insights:", df["River"])
    selected_row = df[df["River"] == selected_river].iloc[0]

    if selected_row["Chromium (Cr)"] > 0.5:
        st.error(f"\u26A0\ufe0f High Chromium detected in {selected_river} — Immediate remediation recommended!")
    else:
        st.success(f"\u2705 Chromium levels are within safe limits in {selected_river}.")

    if selected_row["pH"] < 5.5:
        st.error(f"\u26A1 Acidic conditions detected in {selected_river} — Potential heavy metal leaching.")
    else:
        st.success(f"\u2705 pH level appears acceptable for {selected_river}.")

    st.markdown("\n---\n")
    st.markdown("**System Intelligence Powered by:** Real-Time IoT Sensors | Machine Learning | Environmental Forecasting")

# ================================
# FOOTER
# ================================
st.markdown("---")
st.caption("\u00A9 2025 Beyond Galamsey Project | Powered by Aqualinqs Digital Agency")
