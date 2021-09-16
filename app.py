from mri_personality.data import clean_data, get_data
from sklearn.preprocessing import StandardScaler
import streamlit as st
import numpy as np
import pandas as pd
import pickle
import statsmodels.api as sm
import plotly.graph_objects as go
import base64


st.set_page_config(
            page_title="Personality Cortex", # => Quick reference - Streamlit
            page_icon="🐍",
            layout="centered", # wide
            initial_sidebar_state="auto") # collapsed
'''
# Personality Cortex
'''
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
.stApp {
  background-image: url("data:image/png;base64,%s");
  background-size: cover;
}
</style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

set_background('notebooks/cover2.jpeg')


st.sidebar.title('LW Batch 602 London')
st.sidebar.subheader('Christopher Holmes, Francisco Costa, Luke Vano')
st.sidebar.markdown('Project explores different models to predict big 5 personality types based on brain thickness')
st.markdown('##')
st.markdown('##')
st.markdown('##')


wiki_link='[Wikipedia](https://en.wikipedia.org/wiki/Big_Five_personality_traits)'
st.sidebar.markdown('What are the Big 5 personality traits?')
st.sidebar.markdown(wiki_link, unsafe_allow_html=True)
data_link = '[Nilab Amsterdam](https://nilab-uva.github.io/AOMIC.github.io/)'
st.sidebar.markdown('Data Source:')
st.sidebar.markdown(data_link, unsafe_allow_html=True)
source_link = '[Oxford University Press](https://pubmed.ncbi.nlm.nih.gov/28122961/)'
st.sidebar.markdown('Neuroanatomy basis for Big 5 personalities:')
st.sidebar.markdown(source_link, unsafe_allow_html=True)
python_link = '[NeuroImg - Python](https://nipy.org/nibabel/reference/nibabel.freesurfer.html#nibabel.freesurfer.io.read_geometry/)'
st.sidebar.markdown('Library for neuro imaging files:')
st.sidebar.markdown(python_link, unsafe_allow_html=True)
keras_link = '[Keras - 3D Image Classification](https://keras.io/examples/vision/3D_image_classification/)'
st.sidebar.markdown('Code example for 3D Images from Keras:')
st.sidebar.markdown(keras_link, unsafe_allow_html=True)

st.text('Curious about what type of personality do you have?')

st.set_option('deprecation.showfileUploaderEncoding', False)
#col1, col2 = st.columns([4, 4])

st.markdown('No MRI? No problem. First insert your parameters.')

sex= st.selectbox('Insert your sex', ('Male', 'Female'))


uploaded_csv=st.file_uploader("Upload the CSV file", type="xlsx")


st.markdown('Do you have an MRI? Upload the **NII image** and see the prediction.')

