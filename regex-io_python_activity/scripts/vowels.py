# Write the solution for "Filter Vowels".

# Imported for reading from command line
import sys

# Imported for regular expression commands
import re

# Imported to change file name to represent number of vowels
import os

def vowel_counter(path_to_file):
    # Check if the file exists before proceeding
    if not os.path.isfile(path_to_file):
        print(f"Error: The file '{path_to_file}' does not exist.")
        exit(1)
    
    with open(path_to_file, 'r') as input_file:
        # Counter to keep track of vowels
        vowel_count = 0
        
        # Iterate through each line in the file
        for line in input_file:
            # Get the length of the result for this line
            line_vowel_count = len(re.findall('[aeiouAEIOU]', line))
            
            # Add the vowel count of this line to the total
            vowel_count += line_vowel_count
        
    # Construct the new file name after processing the file
    directory = os.path.dirname(path_to_file)
    new_file_name = f"vowels-{vowel_count}.txt"
    new_file_path = os.path.join(directory, new_file_name)

    # Rename the file with the new name
    os.rename(path_to_file, new_file_path)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python vowels.py input_file_path")
        sys.exit(1)
    
    # Get the input file from the command line
    input_file_path = sys.argv[1]
    
    # Call the vowel_counter function with the provided arguments
    vowel_counter(input_file_path)