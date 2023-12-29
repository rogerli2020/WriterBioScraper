import pandas as pd

# Load the CSV file into a pandas DataFrame
file_path = './assets/final_data.csv'
df = pd.read_csv(file_path)

# Calculate the total count for each outlet
outlet_counts = df['outlet'].value_counts()

# Create a DataFrame with outlet names and their corresponding counts
top_outlets = pd.DataFrame({'outlet': outlet_counts.index, 'count': outlet_counts.values})

# Add a "total_count" column
top_outlets['total_count'] = top_outlets['outlet'].map(outlet_counts)

# Save all outlets to a new CSV file
output_path = './assets/all_outlets.csv'
top_outlets.to_csv(output_path, index=False)

# Display the result
print(top_outlets)
print(f'All outlets saved to {output_path}')
