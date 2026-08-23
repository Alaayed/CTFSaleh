import pandas as pd
from scipy import stats
import numpy as np
def trimmed_average(df, name):
    col = df[name]
    col.sort()

def explanatory_analysis(charges_data_path, personal_data_path, plan_data_path):
    df_charges, df_personal, df_plan = pd.read_csv(charges_data_path), pd.read_csv(personal_data_path), pd.read_csv(plan_data_path)
    # write you solution here
    col = df_charges["monthlyCharges"]
    col.sort_values()
    start, end = round(len(col) * 0.1), round(len(col) * 0.9)
    col[start : end]
    results = {

    }
    return results
