class LogFileAnalyzer:
    """
    Class for analyzing log files and counting occurrences of log levels.

    Problem Statement:
    ------------------
    Given a log file where each line follows the format:
        <timestamp> <log_level> <message>
    Count the number of occurrences of each valid log level (`INFO`, `WARN`, `ERROR`).

    Requirements:
    -------------
    - Ignore lines that are malformed (e.g., missing fields or invalid log levels).
    - Process the file line by line to handle large files efficiently.
    - Return a dictionary with the log levels as keys and their counts as values.

    Usage:
    ------
    Call the `log_file_counter()` method, providing the file path as a string.

    Example:
    --------
    Input File Content (log.txt):
        2023-12-03T10:15:30 INFO User login successful
        2023-12-03T10:16:00 WARN Low disk space
        2023-12-03T10:17:45 ERROR Failed to connect to database
        Malformed line without proper fields
        2023-12-03T10:18:10 INFO User logout successful

    Function Call:
        LogFileAnalyzer.log_file_counter("log.txt")

    Output:
        {
            "INFO": 2,
            "WARN": 1,
            "ERROR": 1
        }
    """
    
    @staticmethod
    def log_file_counter(input_file):
        # Pre-initialize the dictionary for valid log levels
        entries_dict = {"INFO": 0, "WARN": 0, "ERROR": 0}

        try:
            with open(input_file, "r") as input:
                # Process each line in the file
                for line in input:
                    # Split the line into parts with at most 3 components
                    parts = line.split(maxsplit=2)
                    
                    # Validate the line format
                    if len(parts) < 3:
                        continue
                    
                    # Extract log level
                    log_level = parts[1]
                    
                    # Increment count if log level is valid
                    if log_level in entries_dict:
                        entries_dict[log_level] += 1

        except FileNotFoundError:
            print(f"Error: File '{input_file}' not found.")
        except PermissionError:
            print(f"Error: Permission denied to access '{input_file}'.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        
        # Return the dictionary with counts
        return entries_dict