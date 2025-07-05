import pandas as pd

def preprocess_input(df):
    substance_map = {'carbon dioxide': 0, 'methane': 1, 'nitrous oxide': 2, 'other GHGs': 3}
    unit_map = {'kg/2018 USD, purchaser price': 0, 'kg CO2e/2018 USD, purchaser price': 1}
    source_map = {'Commodity': 0, 'Industry': 1}

    df['Substance'] = df['Substance'].map(substance_map)
    df['Unit'] = df['Unit'].map(unit_map)
    df['Source'] = df['Source'].map(source_map)
    return df