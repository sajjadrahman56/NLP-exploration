import pandas as pd

# Create a DataFrame with missing values
data = {
    'A': [1, 2, None, 4, 5,None],
    'B': [None, 2, 3, None, 5,None],
    'C': [1, None, None, 4, None,6]
}
df = pd.DataFrame(data)

# Fill missing values with a specific value
df_filled = df.fillna(0)

# Forward fill
df_ffill = df.ffill()

# Backward fill
df_bfill = df.bfill()

# Interpolation
df_interpolated = df.interpolate()

# print("Original DataFrame:")
# print(df)
# print("\nFilled DataFrame:")
# print(df_filled)
# print("\nForward Filled DataFrame:")
# print(df_ffill)
print("\nBackward Filled DataFrame:")
print(df_bfill)
# print("\nInterpolated DataFrame:")
# print(df_interpolated)