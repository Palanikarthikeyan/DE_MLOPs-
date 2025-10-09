
import streamlit as st
import pandas as pd

st.slider('Select your age:')
st.slider('Select your port rang:',500,550)
st.slider('Select your X value:',15,100,25)

#st.image('C:\\Users\\karth\\OneDrive\\Pictures\\test1.png')
#st.audio()
#st.video()

file = st.file_uploader('select your input file:')

if file is not None:
	df = pd.read_csv(file)
	st.write(df)

st.checkbox('yes')
st.button('Click me')
st.radio('Select your interface:',['eth0','eth1','eth2'])

st.selectbox('select your model:',['gpt4.0','gpt5.0','lamma','gamma'])

st.multiselect('select your file:',['emp.csv','p1.csv','p2.csv'])

st.select_slider('Select your rate:',['Bad','Good','Excellent'])

st.date_input('Travel date:')
