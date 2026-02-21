import pandas as pd

def test():

    df = pd.read_csv("transformed_crypto_data.csv")

    assert (df['current_price'] > 0).all(), 'invalid current_price detected'
    assert (df['market_cap'] >= 0).all(), 'invalid market_cap detected'
    assert (df['total_volume'] >= 0).all(), 'invalid total_volume detected'
    assert (df['id'].notnull()).all(), 'missing id values found'
    assert (df['id'].is_unique), 'duplicate id values found'
    assert (len(df) > 0), 'no data found in the dataframe'
    
if __name__ == "__main__":
    test()