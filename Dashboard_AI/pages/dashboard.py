import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Dashboard | Automobile Analytics",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.set_page_config(
    page_title="Automobile Analytics",
    page_icon="🏎️",
    layout="wide",
    initial_sidebar_state="expanded"
)


st.markdown("""
<style>

/* MAIN BACKGROUND */

.stApp {
    background-color: #0B1117;
}




/* DASHBOARD TITLE */

.dashboard-title {
    font-size: 46px;
    font-weight: 800;
    color: #FFFFFF;
    margin-bottom: 5px;
}

.dashboard-subtitle {
    font-size: 17px;
    color: #A7B0B8;
    margin-bottom: 30px;
}


/* SECTION HEADINGS */

.section-title {
    font-size: 28px;
    font-weight: 700;
    color: #FFFFFF;
    margin-top: 35px;
    margin-bottom: 15px;
}


/* KPI CARDS */

[data-testid="stMetric"] {
    background: #111A22;
    border: 1px solid rgba(20,184,166,0.25);
    border-radius: 16px;
    padding: 20px;
}

[data-testid="stMetricLabel"] {
    color: #A7B0B8;
}

[data-testid="stMetricValue"] {
    color: #14B8A6;
}


/* SIDEBAR */

[data-testid="stSidebar"] {
    background-color: #0F171F;
}

[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3 {
    color: #FFFFFF;
}




/* CAPTIONS */

.stCaption {
    color: #A7B0B8;
    font-size: 14px;
}


/* EXPANDER */

[data-testid="stExpander"] {
    border: 1px solid rgba(20,184,166,0.20);
    border-radius: 12px;
}


/* DIVIDER */

hr {
    border-color: rgba(20,184,166,0.20);
}

</style>
""", unsafe_allow_html=True)


st.markdown("""
<div class="dashboard-title">
AUTOMOBILE ANALYTICS 🏎️
</div>

<div class="dashboard-subtitle">
Interactive data analysis of automobile prices, specifications and market characteristics
</div>
""", unsafe_allow_html=True)   



#data set preview
df=pd.read_csv("automobile_dataset.csv")
#st.dataframe(df)

with st.expander("🔍 View Automobile Dataset"):
    st.dataframe(df, use_container_width=True)


#filter connectivity
selected_fuel = st.sidebar.multiselect(
    "Select Fuel Type",
    options=df['Fuel_Type'].unique(),
    default=df['Fuel_Type'].unique()
)

filtered_df=df[df['Fuel_Type'].isin(selected_fuel)]


year_range = st.sidebar.slider(
    "Select Year",
    int(df['Year'].min()),
    int(df['Year'].max()),
    (int(df['Year'].min()), int(df['Year'].max()))
)

filtered_df = filtered_df[
    filtered_df['Year'].between(year_range[0], year_range[1])
]


selected_make = st.sidebar.multiselect(
    "Select Make",
    options=df['Make'].unique(),
    default=df['Make'].unique()
)

filtered_df = filtered_df[
    filtered_df['Make'].isin(selected_make)
]


selected_body = st.sidebar.multiselect(
    "Select Body Type",
    options=df['Body_Type'].unique(),
    default=df['Body_Type'].unique()
)


filtered_df = filtered_df[
    filtered_df['Body_Type'].isin(selected_body)
]


if filtered_df.empty:
    st.warning("No cars match the selected filters. Please change your filters.")
    st.stop()


    # Check if filtered data is empty
if filtered_df.empty:
    st.warning("No cars match the selected filters. Please change your filters.")
    st.stop()

# DOWNLOAD BUTTON
csv = filtered_df.to_csv(index=False)

st.download_button(
    label="⬇️ Download Filtered Data",
    data=csv,
    file_name="filtered_automobiles.csv",
    mime="text/csv"
)




#KPI CARDS
col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Cars",
    f"{len(filtered_df):,}"
)

col2.metric(
    "Average Selling Price",
    f"{filtered_df['Selling_Price'].mean():,.0f}"
)

col3.metric(
    "Average Mileage",
    f"{filtered_df['Mileage'].mean():,.0f}"
)



#graph connectivity

st.markdown("""
<div class="section-title">
💰 Price Analysis
</div>
""", unsafe_allow_html=True)



top10 = filtered_df.nlargest(10, 'Selling_Price')

fig = px.bar(
    top10,
    x='Selling_Price',
    y='Model',
    orientation='h',
    color='Selling_Price',
    title='Top 10 Most Expensive Cars',
    template='plotly_dark'
)

st.plotly_chart(fig, use_container_width=True)

st.caption("This graph displays the 10 most expensive cars based on their selling price and helps identify the highest-priced vehicles.")


fuel_price = filtered_df.groupby('Fuel_Type')['Selling_Price'].mean().reset_index()

fig = px.bar(
    fuel_price,
    x='Fuel_Type',
    y='Selling_Price',
    color='Fuel_Type',
    title='Average Selling Price by Fuel Type',
    template='plotly_dark'
)

st.plotly_chart(fig, use_container_width=True)

st.caption("This graph compares the average selling price of cars using different fuel types and shows differences in their overall price levels.")


avg_price = filtered_df.groupby('Make')['Selling_Price'].mean().reset_index()
avg_price.columns = ['Make','Average Price']


