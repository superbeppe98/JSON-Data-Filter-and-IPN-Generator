import os
import json

# Check if input file exists
input_file_name = 'input.json'
if not os.path.exists(input_file_name):
    # Create an empty input file
    with open(input_file_name, 'w') as f:
        f.write('[]')

# Open the input JSON file for reading
with open('input.json', 'r') as f:

    # Load the contents of the input JSON file
    data = json.load(f)

    # Extract items belonging to the desired category
    category_name = input("Enter category name: ")
    filtered_data = [
        item for item in data if item['Category Name'] == category_name]

# Count the extracted items
count = len(filtered_data)

# Print the number of extracted items
print(f"{count} items have been extracted.")

# Open the output JSON file for writing
with open('temp.json', 'w') as f:

    # Write the filtered data to the output file
    json.dump(filtered_data, f)

# Prompt user to input IPN length
ipn_length = int(input("Enter desired IPN length: "))

# Take user input for prefix
prefix = input("Enter prefix for IPN: ")

# Calculate the number of digits after the prefix
sequence_length = ipn_length - len(prefix)

# Take user input for number of sequential numbers to generate
num_numbers = int(input("Enter number of sequential numbers to generate: "))

# Create a list of sequential numbers from 1 to 155
sequence_number = [prefix + str(i).zfill(5) for i in range(1, num_numbers+1)]

# Open the output JSON file for reading
with open('temp.json', 'r') as f:

    # Load the contents of the output JSON file
    data = json.load(f)

    # Replace the IPN element of each item with the new value
    for i, item in enumerate(data):
        new_ipn = sequence_number[i].zfill(sequence_length)
        item["IPN - Numero di riferimento interno"] = new_ipn

# Remove temp file
os.remove('temp.json')

# Write the updated JSON content to a new file
with open('output.json', 'w') as outfile:
    json.dump(data, outfile)
