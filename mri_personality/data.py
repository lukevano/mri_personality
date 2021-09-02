import pandas as pd

def get_data():
    
    # Get the raw data from the excel sheet
    df = pd.read_excel('data/master_combined.xlsx')
    
    return df

def clean_data(df):
    
    # Specify columns to remove
    to_remove = ['eTIV.1', 'EstimatedTotalIntraCranialVol', 'BrainSegVolNotVent.2',
    'BrainSegVolNotVent.1', 'BrainSegVolNotVentSurf', 'SupraTentorialVolNotVentVox',
    'lhCerebralWhiteMatterVol', 'rhCerebralWhiteMatterVol', 'BrainSegVolNotVent.2', 
    'BrainSegVol', 'SupraTentorialVol', 'SupraTentorialVolNotVent',
    'BrainSegVol-to-eTIV', 'MaskVol', 'rhCortexVol', 'lhCortexVol', 'Left-WM-hypointensities',
    'Right-WM-hypointensities', 'non-WM-hypointensities', 'Left-non-WM-hypointensities',
    'Right-non-WM-hypointensities']
    
    # Drop the identical columns
    drop_col_df = df.drop(columns=to_remove)
    # Drop the row with nan in NEO_C
    cleaned_df = drop_col_df[drop_col_df.NEO_C.notnull()].reset_index(drop=True)
    
    # Remove the row with no sex data
    sex_df = cleaned_df[cleaned_df.sex.notnull()]
    
    # Replace male and female with M and F respectively
    sex_df.sex.replace('female', 'F', inplace=True)
    sex_df.sex.replace('male', 'M', inplace=True)
    
    # Make male and female df
    f_df = sex_df[sex_df.sex=='F']
    m_df = sex_df[sex_df.sex=='M']
    
    # Keep only the volume and thickness data
    X_f = f_df.iloc[:,11:].reset_index(drop=True)
    X_m = m_df.iloc[:,11:].reset_index(drop=True)
    
    # Create NEO_FF targets
    neo_f = f_df.iloc[:,6:11].reset_index(drop=True)
    neo_m = m_df.iloc[:,6:11].reset_index(drop=True)
    
    return X_f, X_m, neo_f, neo_m, sex_df

if __name__ == '__main__':
    
    df = get_data()
    X_f, X_m, neo_f, neo_m, sex_df = clean_data(df)
