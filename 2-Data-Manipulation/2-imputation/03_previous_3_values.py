import pandas as pd
data = {
    'A': [None, 2, None, 4, 5, 6, None, 7, 8, 9, 5, None, 10,None],
}
df = pd.DataFrame(data)
print(df)
for col in df.columns:
    for idx in df[df[col].isnull()].index:
        prev_values = df[col].iloc[max(0, idx - 3):idx].dropna()
        
        if idx == 0:
            df.at[idx, col] = df[col].bfill().iloc[idx]  
        elif len(prev_values) >= 3:
            df.at[idx, col] = prev_values.mean()
        else:
            df.at[idx, col] = df[col].ffill().iloc[idx]
            
print('--------------------------------')
print(df)
