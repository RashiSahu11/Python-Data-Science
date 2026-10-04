import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px


# --------------------------------------------------
# PAGE TITLE
# --------------------------------------------------

st.title("Explore the Insights Here")


# --------------------------------------------------
# LOAD DATASET
# --------------------------------------------------

df = sns.load_dataset("car_crashes")


# --------------------------------------------------
# CREATE STATE COLUMN
# --------------------------------------------------

df["State"] = df["abbrev"]


# --------------------------------------------------
# SIDEBAR FILTER
# --------------------------------------------------

st.sidebar.title("Dashboard Filters")

selected_state = st.sidebar.multiselect(
    "Select State",
    options=df["State"].unique(),
    default=df["State"].unique()
)


# --------------------------------------------------
# FILTER DATA
# --------------------------------------------------

filtered_df = df[df["State"].isin(selected_state)]


# --------------------------------------------------
# KPI CARDS
# --------------------------------------------------

col1, col2, col3 = st.columns(3)

col1.metric(
    "Average Accidents %",
    f"{filtered_df['total'].mean():.2f}%"
)

col2.metric(
    "Average Speeding %",
    f"{filtered_df['speeding'].mean():.2f}%"
)

col3.metric(
    "Average Alcoholic %",
    f"{filtered_df['alcohol'].mean():.2f}%"
)


# --------------------------------------------------
# DATASET PREVIEW
# --------------------------------------------------

st.subheader("Filtered Data")

st.dataframe(
    filtered_df,
    use_container_width=True
)


# --------------------------------------------------
# GRAPH 1 - TOTAL ACCIDENTS BY STATE
# --------------------------------------------------

figbar = px.bar(
    filtered_df,
    x="abbrev",
    y="total",
    title="State-wise Total Accidents",
    labels={
        "abbrev": "State",
        "total": "Total Accidents"
    },
    color="total",
    template="plotly_dark"
)

st.plotly_chart(
    figbar,
    use_container_width=True
)


# --------------------------------------------------
# GRAPH 2 - STATE-WISE ACCIDENTS
# --------------------------------------------------

figbars = px.bar(
    filtered_df,
    x="abbrev",
    y="total",
    title="State-wise Accident Comparison",
    labels={
        "abbrev": "State",
        "total": "Total Accidents"
    },
    color="abbrev"
)

st.plotly_chart(
    figbars,
    use_container_width=True
)


# --------------------------------------------------
# ROW 3 - LINE CHART + PIE CHART
# --------------------------------------------------

col1, col2 = st.columns(2)


# LINE CHART
with col1:

    figs = px.line(
        filtered_df,
        x="abbrev",
        y="total",
        title="State-wise Total Accidents",
        labels={
            "abbrev": "State",
            "total": "Total Accidents"
        },
        template="plotly_dark",
        color_discrete_sequence=px.colors.sequential.Burg
    )

    st.plotly_chart(
        figs,
        use_container_width=True
    )


# PIE CHART
with col2:

    figpie_small = px.pie(
        filtered_df,
        values="speeding",
        names="abbrev",
        title="Speeding Accidents by State"
    )

    st.plotly_chart(
        figpie_small,
        use_container_width=True
    )


# --------------------------------------------------
# GRAPH 4 - SPEEDING ACCIDENTS PIE CHART
# --------------------------------------------------

figpie = px.pie(
    filtered_df,
    values="speeding",
    names="abbrev",
    title="Speeding Accidents",
    template="plotly_dark",
    color_discrete_sequence=px.colors.sequential.algae_r,
    height=600,
    width=600
)

figpie.update_traces(
    textposition="inside"
)

st.plotly_chart(
    figpie,
    use_container_width=True
)


# --------------------------------------------------
# TOP 10 STATES BY INSURANCE PREMIUM
# --------------------------------------------------

top10 = (
    filtered_df
    .sort_values(
        "ins_premium",
        ascending=False
    )
    .head(10)
)


bar = px.bar(
    top10,
    x="abbrev",
    y="ins_premium",
    title="Top 10 States by Insurance Premium",
    labels={
        "abbrev": "State",
        "ins_premium": "Insurance Premium"
    },
    color="abbrev",
    template="plotly_dark"
)

st.plotly_chart(
    bar,
    use_container_width=True
)


# --------------------------------------------------
# SCATTER PLOT - SPEEDING VS ALCOHOL
# --------------------------------------------------

scatter = px.scatter(
    filtered_df,
    x="speeding",
    y="alcohol",
    color="speeding",
    size="total",
    title="Relationship Between Speeding and Alcohol",
    labels={
        "speeding": "Speeding %",
        "alcohol": "Alcohol %",
        "total": "Total Accidents"
    },
    template="plotly_dark"
)

st.plotly_chart(
    scatter,
    use_container_width=True
)