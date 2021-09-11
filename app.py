from mri_personality.data import clean_data
from sklearn.preprocessing import StandardScaler
import streamlit as st
import numpy as np
import pandas as pd
import pickle
import statsmodels.api as sm
import plotly.graph_objects as go


st.set_page_config(
            page_title="Personality Cortex", # => Quick reference - Streamlit
            page_icon="🐍",
            layout="centered", # wide
            initial_sidebar_state="auto") # collapsed
'''
# Personality Cortex
'''

st.text('Curious about what type of personality do you have?')

st.set_option('deprecation.showfileUploaderEncoding', False)
#col1, col2 = st.columns([4, 4])

st.markdown('No MRI? No problem. First insert your parameters.')

sex= st.selectbox('Insert your sex', ('Male', 'Female'))

#age= st.text_input('Insert your age')

#bmi= st.text_input('Insert your BMI')

#hand=st.selectbox('What hand do you use?', ('right', 'left','ambidextrous'))

#education=st.selectbox('Insert your level of education', ('applied', 'academic','medium','high','low'))

uploaded_csv=st.file_uploader("Upload the CSV file", type="xlsx")


st.markdown('Do you have an MRI? Upload the **NII image** and see the prediction.')

uploaded_image=st.file_uploader("Upload an MRI", type="NII")





st.text('')
st.text('')
st.text('')

st.markdown('**Check out your prediction!**')

scaler = StandardScaler()

