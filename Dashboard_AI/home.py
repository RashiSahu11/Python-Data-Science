import streamlit as st

st.set_page_config(
    page_title="Automobile Analytics",
    page_icon="🏎️",
    layout="wide"
)

st.markdown("""
<style>

.main {
    background-color: #0B1117;
}

/* HERO */

.hero {
    padding: 80px 20px 60px 20px;
    text-align: center;
}

.hero-title {
    font-size: 58px;
    font-weight: 800;
    color: #FFFFFF;
    margin-bottom: 10px;
}

.hero-title span {
    color: #14B8A6;
}

.hero-subtitle {
    font-size: 20px;
    color: #A7B0B8;
    margin-bottom: 30px;
}

/* CARDS */

.home-card {
    background: #111A22;
    border: 1px solid rgba(20,184,166,0.25);
    border-radius: 18px;
    padding: 28px;
    min-height: 180px;
    transition: 0.3s;
}

.home-card:hover {
    border: 1px solid #14B8A6;
    transform: translateY(-3px);
}

.home-card h3 {
    color: #FFFFFF;
}

.home-card p {
    color: #A7B0B8;
    line-height: 1.6;
}

/* SECTION */

.section-title {
    font-size: 30px;
    font-weight: 700;
    color: #FFFFFF;
    margin-top: 40px;
    margin-bottom: 20px;
}

.highlight {
    color: #14B8A6;
    font-weight: 700;
}

</style>
""", unsafe_allow_html=True)


# HERO

st.markdown("""
<div class="hero">

<div class="hero-title">
AUTOMOBILE <span>ANALYTICS</span> 🏎️
</div>

<div class="hero-subtitle">
Interactive Automobile Data Analysis Dashboard
</div>

</div>
""", unsafe_allow_html=True)


# PROJECT CARDS

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="home-card">
    <h3>📊 Data Analysis</h3>
    <p>
    Explore automobile prices, mileage, fuel types,
    body types and vehicle specifications.
    </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="home-card">
    <h3>🔎 Interactive</h3>
    <p>
    Use filters to explore the automobile dataset
    across different fuel types and years.
    </p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="home-card">
    <h3>📈 Visual Insights</h3>
    <p>
    Understand patterns and relationships through
    interactive Plotly visualizations.
    </p>
    </div>
    """, unsafe_allow_html=True)


# ABOUT PROJECT

st.markdown("""
<div class="section-title">
About the Project
</div>
""", unsafe_allow_html=True)

st.write("""
This project is an interactive automobile data analysis dashboard
developed using Python, Pandas, Plotly and Streamlit.
""")

st.write("""
The dashboard explores important automobile characteristics such as
selling price, mileage, fuel type, engine size, horsepower, body type,
fuel efficiency and accident history.
""")