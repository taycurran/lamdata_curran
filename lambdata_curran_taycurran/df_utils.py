"""
Some utility functions for working with dataframes
"""

import pandas as pd

TEST_DF = pd.DataFrame([1, 2, 3])

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