if uploaded_csv!=None:
    f_knn_0=pickle.load(open('mri_personality/f_knn_0.pickle', 'rb'))
    f_knn_1=pickle.load(open('mri_personality/f_knn_1.pickle', 'rb'))
    f_knn_2=pickle.load(open('mri_personality/f_knn_2.pickle', 'rb'))
    f_knn_3=pickle.load(open('mri_personality/f_knn_3.pickle', 'rb'))
    f_knn_4=pickle.load(open('mri_personality/f_knn_4.pickle', 'rb'))
    m_knn_0=pickle.load(open('mri_personality/m_knn_0.pickle', 'rb'))
    m_knn_1=pickle.load(open('mri_personality/m_knn_1.pickle', 'rb'))
    m_knn_2=pickle.load(open('mri_personality/m_knn_2.pickle', 'rb'))
    m_knn_3=pickle.load(open('mri_personality/m_knn_3.pickle', 'rb'))
    m_knn_4=pickle.load(open('mri_personality/m_knn_4.pickle', 'rb'))
    uploaded_df=pd.read_excel(uploaded_csv)
    
    if sex == 'Male':
        #uploaded_df=uploaded_df[uploaded_df['sex']=='']
        uploaded_df.drop(['participant_id','age','sex','BMI','handedness','education_category','NEO_N','NEO_E','NEO_O','NEO_A',
                          'NEO_C','eTIV.1', 'EstimatedTotalIntraCranialVol', 'BrainSegVolNotVent.2',
                         'BrainSegVolNotVent.1', 'BrainSegVolNotVentSurf', 'SupraTentorialVolNotVentVox',
    'lhCerebralWhiteMatterVol', 'rhCerebralWhiteMatterVol', 'BrainSegVolNotVent.2', 
    'BrainSegVol', 'SupraTentorialVol', 'SupraTentorialVolNotVent',
    'BrainSegVol-to-eTIV', 'MaskVol', 'rhCortexVol', 'lhCortexVol', 'Left-WM-hypointensities',
    'Right-WM-hypointensities', 'non-WM-hypointensities', 'Left-non-WM-hypointensities',
    'Right-non-WM-hypointensities'],axis=1,inplace=True)
        uploaded_df=pd.DataFrame(scaler.fit_transform(uploaded_df),columns=uploaded_df.columns)
        uploaded_df=sm.add_constant(uploaded_df)
        
        m_knn_0_results=m_knn_0.predict(uploaded_df.iloc[4,:].values.T.reshape(1,-1))
        m_knn_1_results=m_knn_1.predict(uploaded_df.iloc[4,:].values.T.reshape(1,-1))
        m_knn_2_results=m_knn_2.predict(uploaded_df.iloc[4,:].values.T.reshape(1,-1))
        m_knn_3_results=m_knn_3.predict(uploaded_df.iloc[4,:].values.T.reshape(1,-1))
        m_knn_4_results=m_knn_4.predict(uploaded_df.iloc[4,:].values.T.reshape(1,-1))
        
        # This is the proba that they fall in each category
        m_knn_proba = pd.DataFrame({'Leader': m_knn_0_results,
                            'Task orientatied': m_knn_1_results,
                            'Maverick': m_knn_2_results,
                            'Anxious': m_knn_3_results,
                            'Workaholic': m_knn_4_results})
        results={'Leader': '....','Task': '....'}
        # This is the category they are highest in
        'Results per category:',m_knn_proba
        fig = go.Figure(data=go.Scatterpolar(
        r=m_knn_proba.values,
        theta=m_knn_proba.columns.tolist(),
        fill='toself'))
        fig.update_layout(
         polar=dict(
        radialaxis=dict(
        visible=True),),
        showlegend=False)

        st.plotly_chart(fig)
        st.text(m_knn_proba.values)
        st.text(m_knn_proba.columns.tolist())
        st.text(m_knn_proba.idxmax(axis = 1, skipna = True))

        
        
    if sex == 'Female':
        #uploaded_df=uploaded_df[uploaded_df['sex']=='']
        uploaded_df.drop(['participant_id','age','sex','BMI','handedness','education_category','NEO_N','NEO_E','NEO_O','NEO_A',
                          'NEO_C','eTIV.1', 'EstimatedTotalIntraCranialVol', 'BrainSegVolNotVent.2',
                         'BrainSegVolNotVent.1', 'BrainSegVolNotVentSurf', 'SupraTentorialVolNotVentVox',
    'lhCerebralWhiteMatterVol', 'rhCerebralWhiteMatterVol', 'BrainSegVolNotVent.2', 
    'BrainSegVol', 'SupraTentorialVol', 'SupraTentorialVolNotVent',
    'BrainSegVol-to-eTIV', 'MaskVol', 'rhCortexVol', 'lhCortexVol', 'Left-WM-hypointensities',
    'Right-WM-hypointensities', 'non-WM-hypointensities', 'Left-non-WM-hypointensities',
    'Right-non-WM-hypointensities'],axis=1,inplace=True)
        uploaded_df=pd.DataFrame(scaler.fit_transform(uploaded_df),columns=uploaded_df.columns)
        uploaded_df=sm.add_constant(uploaded_df)
        f_knn_0_results=f_knn_0.predict(uploaded_df.iloc[3,:].values.T.reshape(1,-1))
        f_knn_1_results=f_knn_1.predict(uploaded_df.iloc[3,:].values.T.reshape(1,-1))
        f_knn_2_results=f_knn_2.predict(uploaded_df.iloc[3,:].values.T.reshape(1,-1))
        f_knn_3_results=f_knn_3.predict(uploaded_df.iloc[3,:].values.T.reshape(1,-1))
        f_knn_4_results=f_knn_4.predict(uploaded_df.iloc[3,:].values.T.reshape(1,-1))

        # This is the proba that they fall in each category
        f_knn_proba = pd.DataFrame({'Leader': f_knn_0_results,
                            'Task orientatied': f_knn_1_results,
                            'Maverick': f_knn_2_results,
                            'Anxious': f_knn_3_results,
                            'Workaholic': f_knn_4_results})
        
        category_dict={'Leader': '....','Task orientatied': '....','Maverick': '....','Anxious': '....','Workaholic': '....'}
        # This is the category they are highest in
        'Results per category:',m_knn_proba 
        st.text(m_knn_proba.idxmax(axis = 1, skipna = True))
    
else:
    st.text('Here we should see the CNN prediction')



    
