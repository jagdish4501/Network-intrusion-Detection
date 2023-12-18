import pandas as pd

# Assuming df is your DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
})

# Convert DataFrame to NumPy array
array_data = df.values

# Print the resulting array
print(array_data)
