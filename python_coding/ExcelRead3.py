import openpyxl
import pandas as pd 

def process_rows(filename, target_file_name):
    content = pd.read_excel(filename, engine='openpyxl')
    print(content, '-----content--------')
    result = []
    workbook = openpyxl.load_workbook(filename)
    sheet = workbook.active
    merged_cells = sheet.merged_cells
    
    # is_target_file_name = False
    count = 0
    current_row_values = []
    for row in sheet.iter_rows(min_row=1):  # Include the header row     
        if row[0].value is not None and count == 1:
            return result
        if row[0].value == target_file_name:
            is_target_file_name = True
            # Process the first row immediately here
            current_row_values = [cell.value.strip() for cell in row[1:] if cell.value]  # Accumulate values
            if any(current_row_values):  # Check if any values are present
                output = "_".join(current_row_values)
                result.append(output)
                count = 1    
        elif row[0].value is None and count == 1:
            current_row_values = [cell.value.strip() for cell in row[1:] if cell.value]  # Accumulate values
            if any(current_row_values):  # Check if any values are present
                output = "_".join(current_row_values)
                result.append(output)
    return result                     
 
if __name__ == "__main__":
    filename = r"Book1.xlsx"  # Replace with your actual file name
    # target_file_name = input("Enter the target file name: ")
    target_file_name = "Swc_SoCCtrl_MainController"
    x = process_rows(filename, target_file_name)
    print(x)
