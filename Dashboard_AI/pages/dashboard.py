import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px
st.title("AUTOMOBILES")


#data set preview
df=pd.read_csv("automobile_dataset.csv")
st.dataframe(df)


#filter connectivity
st.sidebar.title("Automobiles Filters")
selected=st.sidebar.multiselect(
    'Select Make',
    options=df['Make'].unique(),
    default=df['Make'].unique()
)

filtered_df=df[df['Make'].isin(selected)]



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

avg_price = filtered_df.groupby('Make')['Selling_Price'].mean().reset_index()
avg_price.columns = ['Make','Average Price']


bar=px.bar(avg_price,x='Make',
           y='Average Price',
     color='Average Price',template='plotly_dark',
     title='Average Selling Price by Make')

st.plotly_chart(bar)


bar=px.bar(filtered_df, x='Selling_Price',
           y='Make',
                color='Make',
                title='Selling Price Distribution',
                 labels={'Selling_Price':'SELLING PRICE','Make':'MAKE'} ,
                 template='plotly_dark')
st.plotly_chart(bar)


scatter=px.scatter(filtered_df, x='Mileage',
                    y='Selling_Price',
                   title=("MILEAGE AND SELLING PRICE"),
                    color= 'Fuel_Type',
                    template='plotly_dark')

st.plotly_chart(scatter)


scatterr=px.scatter(filtered_df,x='Engine_Size',
                   y='Horsepower',
                   color='Fuel_Type',
                   title="Engine Size vs Horsepower by Fuel Type",
                   template='plotly_dark')

st.plotly_chart(scatterr)

