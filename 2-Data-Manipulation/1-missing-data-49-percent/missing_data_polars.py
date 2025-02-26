import polars as pl

data = {
    'id': [1, 2, None, 4, 5, 6, 7, 8, 9, None],
    'scroe': [10, 20, 30, None, None, 70, 80, None, None, None],
    'name': ['a', 'b', None, None, None, None, 'h', 'i', 'j', None]
}

df = pl.DataFrame(data)

def percent_missing(col):
    no_row = df.height  
    total_missing_values = col.is_null().sum()
    missing_percentage = (total_missing_values / no_row) * 100

    print(f'column "{col.name}" = {missing_percentage}%')
    
    if missing_percentage >= 49:
        print(f'Dropping column "{col.name}"')
        return col.name  
    return None  

drop_columns = [percent_missing(df[col]) for col in df.columns]
drop_columns = [col for col in drop_columns if col is not None]

df = df.drop(drop_columns)

print("\nCleaned DataFrame:")
print(df)
