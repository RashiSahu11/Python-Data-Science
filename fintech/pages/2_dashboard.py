import streamlit as st
import pandas as pd
import plotly.express as px


# =========================================================
# PAGE SETTINGS
# =========================================================

st.set_page_config(
    page_title="Digital Payments Dashboard",
    page_icon="💳",
    layout="wide"
)


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown(
    """
    <style>

    .stApp {
        background-color: #FFFDF8;
    }

    [data-testid="stSidebar"] {
        background-color: #F8F1F2;
    }

    .main-title {
        font-size: 42px;
        font-weight: 800;
        color: #7F1D3A;
        margin-bottom: 5px;
    }

    .subtitle {
        color: #78716C;
        font-size: 17px;
        margin-bottom: 25px;
    }

    .kpi-card {
        background-color: #FFFFFF;
        padding: 20px;
        border-radius: 14px;
        border: 1px solid #E7E5E4;
        text-align: center;
        box-shadow: 0px 3px 10px rgba(0,0,0,0.05);
    }

    .kpi-title {
        color: #78716C;
        font-size: 14px;
        font-weight: 600;
    }

    .kpi-value {
        color: #7F1D3A;
        font-size: 27px;
        font-weight: 800;
        margin-top: 6px;
    }

    .section-title {
        color: #7F1D3A;
        font-size: 25px;
        font-weight: 750;
        margin-top: 30px;
        margin-bottom: 15px;
    }

    .explanation {
        background-color: #FFFFFF;
        border-left: 5px solid #9F1239;
        padding: 14px 18px;
        margin-top: 8px;
        margin-bottom: 25px;
        border-radius: 8px;
        border-top: 1px solid #E7E5E4;
        border-right: 1px solid #E7E5E4;
        border-bottom: 1px solid #E7E5E4;
    }

    .explanation-title {
        color: #7F1D3A;
        font-weight: 700;
        font-size: 15px;
        margin-bottom: 5px;
    }

    .explanation-text {
        color: #57534E;
        font-size: 14px;
        line-height: 1.6;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# HELPER FUNCTIONS
# =========================================================

def format_number(value):
    if value >= 1_000_000:
        return f"{value / 1_000_000:.2f}M"
    elif value >= 1_000:
        return f"{value / 1_000:.2f}K"
    else:
        return f"{value:,.2f}"


def kpi_card(title, value):
    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-title">{title}</div>
            <div class="kpi-value">{value}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


def graph_explanation(title, text):
    st.markdown(
        f"""
        <div class="explanation">
            <div class="explanation-title">{title}</div>
            <div class="explanation-text">{text}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# LOAD DATA
# =========================================================

@st.cache_data
def load_data():

    df = pd.read_csv("Digital_Payments_2025_Dataset.csv")

    return df


# =========================================================
# LOAD DATA SAFELY
# =========================================================

try:

    df = load_data()

except FileNotFoundError:

    st.error(
        "Digital_Payments_2025_Dataset.csv was not found. "
        "Make sure the CSV file is in the main project folder."
    )

    st.stop()


# =========================================================
# CLEAN COLUMN NAMES
# =========================================================

df.columns = df.columns.str.strip()


# =========================================================
# REMOVE DUPLICATES
# =========================================================

df = df.drop_duplicates()


# =========================================================
# NUMERIC COLUMNS
# =========================================================

numeric_columns = [
    "CustomerTxCount (Mn)",
    "CustomerTxValue (Cr)",
    "TotalTxCount (Mn)",
    "TotalTxValue (Cr)"
]

for column in numeric_columns:

    if column in df.columns:

        df[column] = pd.to_numeric(
            df[column],
            errors="coerce"
        )


# Remove rows where the main transaction columns are missing

available_numeric_columns = [
    column for column in numeric_columns
    if column in df.columns
]

if available_numeric_columns:

    df = df.dropna(
        subset=available_numeric_columns
    )


# =========================================================
# DASHBOARD HEADER
# =========================================================

st.markdown(
    '<div class="main-title">💳 Digital Payments Intelligence</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Interactive analysis of digital payment transaction activity, '
    'transaction value and payment-application performance.'
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# SIDEBAR FILTERS
# =========================================================

st.sidebar.markdown("## 🔎 Filters")


# ---------------------------------------------------------
# PAYMENT APPLICATION FILTER
# ---------------------------------------------------------

if "PaymentApps" in df.columns:

    payment_apps = sorted(
        df["PaymentApps"].dropna().unique().tolist()
    )

    selected_apps = st.sidebar.multiselect(
        "Payment Application",
        payment_apps,
        default=payment_apps
    )

else:

    selected_apps = []


# ---------------------------------------------------------
# PERIOD FILTER
# ---------------------------------------------------------

if "Period" in df.columns:

    periods = sorted(
        df["Period"].dropna().unique().tolist()
    )

    selected_periods = st.sidebar.multiselect(
        "Period",
        periods,
        default=periods
    )

else:

    selected_periods = []


# ---------------------------------------------------------
# TRANSACTION COUNT FILTER
# ---------------------------------------------------------

if "TotalTxCount (Mn)" in df.columns:

    min_count = float(
        df["TotalTxCount (Mn)"].min()
    )

    max_count = float(
        df["TotalTxCount (Mn)"].max()
    )

    selected_min_count = st.sidebar.slider(
        "Minimum Transaction Count (Mn)",
        min_value=min_count,
        max_value=max_count,
        value=min_count
    )

else:

    selected_min_count = 0


# ---------------------------------------------------------
# TRANSACTION VALUE FILTER
# ---------------------------------------------------------

if "TotalTxValue (Cr)" in df.columns:

    min_value = float(
        df["TotalTxValue (Cr)"].min()
    )

    max_value = float(
        df["TotalTxValue (Cr)"].max()
    )

    selected_min_value = st.sidebar.slider(
        "Minimum Transaction Value (Cr)",
        min_value=min_value,
        max_value=max_value,
        value=min_value
    )

else:

    selected_min_value = 0


# =========================================================
# APPLY FILTERS
# =========================================================

filtered_df = df.copy()


if "PaymentApps" in filtered_df.columns and selected_apps:

    filtered_df = filtered_df[
        filtered_df["PaymentApps"].isin(selected_apps)
    ]


if "Period" in filtered_df.columns and selected_periods:

    filtered_df = filtered_df[
        filtered_df["Period"].isin(selected_periods)
    ]


if "TotalTxCount (Mn)" in filtered_df.columns:

    filtered_df = filtered_df[
        filtered_df["TotalTxCount (Mn)"] >= selected_min_count
    ]


if "TotalTxValue (Cr)" in filtered_df.columns:

    filtered_df = filtered_df[
        filtered_df["TotalTxValue (Cr)"] >= selected_min_value
    ]


# =========================================================
# CHECK FILTER RESULT
# =========================================================

if filtered_df.empty:

    st.warning(
        "No records match the selected filters. "
        "Try changing the filter values."
    )

    st.stop()


# =========================================================
# KPI CALCULATIONS
# =========================================================

if "TotalTxCount (Mn)" in filtered_df.columns:

    total_transactions = filtered_df[
        "TotalTxCount (Mn)"
    ].sum()

else:

    total_transactions = 0


if "TotalTxValue (Cr)" in filtered_df.columns:

    total_transaction_value = filtered_df[
        "TotalTxValue (Cr)"
    ].sum()

else:

    total_transaction_value = 0


if total_transactions > 0:

    average_transaction_value = (
        total_transaction_value /
        total_transactions
    )

else:

    average_transaction_value = 0


if "PaymentApps" in filtered_df.columns:

    number_of_apps = filtered_df[
        "PaymentApps"
    ].nunique()

else:

    number_of_apps = 0


# =========================================================
# KPI SECTION
# =========================================================

st.markdown(
    '<div class="section-title">📌 Key Performance Indicators</div>',
    unsafe_allow_html=True
)

col1, col2, col3, col4 = st.columns(4)


with col1:

    kpi_card(
        "Total Transactions",
        f"{total_transactions:,.2f} Mn"
    )


with col2:

    kpi_card(
        "Transaction Value",
        f"{total_transaction_value:,.2f} Cr"
    )


with col3:

    kpi_card(
        "Avg. Value / Transaction",
        f"{average_transaction_value:,.2f}"
    )


with col4:

    kpi_card(
        "Payment Applications",
        str(number_of_apps)
    )


# =========================================================
# CHART 1
# TRANSACTION VOLUME BY PERIOD
# =========================================================

st.markdown(
    '<div class="section-title">📈 Transaction Volume Trend</div>',
    unsafe_allow_html=True
)

if "Period" in filtered_df.columns and "TotalTxCount (Mn)" in filtered_df.columns:

    period_volume = (
        filtered_df
        .groupby("Period", as_index=False)["TotalTxCount (Mn)"]
        .sum()
    )

    fig1 = px.line(
        period_volume,
        x="Period",
        y="TotalTxCount (Mn)",
        markers=True,
        title="Transaction Volume by Period"
    )

    fig1.update_layout(
        plot_bgcolor="white",
        paper_bgcolor="white",
        font=dict(color="#292524")
    )

    st.plotly_chart(
        fig1,
        use_container_width=True
    )

    graph_explanation(
        "What this shows",
        "This line chart tracks how transaction volume changes "
        "across the selected periods. Peaks indicate periods with "
        "higher transaction activity, while declines indicate lower "
        "transaction activity."
    )


# =========================================================
# CHART 2
# TRANSACTION VALUE BY PERIOD
# =========================================================

st.markdown(
    '<div class="section-title">💰 Transaction Value Trend</div>',
    unsafe_allow_html=True
)

if "Period" in filtered_df.columns and "TotalTxValue (Cr)" in filtered_df.columns:

    period_value = (
        filtered_df
        .groupby("Period", as_index=False)["TotalTxValue (Cr)"]
        .sum()
    )

    fig2 = px.bar(
        period_value,
        x="Period",
        y="TotalTxValue (Cr)",
        title="Transaction Value by Period"
    )

    fig2.update_layout(
        plot_bgcolor="white",
        paper_bgcolor="white",
        font=dict(color="#292524")
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

    graph_explanation(
        "Business interpretation",
        "This chart compares the total monetary value processed "
        "during each period. It helps identify periods where "
        "digital payment activity generated higher transaction value."
    )


# =========================================================
# CHART 3
# PAYMENT APPLICATION PERFORMANCE
# =========================================================

st.markdown(
    '<div class="section-title">🏆 Payment Application Performance</div>',
    unsafe_allow_html=True
)

if "PaymentApps" in filtered_df.columns and "TotalTxCount (Mn)" in filtered_df.columns:

    app_volume = (
        filtered_df
        .groupby("PaymentApps", as_index=False)["TotalTxCount (Mn)"]
        .sum()
        .sort_values(
            "TotalTxCount (Mn)",
            ascending=True
        )
    )

    fig3 = px.bar(
        app_volume,
        x="TotalTxCount (Mn)",
        y="PaymentApps",
        orientation="h",
        title="Payment Applications by Transaction Volume"
    )

    fig3.update_layout(
        plot_bgcolor="white",
        paper_bgcolor="white",
        font=dict(color="#292524")
    )

    st.plotly_chart(
        fig3,
        use_container_width=True
    )

    graph_explanation(
        "Business interpretation",
        "This comparison shows which payment applications account "
        "for the highest transaction volume within the selected "
        "analysis scope."
    )


# =========================================================
# CHART 4
# TRANSACTION VALUE SHARE
# =========================================================

st.markdown(
    '<div class="section-title">🥧 Transaction Value Distribution</div>',
    unsafe_allow_html=True
)

if "PaymentApps" in filtered_df.columns and "TotalTxValue (Cr)" in filtered_df.columns:

    app_value = (
        filtered_df
        .groupby("PaymentApps", as_index=False)["TotalTxValue (Cr)"]
        .sum()
    )

    if len(app_value) <= 10:

        fig4 = px.pie(
            app_value,
            names="PaymentApps",
            values="TotalTxValue (Cr)",
            hole=0.45,
            title="Transaction Value Share by Payment Application"
        )

        fig4.update_layout(
            paper_bgcolor="white",
            font=dict(color="#292524")
        )

        st.plotly_chart(
            fig4,
            use_container_width=True
        )

        graph_explanation(
            "Business interpretation",
            "The donut chart shows how total transaction value is "
            "distributed across payment applications. Larger segments "
            "represent applications contributing a greater share of "
            "the total transaction value."
        )


# =========================================================
# CHART 5
# TRANSACTION VALUE DISTRIBUTION
# =========================================================

st.markdown(
    '<div class="section-title">📊 Transaction Value Distribution</div>',
    unsafe_allow_html=True
)

if "TotalTxValue (Cr)" in filtered_df.columns:

    fig5 = px.histogram(
        filtered_df,
        x="TotalTxValue (Cr)",
        nbins=20,
        title="Distribution of Transaction Values"
    )

    fig5.update_layout(
        plot_bgcolor="white",
        paper_bgcolor="white",
        font=dict(color="#292524")
    )

    st.plotly_chart(
        fig5,
        use_container_width=True
    )

    graph_explanation(
        "What this shows",
        "The histogram shows how transaction values are distributed "
        "across the dataset. It helps identify whether transaction "
        "values are concentrated within a particular range or spread "
        "across a wider range."
    )


# =========================================================
# CHART 6
# TRANSACTION VOLUME VS VALUE
# =========================================================

st.markdown(
    '<div class="section-title">🔎 Transaction Volume vs Value</div>',
    unsafe_allow_html=True
)

if (
    "TotalTxCount (Mn)" in filtered_df.columns
    and "TotalTxValue (Cr)" in filtered_df.columns
):

    if "PaymentApps" in filtered_df.columns:

        fig6 = px.scatter(
            filtered_df,
            x="TotalTxCount (Mn)",
            y="TotalTxValue (Cr)",
            color="PaymentApps",
            title="Transaction Volume vs Transaction Value",
            hover_data=["Period"]
        )

    else:

        fig6 = px.scatter(
            filtered_df,
            x="TotalTxCount (Mn)",
            y="TotalTxValue (Cr)",
            title="Transaction Volume vs Transaction Value"
        )

    fig6.update_layout(
        plot_bgcolor="white",
        paper_bgcolor="white",
        font=dict(color="#292524")
    )

    st.plotly_chart(
        fig6,
        use_container_width=True
    )

    graph_explanation(
        "Analytical interpretation",
        "The scatter plot examines the relationship between "
        "transaction volume and transaction value. Points positioned "
        "higher and further right represent combinations of higher "
        "transaction activity and higher transaction value."
    )


# =========================================================
# CHART 7
# PAYMENT APPLICATION HEATMAP
# =========================================================

st.markdown(
    '<div class="section-title">🔥 Payment Activity Heatmap</div>',
    unsafe_allow_html=True
)

if (
    "PaymentApps" in filtered_df.columns
    and "Period" in filtered_df.columns
    and "TotalTxCount (Mn)" in filtered_df.columns
):

    heatmap_data = filtered_df.pivot_table(
        index="PaymentApps",
        columns="Period",
        values="TotalTxCount (Mn)",
        aggfunc="sum",
        fill_value=0
    )

    fig7 = px.imshow(
        heatmap_data,
        text_auto=True,
        aspect="auto",
        title="Payment Application Activity by Period"
    )

    fig7.update_layout(
        paper_bgcolor="white",
        font=dict(color="#292524")
    )

    st.plotly_chart(
        fig7,
        use_container_width=True
    )

    graph_explanation(
        "Business interpretation",
        "The heatmap compares transaction activity across payment "
        "applications and periods. Darker or more intense cells "
        "represent combinations with relatively higher transaction "
        "volume."
    )


# =========================================================
# KEY INSIGHTS
# =========================================================

st.markdown(
    '<div class="section-title">💡 Key Insights</div>',
    unsafe_allow_html=True
)


col1, col2, col3, col4 = st.columns(4)


# Leading application

with col1:

    if "PaymentApps" in filtered_df.columns:

        leading_app = (
            filtered_df
            .groupby("PaymentApps")["TotalTxCount (Mn)"]
            .sum()
            .idxmax()
        )

        st.metric(
            "Leading Application",
            leading_app
        )


# Highest value period

with col2:

    if "Period" in filtered_df.columns:

        highest_value_period = (
            filtered_df
            .groupby("Period")["TotalTxValue (Cr)"]
            .sum()
            .idxmax()
        )

        st.metric(
            "Highest-Value Period",
            str(highest_value_period)
        )


# Highest volume period

with col3:

    if "Period" in filtered_df.columns:

        highest_volume_period = (
            filtered_df
            .groupby("Period")["TotalTxCount (Mn)"]
            .sum()
            .idxmax()
        )

        st.metric(
            "Highest-Volume Period",
            str(highest_volume_period)
        )


# Current scope

with col4:

    st.metric(
        "Records in Current Scope",
        f"{len(filtered_df):,}"
    )


# =========================================================
# DATA PREVIEW
# =========================================================

st.markdown(
    '<div class="section-title">📋 Filtered Data Preview</div>',
    unsafe_allow_html=True
)

st.dataframe(
    filtered_df,
    use_container_width=True
)


# =========================================================
# DOWNLOAD BUTTON
# =========================================================

st.markdown(
    '<div class="section-title">⬇️ Download Analysis Data</div>',
    unsafe_allow_html=True
)

csv_data = filtered_df.to_csv(index=False)

st.download_button(
    label="Download Filtered CSV",
    data=csv_data,
    file_name="filtered_digital_payments.csv",
    mime="text/csv"
)


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    """
    <br>
    <hr>
    <p style="text-align:center; color:#78716C;">
        Digital Payments Intelligence • Python • Pandas • Plotly • Streamlit
    </p>
    """,
    unsafe_allow_html=True
)