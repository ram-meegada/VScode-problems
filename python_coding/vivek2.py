import openpyxl

filename = 'Book2.xlsx'  # Replace with the actual path to your Excel file
workbook = openpyxl.load_workbook(filename)
sheet = workbook.active

# Initialize a dictionary to store the grouped data
grouped_data = {"Global": [], "Folder scope": [], "File scope": []}

# Iterate over rows and group data based on the specified columns
for row in sheet.iter_rows(min_row=1, values_only=True):
    global_value, folder_scope_value, file_scope_value = row[1], row[5], row[2]

    if global_value:
        grouped_data["Global"].append(global_value)

    if folder_scope_value:
        grouped_data["Folder scope"].append(folder_scope_value)

    if file_scope_value:
        grouped_data["File scope"].append(file_scope_value)

# Print the result
print(grouped_data)
