import streamlit as st

st.set_page_config(
    page_title="About | Automobile Analytics",
    page_icon="ℹ️",
    layout="wide"
)

st.markdown("""
<style>

.about-title {
    text-align: center;
    font-size: 48px;
    font-weight: 800;
    color: #FFFFFF;
    margin-top: 30px;
}

.about-subtitle {
    text-align: center;
    font-size: 18px;
    color: #A7B0B8;
    margin-bottom: 45px;
}

.about-card {
    background: #111A22;
    border: 1px solid rgba(20,184,166,0.20);
    border-radius: 18px;
    padding: 28px;
    margin-bottom: 20px;
}

.about-card h3 {
    color: #14B8A6;
}

.about-card p {
    color: #D1D5DB;
    line-height: 1.7;
}

.tech-card {
    background: #111A22;
    border: 1px solid rgba(20,184,166,0.20);
    border-radius: 15px;
    padding: 20px;
    text-align: center;
}

.tech-card h3 {
    color: #FFFFFF;
}

.tech-card p {
    color: #A7B0B8;
}

</style>
""", unsafe_allow_html=True)


st.markdown("""
<div class="about-title">
AUTOMOBILE DATA ANALYSIS
</div>

<div class="about-subtitle">
Interactive Automobile Analytics Dashboard
</div>
""", unsafe_allow_html=True)


st.markdown("""
<div class="about-card">

<h3>🎯 Project Objective</h3>

<p>
The objective of this project is to analyse automobile data and
identify patterns related to selling price, mileage, fuel type,
vehicle specifications, body type and accident history through
interactive visualizations.
</p>

</div>
""", unsafe_allow_html=True)


st.markdown("""
<div class="about-card">

<h3>📊 Dataset</h3>

<p>
The dataset contains automobile information including make, model,
year, fuel type, transmission, engine size, mileage, horsepower,
torque, owners, accident history, service history, body type,
fuel efficiency, location and selling price.
</p>

</div>
""", unsafe_allow_html=True)


st.markdown("""
<div class="about-card">

<h3>🔎 Analysis Performed</h3>

<p>
The dashboard analyses automobile distribution, selling prices,
price trends, mileage, engine specifications, fuel types,
body types, fuel efficiency and accident history.
</p>

</div>
""", unsafe_allow_html=True)


st.subheader("🛠️ Technologies Used")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="tech-card">
    <h3>🐍 Python</h3>
    <p>Programming & Analysis</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="tech-card">
    <h3>🐼 Pandas</h3>
    <p>Data Manipulation</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="tech-card">
    <h3>📊 Plotly</h3>
    <p>Interactive Visualization</p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="tech-card">
    <h3>⚡ Streamlit</h3>
    <p>Dashboard Development</p>
    </div>
    """, unsafe_allow_html=True)