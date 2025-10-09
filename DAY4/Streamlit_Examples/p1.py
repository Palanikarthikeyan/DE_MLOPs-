
import streamlit as st
import pandas as pd
import numpy as np

st.title('Welcome to streamlit learning')
st.write('this is test message')

df = pd.DataFrame({'pid':[101,102,130],'pname':['pA','pB','pC']})
st.write(df)

df1 = pd.DataFrame(np.random.randn(20,3),columns=['A','B','C'])
st.write(df1)