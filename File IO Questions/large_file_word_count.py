from typing import List, Tuple
import heapq
from collections import Counter
import re

class Solution:
    """
    Solution class for solving the "Top K Frequent Words in a Large File" problem.

    Problem Statement:
    ------------------
    Given a very large text file (too large to fit into memory), find the top `k` most
    frequent words in the file. Words are treated case-insensitively, and punctuation
    should be ignored.

    The function must:
    1. Count the occurrences of each unique word in the file.
    2. Return the top `k` most frequent words in descending order of frequency.
    3. Break ties alphabetically in ascending order.

    Assumptions:
    ------------
    - The file is too large to load into memory at once.
    - Words are separated by whitespace, and punctuation should be ignored.
    - The function should handle missing files or file permission errors gracefully.

    Usage:
    ------
    Call the `top_k_frequent_words()` method, providing the file path as a string
    and `k` as an integer for the number of top frequent words to return.

    Example:
    --------
    Input File Content (example.txt):
        Hello, world! Hello there.
        This is a test. Hello test world.

    Function Call:
        Solution.top_k_frequent_words("example.txt", 2)

    Output:
        [("hello", 3), ("world", 2)]
    """
    
    @staticmethod
    def top_k_frequent_words(file_path: str, k: int) -> List[Tuple[str, int]]:
        word_freq = Counter()
        
        try:
            with open(file_path, "r") as input_file:
                for line in input_file:
                    # Normalize the line: remove punctuation and convert to lowercase
                    words = re.findall(r'\b\w+\b', line.lower())
                    
                    # Update word frequencies
                    for word in words:
                        word_freq[word] += 1

            # Use a min-heap to keep only the top k elements
            heap = []
            for word, freq in word_freq.items():
                heapq.heappush(heap, (freq, word))
                if len(heap) > k:
                    heapq.heappop(heap)  # Remove the smallest frequency

            # Sort heap results by frequency (descending) and alphabetically (ascending for ties)
            result = sorted(heap, key=lambda x: (-x[0], x[1]))
            return [(word, freq) for freq, word in result]

        except PermissionError:
            print(f"NO PERMISSION TO OPEN FILE {file_path}")
            return []
        except Exception as e:
            print(f"Error: {e}")
            return []
