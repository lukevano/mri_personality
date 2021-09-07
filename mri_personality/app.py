import streamlit as st
import io
from typing import List, Optional
import markdown
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import plotly.graph_objects as go
import streamlit as st
from plotly import express as px
from plotly.subplots import make_subplots


st.set_page_config(
            page_title="Personality Cortex", # => Quick reference - Streamlit
            page_icon="🐍",
            layout="centered", # wide
            initial_sidebar_state="auto") # collapsed
'''
# Personality Cortex
'''

st.text('Curious about your what type of personality you have?')

st.set_option('deprecation.showfileUploaderEncoding', False)
#col1, col2 = st.columns([4, 4])

st.markdown('No MRI? No problem. Upload your **CSV file** with all the parameters.')

uploaded_csv=st.file_uploader("Upload the CSV file", type="csv")



st.markdown('Do you have an MRI? Upload the **NII image** and see the prediction.')

uploaded_image=st.file_uploader("Upload an MRI", type="NII")





st.text('')
st.text('')
st.text('')

st.markdown('**Check out your prediction!**')

st.text('Here we should see the prediction')
    
