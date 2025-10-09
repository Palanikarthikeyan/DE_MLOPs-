
import streamlit as st
import pandas as pd
import numpy as np

st.title('Welcome to streamlit learning')

st.write('Hello..userA')

model = st.text_input('Enter a model name:')

if model:
	st.write(f'input model name is:{model}')

port = st.slider('Select your port range:',5000,6000,6500)

if port:
	st.write(f'Selected port number:{port}')

d={}
d['pname']=['pA','pB','pC']
d['dept']=['sales','prod','qa']
d['city']=['City-1','City-2','City-3']

st.selectbox('Select your data:',d)