uploaded_image=st.file_uploader("Upload an MRI", type="JPG")


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
        #uploaded_df.drop(['participant_id','age','sex','BMI','handedness','education_category','NEO_N','NEO_E','NEO_O','NEO_A',
         #                 'NEO_C','eTIV.1', 'EstimatedTotalIntraCranialVol', 'BrainSegVolNotVent.2',
          #               'BrainSegVolNotVent.1', 'BrainSegVolNotVentSurf', 'SupraTentorialVolNotVentVox',
    #'lhCerebralWhiteMatterVol', 'rhCerebralWhiteMatterVol', 'BrainSegVolNotVent.2', 
    #'BrainSegVol', 'SupraTentorialVol', 'SupraTentorialVolNotVent',
    #'BrainSegVol-to-eTIV', 'MaskVol', 'rhCortexVol', 'lhCortexVol', 'Left-WM-hypointensities',
    #'Right-WM-hypointensities', 'non-WM-hypointensities', 'Left-non-WM-hypointensities',
    #'Right-non-WM-hypointensities'],axis=1,inplace=True)
        uploaded_df=pd.DataFrame(scaler.fit_transform(uploaded_df),columns=uploaded_df.columns)
        uploaded_df=sm.add_constant(uploaded_df)
        
        m_knn_0_results=m_knn_0.predict(uploaded_df.values.T.reshape(1,-1))
        m_knn_1_results=m_knn_1.predict(uploaded_df.values.T.reshape(1,-1))
        m_knn_2_results=m_knn_2.predict(uploaded_df.values.T.reshape(1,-1))
        m_knn_3_results=m_knn_3.predict(uploaded_df.values.T.reshape(1,-1))
        m_knn_4_results=m_knn_4.predict(uploaded_df.values.T.reshape(1,-1))
        
        # This is the proba that they fall in each category
        m_knn_proba = pd.DataFrame({'Leader': m_knn_0_results,
                            'Task oriented': m_knn_1_results,
                            'Maverick': m_knn_2_results,
                            'Anxious': m_knn_3_results,
                            'Workaholic': m_knn_4_results})
        results={'Leader': 'You are levelheaded in the face of adversity. You are openminded and can think outside the box. When working in a team you get on well with others. You are organised and like to be around others'
                 ,'Task oriented': 'You are extremely calm, cool, and collected. Like to be around others but sometimes find it difficult to see their point of view. You are very closeminded and like to stick to a plan or structure rather than thinking outside of the box.'
                 ,'Maverick': 'You play by your own rules and don’t care what others think about you. When completing tasks you find it difficult to be organised but are able to rise to unforeseen challenges. You are passionate but sometimes your emotions make it difficult for you to think clearly.'
                 ,'Anxious':'You are stressed most of the time and prefer your own company than being with others. When working with others you often let others take charge and find it difficult to get your point across.'
                 ,'Workaholic':'Are hardworking but aloof, finding it difficult to take on board other people’s point of view. You are a perfectionist who finds it difficult to break the rules.'}
        # This is the category they are highest in
        
        fig = go.Figure(data=go.Scatterpolar(
        r=m_knn_proba.values[0],
        theta=m_knn_proba.columns.tolist(),
        fill='toself'))
        fig.update_layout(
         polar=dict(
        radialaxis=dict(
        visible=True),),
        showlegend=False)

        st.plotly_chart(fig)
        
        st.markdown(results[m_knn_proba.idxmax(axis = 1, skipna = True).values[0]])

        
        
    if sex == 'Female':
        #uploaded_df=uploaded_df[uploaded_df['sex']=='']
        #uploaded_df.drop(['participant_id','age','sex','BMI','handedness','education_category','NEO_N','NEO_E','NEO_O','NEO_A',
        #                  'NEO_C','eTIV.1', 'EstimatedTotalIntraCranialVol', 'BrainSegVolNotVent.2',
         #                'BrainSegVolNotVent.1', 'BrainSegVolNotVentSurf', 'SupraTentorialVolNotVentVox',
    #'lhCerebralWhiteMatterVol', 'rhCerebralWhiteMatterVol', 'BrainSegVolNotVent.2', 
    #'BrainSegVol', 'SupraTentorialVol', 'SupraTentorialVolNotVent',
    #'BrainSegVol-to-eTIV', 'MaskVol', 'rhCortexVol', 'lhCortexVol', 'Left-WM-hypointensities',
    #'Right-WM-hypointensities', 'non-WM-hypointensities', 'Left-non-WM-hypointensities',
    #'Right-non-WM-hypointensities'],axis=1,inplace=True)
        uploaded_df=pd.DataFrame(scaler.fit_transform(uploaded_df),columns=uploaded_df.columns)
        uploaded_df=sm.add_constant(uploaded_df)
        f_knn_0_results=f_knn_0.predict(uploaded_df.iloc[0,:].values.T.reshape(1,-1))
        f_knn_1_results=f_knn_1.predict(uploaded_df.iloc[0,:].values.T.reshape(1,-1))
        f_knn_2_results=f_knn_2.predict(uploaded_df.iloc[0,:].values.T.reshape(1,-1))
        f_knn_3_results=f_knn_3.predict(uploaded_df.iloc[0,:].values.T.reshape(1,-1))
        f_knn_4_results=f_knn_4.predict(uploaded_df.iloc[0,:].values.T.reshape(1,-1))
        
        # This is the proba that they fall in each category
        f_knn_proba = pd.DataFrame({'Leader': f_knn_0_results,
                            'Task oriented': f_knn_1_results,
                            'Maverick': f_knn_2_results,
                            'Anxious': f_knn_3_results,
                            'Workaholic': f_knn_4_results})
        results={'Leader': 'You are levelheaded in the face of adversity. You are openminded and can think outside the box. When working in a team you get on well with others. You are organised and like to be around others'
                 ,'Task oriented': 'You are extremely calm, cool, and collected. Like to be around others but sometimes find it difficult to see their point of view. You are very closeminded and like to stick to a plan or structure rather than thinking outside of the box.'
                 ,'Maverick': 'You play by your own rules and don’t care what others think about you. When completing tasks you find it difficult to be organised but are able to rise to unforeseen challenges. You are passionate but sometimes your emotions make it difficult for you to think clearly.'
                 ,'Anxious':'You are stressed most of the time and prefer your own company than being with others. When working with others you often let others take charge and find it difficult to get your point across.'
                 ,'Workaholic':'Are hardworking but aloof, finding it difficult to take on board other people’s point of view. You are a perfectionist who finds it difficult to break the rules.'}
        # This is the proba that they fall in each category
        fig = go.Figure(data=go.Scatterpolar(
        r=f_knn_proba.values[0],
        theta=f_knn_proba.columns.tolist(),
        fill='toself'))
        fig.update_layout(
         polar=dict(
        radialaxis=dict(
        visible=True),),
        showlegend=False)

        st.plotly_chart(fig)
        
        st.markdown(results[f_knn_proba.idxmax(axis = 1, skipna = True).values[0]])
    
