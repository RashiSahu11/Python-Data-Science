import streamlit as st

# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Digital Payments Intelligence",
    page_icon="💳",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# BURGUNDY UI CSS
# =========================================================

st.markdown("""
<style>

    /* =========================
       MAIN PAGE
    ========================= */

    .stApp {
        background-color: #FAF7F5;
    }

    .block-container {
        max-width: 1400px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    /* =========================
       SIDEBAR
    ========================= */

    section[data-testid="stSidebar"] {
        background-color: #FFFDFC;
        border-right: 1px solid #E7D9D5;
    }

    /* =========================
       HEADINGS
    ========================= */

    h1 {
        color: #5A1725 !important;
        font-weight: 800 !important;
        letter-spacing: -0.5px;
    }

    h2 {
        color: #6B1E2E !important;
        font-weight: 750 !important;
    }

    h3 {
        color: #6B1E2E !important;
        font-weight: 700 !important;
    }

    /* =========================
       BODY TEXT
    ========================= */

    p {
        color: #5F5553;
        line-height: 1.65;
    }

    /* =========================
       DIVIDER
    ========================= */

    hr {
        border: none;
        border-top: 1px solid #E7D9D5;
        margin: 25px 0;
    }

    /* =========================
       NATIVE STREAMLIT CARDS
    ========================= */

    div[data-testid="stVerticalBlockBorderWrapper"] {
        background-color: #FFFFFF;
        border: 1px solid #E7D9D5;
        border-radius: 16px;
        box-shadow: 0 5px 18px rgba(90, 23, 37, 0.06);
    }

    div[data-testid="stVerticalBlockBorderWrapper"]:hover {
        border-color: #B9828C;
        box-shadow: 0 8px 24px rgba(90, 23, 37, 0.09);
    }

    /* =========================
       INFO BOX
    ========================= */

    div[data-testid="stAlert"] {
        background-color: #F6ECEE;
        border: 1px solid #DFC3C8;
        border-radius: 14px;
    }

    /* =========================
       BUTTONS
    ========================= */

    .stButton > button {
        background-color: #6B1E2E;
        color: white;
        border: none;
        border-radius: 10px;
        font-weight: 600;
    }

    .stButton > button:hover {
        background-color: #861F35;
        color: white;
        border: none;
    }

    /* =========================
       FOOTER
    ========================= */

    .footer-text {
        color: #9B8580;
        text-align: center;
        font-size: 13px;
        margin-top: 35px;
    }

</style>
""", unsafe_allow_html=True)


# =========================================================
# HERO
# =========================================================

st.title("💳 Digital Payments Intelligence")

st.subheader(
    "Interactive analytics dashboard for exploring digital payment "
    "transaction volume, transaction value, application performance "
    "and time-based trends."
)

st.divider()


# =========================================================
# PROJECT OVERVIEW
# =========================================================

st.header("📌 Project Overview")

st.write(
    """
    This project transforms structured digital payment transaction
    data into meaningful business insights through interactive
    analysis and visualisation.
    """
)

st.write(
    """
    The dashboard focuses on transaction volume, transaction value,
    payment-application performance, period-wise trends, and the
    relationship between transaction volume and transaction value.
    """
)


# =========================================================
# KEY FEATURES
# =========================================================

st.header("📊 What This Dashboard Analyses")

col1, col2, col3, col4 = st.columns(4)

with col1:

    with st.container(border=True):

        st.markdown("### 📈 Transaction Trends")

        st.write(
            "Analyse transaction volume across different time periods "
            "and identify changes in payment activity."
        )


with col2:

    with st.container(border=True):

        st.markdown("### 💰 Transaction Value")

        st.write(
            "Explore transaction value and identify periods with "
            "higher-value payment activity."
        )


with col3:

    with st.container(border=True):

        st.markdown("### 📱 Application Performance")

        st.write(
            "Compare payment applications using transaction volume "
            "and transaction value."
        )


with col4:

    with st.container(border=True):

        st.markdown("### 🔎 Interactive Analysis")

        st.write(
            "Apply filters and dynamically explore different "
            "segments of the dataset."
        )


# =========================================================
# BUSINESS QUESTIONS
# =========================================================

st.header("💡 Business Questions")

st.info(
    """
    **The dashboard helps answer questions such as:**

    • Which periods have the highest transaction volume?

    • Which periods generate the highest transaction value?

    • Which payment applications contribute the most transaction activity?

    • How is transaction value distributed across applications?

    • Is higher transaction volume associated with higher transaction value?

    • How does payment activity change across different periods?
    """
)


# =========================================================
# ANALYTICAL WORKFLOW
# =========================================================

st.header("⚙️ Analytical Workflow")

workflow1, workflow2 = st.columns(2)

with workflow1:

    with st.container(border=True):

        st.markdown("### 1️⃣ Data Preparation")

        st.write(
            "Load the dataset, clean column names, convert numerical "
            "fields and remove duplicate records."
        )

        st.markdown("### 2️⃣ Filtering")

        st.write(
            "Users can filter payment applications, periods, "
            "transaction volume and transaction value."
        )


with workflow2:

    with st.container(border=True):

        st.markdown("### 3️⃣ Analysis")

        st.write(
            "Calculate KPIs and analyse trends, application performance, "
            "distributions and relationships between metrics."
        )

        st.markdown("### 4️⃣ Visualisation")

        st.write(
            "Present analytical findings through interactive "
            "Plotly visualisations."
        )


# =========================================================
# TECHNOLOGIES
# =========================================================

st.header("🛠️ Technologies Used")

tech1, tech2, tech3, tech4 = st.columns(4)

with tech1:

    with st.container(border=True):

        st.markdown("### 🐍 Python")

        st.write(
            "Main programming language for data processing, "
            "analysis and dashboard development."
        )


with tech2:

    with st.container(border=True):

        st.markdown("### 🐼 Pandas")

        st.write(
            "Used for loading, cleaning, filtering and aggregating data."
        )


with tech3:

    with st.container(border=True):

        st.markdown("### 📊 Plotly")

        st.write(
            "Used to create interactive analytical visualisations."
        )


with tech4:

    with st.container(border=True):

        st.markdown("### 🚀 Streamlit")

        st.write(
            "Used to build the interactive web-based analytics dashboard."
        )


# =========================================================
# EXPLORE PROJECT
# =========================================================

st.header("🚀 Explore the Project")

st.info(
    "Use the sidebar to open the About page for project methodology "
    "and dataset information, or open the Dashboard page to interact "
    "with the analysis."
)


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    '<p class="footer-text">'
    'Digital Payments Intelligence • Data Analytics Portfolio Project'
    '</p>',
    unsafe_allow_html=True
)