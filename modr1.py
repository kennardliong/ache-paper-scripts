import csv

smile1 = "COC1=C(C=C2C(=C1)CC(C2=O)CC3CCN(CC3)"
smile2 = ")OC"

# Define the file name
file_name = 'functional_groups.csv'
output_file_name = 'output_file.csv'

with open(file_name, mode='r') as input_file:
    # Create a CSV reader object
    csv_reader = csv.reader(input_file)
    
    # Read the header
    header = next(csv_reader)
    
    # Add a new column name to the header
    header.append('Mods')
    
    # Open the output CSV file
    with open(output_file_name, mode='w', newline='') as output_file:
        # Create a CSV writer object
        csv_writer = csv.writer(output_file)
        
        # Write the updated header to the output file
        csv_writer.writerow(header)
        
        # Iterate through the rows in the input CSV file
        for row in csv_reader:
            # Duplicate the SMILES string in the third column
            row.append(smile1 + row[1] + smile2)
            # Write the updated row to the output file
            csv_writer.writerow(row)
