from data import *
from termcolor import colored
import pandas as pd
import statsmodels.api as sm
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

class Trainer(object):
    
    def __init__(self, X_f, X_m, neo_f, neo_m, sex_df):
        
        self.pipeline = None
        self.X_f = X_f
        self.X_m = X_m
        self.neo_f = neo_f
        self.neo_m = neo_m
        self.sex_df = sex_df
        
    def preprocessing(self):
        
        # Normalise features
        scaler = StandardScaler()
        X_f_scaled = scaler.fit_transform(self.X_f)
        X_m_scaled = scaler.fit_transform(self.X_m)

        # Add a constant as a feature to the scaled X
        X_f_scaled_int = sm.add_constant(X_f_scaled)
        self.X_f_scaled_int = pd.DataFrame(X_f_scaled_int, 
                                        columns=pd.Index(['const']).append(self.X_f.columns))

        X_m_scaled_int = sm.add_constant(X_m_scaled)
        self.X_m_scaled_int = pd.DataFrame(X_m_scaled_int, 
                                        columns=pd.Index(['const']).append(self.X_f.columns))
        
        # Target creation- first select target columns
        self.y_sex = self.sex_df.iloc[:, 6:11]
        
        # Use KMeans clustering to generate new targets- create the model
        clusters = KMeans(n_clusters=5, random_state=0)
        
        # Scale the targets then generate 5 clusters using KNN
        y_scaled = pd.DataFrame(scaler.fit_transform(self.y_sex), columns=self.y_sex.columns)
        clusters.fit_transform(y_scaled)
        knn_label = clusters.labels_
        
        # Create add a column that adds the created target to the observation
        self.sex_df['knn_label'] = knn_label

        # Make female and male targets with this dataframe
        f_target_df = self.sex_df[self.sex_df.sex=='F'].reset_index(drop=True)
        m_target_df = self.sex_df[self.sex_df.sex=='M'].reset_index(drop=True)
        self.y_f_knn = f_target_df.knn_label
        self.y_m_knn = m_target_df.knn_label
    
    def run(self):
        
        # Fit the models for each created target
        self.results_f_knn_0 = sm.Logit(self.y_f_knn==0, self.X_f_scaled_int).fit(maxiter=100)
        self.results_f_knn_1 = sm.Logit(self.y_f_knn==1, self.X_f_scaled_int).fit(maxiter=100)
        self.results_f_knn_2 = sm.Logit(self.y_f_knn==2, self.X_f_scaled_int).fit(maxiter=100)
        self.results_f_knn_3 = sm.Logit(self.y_f_knn==3, self.X_f_scaled_int).fit(maxiter=100)
        self.results_f_knn_4 = sm.Logit(self.y_f_knn==4, self.X_f_scaled_int).fit(maxiter=100)
        self.results_m_knn_0 = sm.Logit(self.y_m_knn==0, self.X_m_scaled_int).fit(maxiter=100)
        self.results_m_knn_1 = sm.Logit(self.y_m_knn==1, self.X_m_scaled_int).fit(maxiter=100)
        self.results_m_knn_2 = sm.Logit(self.y_m_knn==2, self.X_m_scaled_int).fit(maxiter=100)
        self.results_m_knn_3 = sm.Logit(self.y_m_knn==3, self.X_m_scaled_int).fit(maxiter=100)
        self.results_m_knn_4 = sm.Logit(self.y_m_knn==4, self.X_m_scaled_int).fit(maxiter=100)
        
    def save_model_locally(self):
        
        # Save a model for each KNN cluster locally
        self.results_f_knn_0.save("f_knn_0.pickle")
        self.results_f_knn_1.save("f_knn_1.pickle")
        self.results_f_knn_2.save("f_knn_2.pickle")
        self.results_f_knn_3.save("f_knn_3.pickle")
        self.results_f_knn_4.save("f_knn_4.pickle")
        self.results_m_knn_0.save("m_knn_0.pickle")
        self.results_m_knn_1.save("m_knn_1.pickle")
        self.results_m_knn_2.save("m_knn_2.pickle")
        self.results_m_knn_3.save("m_knn_3.pickle")
        self.results_m_knn_4.save("m_knn_4.pickle")
        
        print(colored("model.pickle saved locally", "green"))
        
        
if __name__ == "__main__":
    
    # Get and clean data
    df = get_data()
    X_f, X_m, neo_f, neo_m, sex_df = clean_data(df)
    trainer = Trainer(X_f, X_m, neo_f, neo_m, sex_df)
    trainer.preprocessing()
    
    # Train and run the models
    trainer.run()
    
    # Save the models
    trainer.save_model_locally()