elif uploaded_image!=None:
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
    uploaded_df=pd.read_excel('mri_personality/data/master_combined.xlsx')
    
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
                            'Task oriented': m_knn_1_results,
                            'Maverick': m_knn_2_results,
                            'Anxious': m_knn_3_results,
                            'Workaholic': m_knn_4_results})
        results={'Leader': 'You are levelheaded in the face of adversity. You are openminded and can think outside the box. When working in a team you get on well with others. You are organised and like to be around others'
                 ,'Task oriented': 'You are extremely calm, cool, and collected. Like to be around others but sometimes find it difficult to see their point of view. You are very closeminded and like to stick to a plan or structure rather than thinking outside of the box.'
                 ,'Maverick': 'You play by your own rules and don’t care what others think about you. When completing tasks you find it difficult to be organised but are able to rise to unforeseen challenges. You are passionate but sometimes your emotions make it difficult for you to think clearly.'
                 ,'Anxious':'You are stressed most of the time and prefer your own company than being with others. When working with others you often let others take charge and find it difficult to get your point across.'
                 ,'Workaholic':'Are hardworking but aloof, finding it difficult to take on board other people’s point of view. You are a perfectionist who finds it difficult to break the rules.'}
        # This is the category they are highest in
        
        fig = go.Figure(data=go.Scatterpolar(
        r=m_knn_proba.values[0],
        theta=m_knn_proba.columns.tolist(),
        fill='toself'))
        fig.update_layout(
         polar=dict(
        radialaxis=dict(
        visible=True),),
        showlegend=False)

        st.plotly_chart(fig)
        
        st.markdown(results[m_knn_proba.idxmax(axis = 1, skipna = True).values[0]])

        
        
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
        f_knn_0_results=f_knn_0.predict(uploaded_df.iloc[0,:].values.T.reshape(1,-1))
        f_knn_1_results=f_knn_1.predict(uploaded_df.iloc[0,:].values.T.reshape(1,-1))
        f_knn_2_results=f_knn_2.predict(uploaded_df.iloc[0,:].values.T.reshape(1,-1))
        f_knn_3_results=f_knn_3.predict(uploaded_df.iloc[0,:].values.T.reshape(1,-1))
        f_knn_4_results=f_knn_4.predict(uploaded_df.iloc[0,:].values.T.reshape(1,-1))
        
        # This is the proba that they fall in each category
        f_knn_proba = pd.DataFrame({'Leader': f_knn_0_results,
                            'Task oriented': f_knn_1_results,
                            'Maverick': f_knn_2_results,
                            'Anxious': f_knn_3_results,
                            'Workaholic': f_knn_4_results})
        results={'Leader': 'You are levelheaded in the face of adversity. You are openminded and can think outside the box. When working in a team you get on well with others. You are organised and like to be around others'
                 ,'Task oriented': 'You are extremely calm, cool, and collected. Like to be around others but sometimes find it difficult to see their point of view. You are very closeminded and like to stick to a plan or structure rather than thinking outside of the box.'
                 ,'Maverick': 'You play by your own rules and don’t care what others think about you. When completing tasks you find it difficult to be organised but are able to rise to unforeseen challenges. You are passionate but sometimes your emotions make it difficult for you to think clearly.'
                 ,'Anxious':'You are stressed most of the time and prefer your own company than being with others. When working with others you often let others take charge and find it difficult to get your point across.'
                 ,'Workaholic':'Are hardworking but aloof, finding it difficult to take on board other people’s point of view. You are a perfectionist who finds it difficult to break the rules.'}
        # This is the proba that they fall in each category
        fig = go.Figure(data=go.Scatterpolar(
        r=f_knn_proba.values[0],
        theta=f_knn_proba.columns.tolist(),
        fill='toself'))
        fig.update_layout(
         polar=dict(
        radialaxis=dict(
        visible=True),),
        showlegend=False)

        st.plotly_chart(fig)
        
        st.markdown(results[f_knn_proba.idxmax(axis = 1, skipna = True).values[0]])
    



    
