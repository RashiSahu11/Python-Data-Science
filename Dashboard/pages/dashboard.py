import streamlit as st # cd dashboard
import pandas as pd    #python -m streamlit run home.py
import seaborn as sns
import plotly.express as px
st.title("Explore the insight here")

#DATASET PREVIEW
df=sns.load_dataset("Car_crashes")



#FILTER CONNECTIVITY
df['State']=df['abbrev']

#Side bar
st.sidebar.title("Dashboard Filters")
selected_state=st.sidebar.multiselect(
    'Select State',
    options=df['State'],
    default=df['State']
)
filtered_df=df[df['State'].isin(selected_state)]


#KPI Cards
col1,col2,col3=st.columns(3)

col1.metric(
    'Average accidents %',
    round(filtered_df['total'].mean()),'%'
)

col2.metric(
    'Average speeding %',
    round(filtered_df['speeding'].mean()),'%'
)

col3.metric(
    'Average alcoholic %',
    round(filtered_df['alcohol'].mean()),'%'
)
st.dataframe(filtered_df)


#GRAPH CONNECTIVITY
#total accident by state
figbar=px.bar(filtered_df, x='abbrev', y='total',
               title='State wise total accidents',
               labels={'abbrev':'State','total':'Total State'},
               color='total',template='plotly_dark')
st.plotly_chart(figbar)

figbars=px.bar(filtered_df, x='abbrev', y='total',
               title='State wise total accidents',
               labels={'abbrev':'State','total':'Total State'},
               color='abbrev')
st.plotly_chart(figbars)

#row3
col1,col2=st.columns(2)
with col1:
    figs=figs=px.line(filtered_df,x='abbrev',y='total',
             title ='Statewise total accidents',
             labels={'abbrev':'State','total':'Total State'},
             template='plotly_dark',color_discrete_sequence=px.colors.sequential.Burg)
    st.plotly_chart(figs)    

with col2:
    figpie=figpie=px.pie(filtered_df,values='speeding',
                          names='abbrev')
    st.plotly_chart(figpie)


figpie=px.pie(filtered_df,values='speeding',names='abbrev',
               title='speeding accidents',
               template='plotly_dark',
               color_discrete_sequence=px.colors.sequential.algae_r,
               height=600,width=600)
figpie.update_traces(textposition='inside')
st.plotly_chart(figpie) 


top10=df.sort_values('ins_premium',ascending=False).head(10)   
bar=px.bar(top10,x='abbrev',y='ins_premium',
           title='Ins premium',color='abbrev',template='plotly_dark')
st.plotly_chart(bar)



scatter=px.scatter(filtered_df,x='speeding',y='alcohol',
                    color='speeding',size='total',
                    template='plotly_dark')
st.plotly_chart(scatter)                                      
