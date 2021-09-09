FROM python:3.8.6-buster

COPY mri_personality /f_knn_0.pickle
COPY mri_personality /f_knn_1.pickle
COPY mri_personality /f_knn_2.pickle
COPY mri_personality /f_knn_3.pickle
COPY mri_personality /f_knn_4.pickle
COPY mri_personality /m_knn_0.pickle
COPY mri_personality /m_knn_1.pickle
COPY mri_personality /m_knn_2.pickle
COPY mri_personality /m_knn_3.pickle
COPY mri_personality /m_knn_4.pickle

COPY requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD uvicorn api.fast:app --host 0.0.0.0 --port $PORT
