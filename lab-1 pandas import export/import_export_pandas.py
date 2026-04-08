import pandas as pd

# Create a sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}
df = pd.DataFrame(data)

# Display the DataFrame
print('Original DataFrame:')
print(df)

# Export DataFrame to CSV
csv_file = 'sample_data.csv'
df.to_csv(csv_file, index=False)
print(f'\nData exported to CSV file: {csv_file}')

# Export DataFrame to Excel
excel_file = 'sample_data.xlsx'
df.to_excel(excel_file, index=False)
print(f'Data exported to Excel file: {excel_file}')

# Export DataFrame to JSON
json_file = 'sample_data.json'
df.to_json(json_file, orient='records', lines=False)
print(f'Data exported to JSON file: {json_file}')

# Import data back from CSV
imported_csv = pd.read_csv(csv_file)
print('\nData imported from CSV:')
print(imported_csv)

# Import data back from Excel
imported_excel = pd.read_excel(excel_file)
print('\nData imported from Excel:')
print(imported_excel)

# Import data back from JSON
imported_json = pd.read_json(json_file)
print('\nData imported from JSON:')
print(imported_json)
