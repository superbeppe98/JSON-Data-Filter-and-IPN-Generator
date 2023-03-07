# JSON-Data-Filter-and-IPN-GeneratorSON Data Filter and IPN Generator
JSON Data Filter and IPN Generator is a Python program that filters items from a JSON file based on a user-specified category name and generates a sequence of unique internal reference numbers (IPN) for the filtered items.

Installation
To use JSON Data Filter and IPN Generator, you need to have Python 3 installed on your system. No additional dependencies are required.

Usage
To use JSON Data Filter and IPN Generator, you need to provide a JSON file named "input.json" that contains a list of items to filter and generate IPNs for. The items in the file should have a "Category Name" attribute that specifies their category. Once you have the file ready, you can run the program by navigating to the directory where the program is stored and running the following command:

shell
Copy code
$ python3 json_filter_and_ipn_generator.py
This will prompt you to enter a category name to filter the items by. Once you have entered the category name, the program will filter the items that belong to that category and output the number of extracted items. The filtered items will be stored in a temporary file named "temp.json".

Next, the program will prompt you to enter a desired IPN length, a prefix for the IPNs, and the number of sequential numbers to generate. Based on these inputs, the program will generate a sequence of unique IPNs with the specified prefix and sequential numbers. The generated IPNs will be assigned to the filtered items in the temporary file.

Finally, the program will write the updated JSON content to a new file named "output.json". You can view the output file to see the filtered items with their new IPNs.
