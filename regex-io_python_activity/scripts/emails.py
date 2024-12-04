# Write the solution for "New Emails".
# Imported for reading from command line
import sys

# Imported for regular expression commands
import re

# Converts the emails of a input_file in the format name,email
def email_transformer(input_file_path, output_file_path):
    with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
        
        # Define the domain name we will append to the username of the previous email
        new_domain = '@mlh.io'
        
        # Define the domain that is considered valid
        valid_domain = '@gmail.com'
        
        for line in input_file:
            # Strip line of white space and newlines
            line = line.strip()
            
            # Check if the line has one ',' to determine if it is in the valid format
            if line.count(',') != 1:
                continue
            
            # For each line in the input_file, split the line into the name and the email to isolate email
            name,email = re.split(',', line)
            
            # Check if the email is valid (end with @gmail.com)
            if not re.search(f'{valid_domain}$', email):
                output_file.write(f'{email}\n')
                continue
            
            # For each email, split into username and domain. Pick the username
            username = email.split('@')[0]
            
            # Add the username to the new domain and append it to the new input_file
            changed_email = username + new_domain
            
            output_file.write(f'{changed_email}\n')
    
    
# Ensure the script is run with two arguments
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python emails.py input_file_path output_file_path")
        sys.exit(1)

    # Retrieve the input and output file names from command-line arguments
    input_filename = sys.argv[1]
    output_filename = sys.argv[2]

    # Call the email_transformer function with the provided filenames
    email_transformer(input_filename, output_filename)