import streamlit as st
import io
import matplotlib.pyplot as plt
import pandas as pd
import pickle


st.set_page_config(
            page_title="Personality Cortex", # => Quick reference - Streamlit
            page_icon="🐍",
            layout="centered", # wide
            initial_sidebar_state="auto") # collapsed
'''
# Personality Cortex
'''

st.text('Curious about what type of personality you have?')

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

if uploaded_csv!=None:
    f_knn_0=pickle.load(open('f_knn_0.pickle', 'rb'))
    f_knn_1=pickle.load(open('f_knn_1.pickle', 'rb'))
    f_knn_2=pickle.load(open('f_knn_2.pickle', 'rb'))
    f_knn_3=pickle.load(open('f_knn_3.pickle', 'rb'))
    f_knn_4=pickle.load(open('f_knn_4.pickle', 'rb'))
    m_knn_0=pickle.load(open('m_knn_0.pickle', 'rb'))
    m_knn_1=pickle.load(open('m_knn_1.pickle', 'rb'))
    m_knn_2=pickle.load(open('m_knn_2.pickle', 'rb'))
    m_knn_3=pickle.load(open('m_knn_3.pickle', 'rb'))
    m_knn_4=pickle.load(open('m_knn_4.pickle', 'rb'))
    uploaded_df=pd.read_csv(uploaded_csv)
    f_knn_0_results=f_knn_0.predict(uploaded_df)
    f_knn_1_results=f_knn_1.predict(uploaded_df)    
    f_knn_2_results=f_knn_2.predict(uploaded_df)
    f_knn_3_results=f_knn_3.predict(uploaded_df)
    f_knn_4_results=f_knn_4.predict(uploaded_df)
    st.text(f_knn_0_results)
    
else:
    st.text('Here we should see the CNN prediction')



    