bar=px.bar(avg_price,x='Make',
           y='Average Price',
     color='Average Price',template='plotly_dark',
     title='Average Selling Price by Make')

st.plotly_chart(bar)

st.caption("This graph compares the average selling price of different car makes and shows which brands have higher overall prices.")


his = px.histogram(
    filtered_df,
    x='Selling_Price',
    title='Selling Price Distribution',
    labels={'Selling_Price':'SELLING PRICE'},
    template='plotly_dark'
)

st.plotly_chart(his, use_container_width=True)

st.caption(
    "This histogram shows how the selling prices are distributed "
    "and where most of the cars are concentrated in terms of price."
)


year_price=filtered_df.groupby('Year')['Selling_Price'].mean().reset_index()

line=px.line(year_price, x='Year',
             y='Selling_Price',
             labels={'Year':'YEAR','Selling_price':'SELLING PRICE'},
             template='plotly_dark',
             title='SELLING PRICE BY YEAR')

st.plotly_chart(line)

st.caption("This graph shows how the average selling price changes across different years and helps identify price trends over time.")




st.markdown("""
<div class="section-title">
🚗 Vehicle Analysis
</div>
""", unsafe_allow_html=True)


brand_count = filtered_df['Make'].value_counts().reset_index()
brand_count.columns=['Make','Count of Cars']

bar= px.bar(
 brand_count,
 x='Make',
 y='Count of Cars',
 color='Count of Cars',
 template='plotly_dark',
 title='Number of Cars by Make'
)

st.plotly_chart(bar)

st.caption(
    "This graph shows the number of cars available for each make. "
    "It helps compare which brands have the highest and lowest number of cars."
)



body_count = filtered_df.groupby('Body_Type').size().reset_index(name='Number_of_Cars')

bar = px.bar(
    body_count,
    x='Body_Type',
    y='Number_of_Cars',
    color='Number_of_Cars',
    title='Number of Cars by Body Type',
    template='plotly_dark'
)

st.plotly_chart(bar, use_container_width=True)

st.caption(
    "This graph shows the number of cars in each body type "
    "and helps identify the most common vehicle designs in the dataset."
)


fuel_count=filtered_df['Fuel_Type'].value_counts().reset_index()
fuel_count.columns=['Fuel_Type','Number_of_Cars']

pie=px.pie(fuel_count, 
           names= 'Fuel_Type',
           values='Number_of_Cars',
           title='Fuel type by Number of Cars',
           hole=0.45,
    color_discrete_sequence=[
        '#0F766E',
        '#14B8A6',
        '#5EEAD4',
        '#99F6E4',
        '#CCFBF1'
    ]
    )

st.plotly_chart(pie, use_container_width=True)


st.caption("This donut chart shows the proportion of cars using each fuel type and helps understand the overall fuel-type composition of the dataset.")



st.markdown("""
<div class="section-title">
🔬 Relationship Analysis
</div>
""", unsafe_allow_html=True)


scatter=px.scatter(filtered_df, x='Mileage',
                    y='Selling_Price',
                   title="Mileage vs Selling Price",
                    color= 'Fuel_Type',
                    template='plotly_dark')

st.plotly_chart(scatter)

st.caption("This scatter plot shows the relationship between mileage and selling price. It helps identify whether cars with higher mileage tend to have lower prices.")




scatterr=px.scatter(filtered_df,x='Engine_Size',
                   y='Horsepower',
                   color='Fuel_Type',
                   title="Engine Size vs Horsepower by Fuel Type",
                   template='plotly_dark')

st.plotly_chart(scatterr)

st.caption("This graph compares engine size and horsepower and shows how these two vehicle specifications are related across different fuel types.")




box=px.box(filtered_df,x='Accident_History',
           y='Selling_Price',
           title='Accidental History vs Selling Price',
           template='plotly_dark',
           labels={'Accidental_History':'ACCIDENTAL HISTORY','Selling_Price':'SELLING PRICE'})

st.plotly_chart(box)

st.caption("This graph compares selling prices across different accident history categories and helps understand how accident history may affect vehicle prices.")



fig=px.scatter(filtered_df,x='Fuel_Efficiency',
               y='Selling_Price',
               color='Body_Type',
               title='Fuel Efficiency vs Selling Price by Body Type',
               labels={'Fuel_Efficiency':'Efficiency of Fuel','Selling_Price':'Selling price'},
               template='plotly_dark')

st.plotly_chart(fig)

st.caption("This scatter plot shows the relationship between fuel efficiency and selling price and allows comparison across different body types.")


#KEY INSIGHTS


st.subheader("💡 Key Insights")

st.info(
    f"""
    **Fuel:** {filtered_df['Fuel_Type'].mode()[0]} is the most common fuel type.

    **Body Type:** {filtered_df['Body_Type'].mode()[0]} is the most common body type.

    **Average Price:** {filtered_df['Selling_Price'].mean():,.0f}

    **Average Mileage:** {filtered_df['Mileage'].mean():,.0f}
    """
)


st.markdown("""
<hr>

<div style="text-align:center; color:#8B949E; padding:20px;">
Automobile Analytics Dashboard • Built with Python, Pandas, Plotly & Streamlit
</div>
""", unsafe_allow_html=True)