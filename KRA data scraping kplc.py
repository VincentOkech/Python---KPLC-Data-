import pandas as pd

def print_row_values(input_values, filename):
    try:
        # Read the Excel file
        df = pd.read_excel(filename)
        
        # Split the input values by comma and strip extra spaces
        inputs = [x for x in input_values.split(',')]
        
        # Iterate through each row
        for index, row in df.iterrows():
            # Iterate through each column in the row
            for column_name, value in row.items():
                # Check if the value in the column matches any of the input values
                if str(value) in inputs:
                    # Print the row values if input value is found1 
                    print(f"Input '{value}' found in row {index+2}, column '{column_name}': {row.tolist()}")
                    break  # Break out of the loop if input value is found
    
    except Exception as e:
        print("An error occurred:", e)

# Replace 'input_file.xlsx' with the path to your Excel file
filename = r'C:\Users\Vinn\Documents\Python Scripts\Ndata.xlsx'

# Input values separated by comma
input_values = input("Enter input value(s) separated by comma: ")

print_row_values(input_values, filename)
