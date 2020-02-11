"""
Some utility functions for working with dataframes
"""

import pandas as pd

TEST_DF = pd.DataFrame([1, 2, 3])

def cardinality_report(df):
    """
    Takes a dataframe and returns a report on the cardinality
    of categorical columns within the dataframe

    Params:
        df (pandas DataFrame)
    
    Returns:
        A series of 5 Print Statements for each Categorical Column
        identified in the dataframe separated by a newline
    """
    # Get only categorical features from DF
    columns = df.describe(exclude='number').columns
    # Evaluate cardinality qualities for each feature
    for col in columns:
        print(f"COLUMN: {col}")
        print(f"nUnique: {df[col].nunique()}")
        print(f"Perc Uniq: {df[col].nunique() / df.shape[0]}")
        print("TOP 5")
        print(df[col].value_counts().nlargest(5))
        print('\n')


def check_facts(df):
    """
    Checks basic facts about an entire dataframe.
    Returns series of print statements.
    """
    print(f"Shape: {df.shape}")
    print(f"PercNull: {df.isna().sum().sum()/df.size}")



# TODO: Make Funct work for Multiple Datatypes
 def check_mask(df, target, method='contains'):

    if target == 

    for feature in df.columns:
        
        if method == 'exact':
            condition = df[feature] == (target)
        if method == 'isin':
            condition = df[feature].str.isin(target)
        if method == 'contains':
            condition = df[feature].str.contains(target)
        else:
            except("method must be 'exact', 'isin', or 'contains'")
    
        print(feature)
        print(condition.sum())
        print()

    