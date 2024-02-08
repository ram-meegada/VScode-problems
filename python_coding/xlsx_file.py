import pandas as pd

# Read the original Excel file
original_file_path = 'ListofStates.xlsx'
df_original = pd.read_excel(original_file_path)
state_list = df_original['AL'].tolist()
# Select the first five records
# df_first_five = df_original.head(5)

# Specify the path for the new Excel file
# new_file_path = 'ListofStates.xlsx'

# Write the first five records to the new Excel file
# df_first_five.to_excel(new_file_path, index=False)
print(state_list)