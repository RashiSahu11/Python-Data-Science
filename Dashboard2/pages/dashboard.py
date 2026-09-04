import streamlit as st # cd dashboard2
import pandas as pd    #python -m streamlit run home.py
import seaborn as sns
import plotly.express as px

#DATASET PREVEIW
df=sns.load_dataset('titanic')

st.title("Explore the insights here")

#FILTER CONNECTIVITY
df['passenger class']=df['pclass']

#SIDE BAR
st.sidebar.title("PASSENGER CLASS")
selected=st.sidebar.multiselect(
    'select',
    options =df['pclass'],
    default =df['pclass']
)
filtered_df=df[df['passenger class'] .isin (selected)]


#KPI CARDS
col1,col2=st.columns(2)

col1.metric=(
    "Average Fare %",
    round(filtered_df['fare'].mean()),'%'
)

col2.metric=( 
    "Average age %",
    round(filtered_df['age'].mean()),'%'
)


st.dataframe(filtered_df)

#GRAPH CONNECTIVITY
tit=px.bar(df,x='embark_town',y='alive',
           title='embarked which are alive',
           labels={'embark_town':'embarked','alive':'on earth'}
           ,color='embark_town',template='plotly_dark' )
st.plotly_chart(tit)


tits=px.bar(df,x='age',y='fare',
              title='fare according to age',
              labels={'age':'age of passenger','fare':'accordingly'})
st.plotly_chart(tits)


tit2=px.bar(df,x='alive',y='who',
             title='whom are alived',
             labels={'alive':'onearth','who':'gender'},
             template='plotly_dark')
st.plotly_chart(tit2)


tat=px.pie(df,values='fare',names='alive',
           title='Alived people',
           labels={'fare':'money','alive':'on earth'},
           template='plotly_dark',
           color_discrete_sequence=px.colors.sequential.Blackbody_r,
           height=500,width=500)
tat.update_traces(textposition='inside')
st.plotly_chart(tat)


scattering=px.scatter(df,x='fare',y='age',
                      template='plotly_dark',
                    title='fare ploted on bases of age',
                    color='age',size='fare')
st.plotly_chart(scattering)


fig_hist = px.histogram(
    df, 
    x='age', 
    color='survived',
    barmode='overlay',
    title='Age Distribution by Survival Status',
    labels={'survived': 'Survived '},template='plotly_dark'
)
st.plotly_chart(fig_hist)


fighis=px.histogram(df,
                    x='age',y='fare',color='survived',
                    barmode='overlay',
                    title='Histogram of age and fare',
                    color_discrete_sequence=px.colors.sequential.PuBuGn_r,
                    template='plotly_dark'
                )
st.plotly_chart(fighis)


scattered=px.scatter(df,
                     x='age',y='fare',
                     title='AGE BY GENDER',
                     labels={'age':'AGE','survived':'GENDER'},
                     color_discrete_sequence=px.colors.sequential.algae_r,
                    
                     )
st.plotly_chart(scattered)


BAR=px.bar(df,
           x='embarked',y='deck',
           title='BAR CHART OF EMBARKED AND DECK',
           labels={'embarked':'PLACES','deck':'DECK'},
           template='plotly_dark',color_discrete_sequence=px.colors.sequential.Cividis)
st.plotly_chart(BAR)


LINE=px.bar(df,
             x='class',y='who',
             labels={'class':'CLASS','who':'WHO'},
             title='CLASSES FOR WHO',
             color_discrete_sequence=px.colors.sequential.matter_r)
st.plotly_chart(LINE)


#COLUMNS
col1,col2=st.columns(2)

with col1:
    pies=px.pie(df,
            values='sibsp',names='fare',
            labels={'sibsp':'SIBSP','fare':'FARE'},
            template='plotly_dark',color_discrete_sequence=px.colors.sequential.Darkmint
            )
pies.update_traces(textposition='inside')
st.plotly_chart(pies)

with col2:
     
     his=px.histogram(df,
                 x='sex',y='pclass',
                 title='SURVIVAL COUNT',
                 labels={'sex':'SEX','pclass':'passenger count'},
                 color='survived',
                 template='plotly_dark')
     st.plotly_chart(his)


bar=px.bar(df,
           x='age',y='pclass',
           title='survival count on the basis of age and pclass',
           labels={'age':'AGE','pclass':'PASSENGER CLASS'},
           template='plotly_dark',
           color='survived')
st.plotly_chart(bar)


his=px.histogram(df,
                 x='class',
                 color='survived',
                 title='survival count on the basis of class',
                 labels={'class':'CLASS'},
                 template='plotly_dark'
                 )
st.plotly_chart(his)


his=px.histogram(df,
                 x='age',
                 color_discrete_sequence=px.colors.sequential.Brwnyl_r,
                 template='plotly_dark',nbins=30)
st.plotly_chart(his)


scatter=px.scatter(df,
                   x='age',y='fare',
                   color='survived',title='survival on the age and fare',
                   template='plotly_dark',color_discrete_sequence=px.colors.sequential.BuGn_r
                          )
st.plotly_chart(scatter)