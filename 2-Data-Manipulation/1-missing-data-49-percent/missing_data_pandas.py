import pandas as pd

data = {
    'id': [1, 2, None, 4, 5, 6, 7, 8, 9, None],
    'scroe': [10, 20, 30, None, None, 70, 80, None, None, None],
    'name': ['a', 'b', None, None, None, None, 'h', 'i', 'j', None]
}

df = pd.DataFrame(data)

def percent_missing(col):
    no_row = len(col)
    total_missing_values = col.isnull().sum()
    missing_percentage = (total_missing_values / no_row) * 100

    print(f'column "{col.name}" = {missing_percentage}%')
    
    if missing_percentage >= 49:
        print(f'Dropping column "{col.name}"')
        return col.name  #
    return None  


drop_columns = df.apply(percent_missing, axis=0)

df_cleaned = drop_columns.dropna() #columns_to_drop = [col for col in df.apply(percent_missing, axis=0) if col is not None]

df.drop(columns=df_cleaned, inplace=True)

print("\nCleaned DataFrame:")
print(df)
