import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px
st.title("AUTOMOBILES🏎️. ݁₊ ⊹ . ݁˖ .")


#data set preview
df=pd.read_csv("automobile_dataset.csv")
st.dataframe(df)


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






#KPI cards
col1,col2,col3=st.columns(3)

col1.metric("Total Cars",len(filtered_df))

col2.metric("Average selling price",round(filtered_df["Selling_Price"].mean(),2))

col3.metric("Average Mileage",round(filtered_df['Mileage'].mean(),2))




#graph connectivity
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





scatter=px.scatter(filtered_df, x='Mileage',
                    y='Selling_Price',
                   title=("MILEAGE AND SELLING PRICE"),
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



year_price=filtered_df.groupby('Year')['Selling_Price'].mean().reset_index()

line=px.line(year_price, x='Year',
             y='Selling_Price',
             labels={'Year':'YEAR','Selling_price':'SELLING PRICE'},
             template='plotly_dark',
             title='SELLING PRICE BY YEAR')

st.plotly_chart(line)

st.caption("This graph shows how the average selling price changes across different years and helps identify price trends over time.")


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



box=px.box(filtered_df,x='Accident_History',
           y='Selling_Price',
           title='Accidental History vs Selling Price',
           template='plotly_dark',
           labels={'Accidental_History':'ACCIDENTAL HISTORY','Selling_Price':'SELLING PRICE'})

st.plotly_chart(box)

st.caption("This graph compares selling prices across different accident history categories and helps understand how accident history may affect vehicle prices.")



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



fig=px.scatter(filtered_df,x='Fuel_Efficiency',
               y='Selling_Price',
               color='Body_Type',
               title='SELLING PRICE VS BODY TYPE',
               labels={'Fuel_Efficiency':'Efficiency of Fuel','Selling_Price':'Selling price'},
               template='plotly_dark')

st.plotly_chart(fig)

st.caption("This scatter plot shows the relationship between fuel efficiency and selling price and allows comparison across different body types.")



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
