# Write the solution for "Longest Word".

# Imported for reading from command line
import sys

# Imported for regular expression commands
import re

# Loop through the text and find the longest word O(n)
# Once longest word length is found, bold this word in resulting file O(n)
def longest_word_bold(input_file_path, output_file_path):
    with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
    
        # Define the largest word length as zero to start
        longest_word_len = 0
            
        # Read through each line in the input file
        for line in input_file:
            # Split the line into words
            words = re.findall(r'\b\w+\b', line)
            
            # Go through the words and store longest
            for word in words:
                curr_word_len = len(word)
                
                # For each word in the line, hold largest word thus far
                longest_word_len = max(longest_word_len, curr_word_len)
    
        # Reset the file pointer to start for the second pass
        input_file.seek(0)
        
        # Second pass to apply formatting
        for line in input_file:
            # Store the updated line
            updated_line = line
            
            # Find all the words
            words = re.findall(r'\b\w+\b', line)
            
            # Go through all of the words
            for word in words:
                # modify the words if they are the same length as max word.
                if len(word) == longest_word_len:
                    # Use regex to change full word matches
                    updated_line = re.sub(fr'\b{word}\b', f'**{word}**', updated_line)
            
            # Write this updated line to output file
            output_file.write(updated_line)

# Ensure the script is run with two arguments
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python longest.py input_file_path output_file_path")
        sys.exit(1)

    # Retrieve the input and output file names from command-line arguments
    input_filename = sys.argv[1]
    output_filename = sys.argv[2]

    # Call the word bolder function with the provided filenames
    longest_word_bold(input_filename, output_filename)