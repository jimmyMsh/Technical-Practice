# Write the solution for "Split the files".

# Imported for reading from command line
import sys

# Imported for regular expression commands
import re

# Imported to change file name to represent number of vowels
import os

def split_file_content(input_file_path, output_dir_path, max_file_byte_size = 500):
    # Capture the start of the file name (to create other files if needed)
    file_name = os.path.basename(input_file_path).split('.')[0]
    
    # vars to keep track of the file splitting
    curr_bytes = 0
    part_num = 1
    current_buffer = ''
    
    # Defining helper method to handle writing buffer to a new file when it surpasses byte size
    def write_buffer_to_file(buffer, part_num):
        # Define the file we are writing to
        output_file_path = f"{output_dir_path}/{file_name}-{part_num}.txt"
        # Write the buffer to this file
        with open(output_file_path, 'w') as output_file:
            output_file.write(buffer)
    
    # Define the regex for capturing all ascii (non-whitespace and whitespace)
    text_pattern = re.compile(r'\S+|\s+')
    
    with open(input_file_path, 'r') as input_file:
        while True:
            # Read a chunk of 100 chars
            chunk = input_file.read(100)
            
            # Iterate as long as there are 'chunks' in the file
            if not chunk:
                break
            
            # Get all of the ascii from the chunk
            all_text = text_pattern.findall(chunk)
            
            # Iterate through the text
            for text in all_text:
                # Get the size of this text
                text_size = len(text.encode('utf-8'))
                
                if text_size + curr_bytes > max_file_byte_size:
                    # Then write the buffer to another file with helper method
                    write_buffer_to_file(current_buffer, part_num)
                    
                    # Reset the current buffer (now written to another file)
                    current_buffer = ''
                    
                    # Reset the current bytes to track again
                    curr_bytes = 0
                    
                    # Iterate to next part of file
                    part_num += 1
                
                # Add the current text to the buffer
                current_buffer += text
                curr_bytes += text_size
            
        
        # Write remaining buffer to file
        if current_buffer:
            write_buffer_to_file(current_buffer, part_num)
                
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python inputs.py input_file_path output_dir_path")
        exit(1)
    
    # Get the input file from command line
    input_file_path = sys.argv[1]
    
    # Get the ouput dir from the command line
    output_dir_path = sys.argv[2]
    
    # Call the split_file_content function
    split_file_content(input_file_path, output_dir_path)