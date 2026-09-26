import streamlit as st

# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="About | Digital Payments Intelligence",
    page_icon="📘",
    layout="wide"
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
       CARDS
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
       ALERTS
    ========================= */

    div[data-testid="stAlert"] {
        border-radius: 14px;
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
# PAGE HEADER
# =========================================================

st.title("📘 About the Project")

st.subheader(
    "Digital Payments Intelligence — turning transaction data "
    "into structured business insights."
)

st.divider()


# =========================================================
# PROJECT OBJECTIVE
# =========================================================

st.header("🎯 Project Objective")

with st.container(border=True):

    st.subheader("Turning Transaction Data into Business Insights")

    st.write(
        """
        The objective of this project is to analyse digital payment
        transaction activity and convert structured transaction data
        into clear and interactive business insights.
        """
    )

    st.write(
        """
        The analysis focuses on transaction volume, transaction value,
        payment-application performance, period-wise trends, and the
        relationship between transaction volume and transaction value.
        """
    )


# =========================================================
# DATASET
# =========================================================

st.header("🗂️ Dataset")

with st.container(border=True):

    st.subheader("Digital Payments Dataset")

    st.write(
        """
        The dataset contains aggregated digital-payment transaction
        information across payment applications and time periods.
        """
    )

    st.write(
        """
        It is used for analytical and portfolio purposes and is not
        treated as private or proprietary transaction data from any
        individual payment company.
        """
    )


# =========================================================
# DATASET FIELDS
# =========================================================

st.header("📋 Dataset Fields")

fields = [
    (
        "PaymentApps",
        "Payment application represented in the dataset."
    ),
    (
        "CustomerTxCount (Mn)",
        "Customer transaction count, measured in millions."
    ),
    (
        "CustomerTxValue (Cr)",
        "Customer transaction value, measured in crores."
    ),
    (
        "TotalTxCount (Mn)",
        "Total transaction count, measured in millions."
    ),
    (
        "TotalTxValue (Cr)",
        "Total transaction value, measured in crores."
    ),
    (
        "Period",
        "Time period used for analysing transaction activity."
    ),
    (
        "Yr",
        "Year associated with the corresponding records."
    )
]

for field_name, description in fields:

    with st.container(border=True):

        st.markdown(f"### `{field_name}`")

        st.write(description)


# =========================================================
# TECHNOLOGIES
# =========================================================

st.header("🛠️ Technologies Used")

tech1, tech2 = st.columns(2)

with tech1:

    with st.container(border=True):

        st.subheader("🐍 Python")

        st.write(
            "Main programming language used for data processing, "
            "analysis and dashboard development."
        )

    with st.container(border=True):

        st.subheader("🐼 Pandas")

        st.write(
            "Used for loading, cleaning, filtering, grouping "
            "and aggregating the dataset."
        )


with tech2:

    with st.container(border=True):

        st.subheader("📊 Plotly")

        st.write(
            "Used to create interactive visualisations for trends, "
            "comparisons, distributions and analytical relationships."
        )

    with st.container(border=True):

        st.subheader("🚀 Streamlit")

        st.write(
            "Used to build the interactive web-based analytics dashboard."
        )


# =========================================================
# ANALYTICAL METHODOLOGY
# =========================================================

st.header("🔬 Analytical Methodology")

methodology = [
    "Load and inspect the dataset.",
    "Clean column names and numerical fields.",
    "Remove duplicate records.",
    "Handle invalid or missing numerical values.",
    "Apply interactive filters.",
    "Calculate key performance indicators.",
    "Analyse transaction trends across periods.",
    "Compare payment applications.",
    "Analyse transaction-value distribution.",
    "Examine transaction volume versus transaction value.",
    "Present findings through interactive visualisations."
]

for number, step in enumerate(methodology, 1):

    with st.container(border=True):

        st.write(f"**{number}.** {step}")


# =========================================================
# ANALYTICAL SCOPE
# =========================================================

st.header("📊 Analytical Scope")

scope1, scope2 = st.columns(2)

with scope1:

    with st.container(border=True):
        st.write("✓ Transaction volume trends")

    with st.container(border=True):
        st.write("✓ Transaction value trends")

    with st.container(border=True):
        st.write("✓ Payment application comparison")

    with st.container(border=True):
        st.write("✓ Transaction value distribution")


with scope2:

    with st.container(border=True):
        st.write("✓ Transaction volume versus transaction value")

    with st.container(border=True):
        st.write("✓ Payment application activity across periods")

    with st.container(border=True):
        st.write("✓ Interactive filtered-data exploration")


# =========================================================
# ANALYTICAL LIMITATIONS
# =========================================================

st.header("⚠️ Analytical Limitations")

st.warning(
    """
    The dataset contains aggregated transaction information rather
    than individual customer-level records.

    Therefore, this project does not claim to measure individual
    customer churn, retention, customer lifetime value, or other
    customer-level behavioural metrics.

    The analysis is restricted to transaction and payment-application
    metrics supported by the available dataset.
    """
)


# =========================================================
# PROJECT STRUCTURE
# =========================================================

st.header("📁 Project Structure")

project_files = [
    (
        "app.py",
        "Main Home page and project introduction."
    ),
    (
        "Digital_Payments_2025_Dataset.csv",
        "Dataset used for the analysis."
    ),
    (
        "requirements.txt",
        "Required Python libraries for running the project."
    ),
    (
        "pages/1_📘_About.py",
        "Project information, methodology, scope, limitations and dataset details."
    ),
    (
        "pages/2_📊_Dashboard.py",
        "Interactive filters, KPIs, charts, insights, filtered data and CSV download."
    )
]

for filename, description in project_files:

    with st.container(border=True):

        st.subheader(filename)

        st.write(description)


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    '<p class="footer-text">'
    'Digital Payments Intelligence • Data Analytics Portfolio Project'
    '</p>',
    unsafe_allow_html=True
)