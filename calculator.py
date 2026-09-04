#pip install streamlit
#to run : python -m streamlit run calculator .py
import streamlit as st

st.title("Streamlit Calculator")
st.subheader ("this is a simple calculator app built with streamlit")# larger 
st.markdown("This is a simple calculator app built with Streamlit.")# smaller

c1,c2=st.columns(2)
fnum=c1.number_input("Enter first number",value=0)
snum=c2.number_input("Enter second number",value=0)

options=['Addition','Subtraction','Multiplication','Division']
choice=st.radio("Select an operation",options)

button=st.button('Calculate')

result=0
if button:
    if choice=='Addition':
        result=fnum+snum
    if choice=='Subtraction':
        result=fnum-snum
    if choice=='Multiplication': 
        result=fnum*snum
    if choice=='Division':
        result=fnum/snum
st.success ("Result:"+str(result))

st.balloons()
st.snow()
           