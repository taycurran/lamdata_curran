"""
lambdata_curran - a collection of datascience helper functions
"""

import pandas as pd
import numpy as np

# sample code
ONES = pd.DataFrame(np.ones(10))
ZEROS = pd.DataFrame(np.zeros(50))

def checkCardinality(df):
    """
    Takes a dataframe and returns a report on the cardinality
    of categorical features within the dataframe
    """
    columns = df.describe(exclude='number').columns
    for col in columns:
        print(f"COLUMN: {col}")
        print(f"nUnique: {df[col].nunique()}")
        print(f"Perc Uniq: {df[col].nunique() / df.shape[0]}")
        print("TOP 5")
        print(df[col].value_counts().nlargest(5))
        print('\n')