import pandas as pd
from openpyxl import load_workbook

def process_data(input_file, output_file):
    # Load data from Excel
    df = pd.read_excel(input_file)
    
    # Data Cleaning and Processing
    df = df.dropna()  # Remove missing values
    df['Processed'] = df['Value'] * 1.1  # Example calculation
    
    # Save to a new Excel file
    df.to_excel(output_file, index=False)
    print(f"Data successfully processed and saved to {output_file}")

# Example usage
if __name__ == "__main__":
    process_data("input_data.xlsx", "output_data.xlsx")
