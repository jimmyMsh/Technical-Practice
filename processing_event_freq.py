from collections import defaultdict
import heapq

class Solution:
    """
    Class to process server event logs and calculate event frequencies within a sliding time window.

    Methods:
    --------
    log_process(logs: List[Tuple[int, int]], W: int) -> List[Dict[int, int]]:
        Computes the frequency of each event ID within the last W seconds at each event's timestamp.

    Expected Input:
    ---------------
    - logs: A list of tuples, where each tuple contains:
        * timestamp (int): The time (in seconds) of the event.
        * event_id (int): The unique identifier of the event.
    - W: An integer representing the sliding time window (in seconds).

    Expected Output:
    ----------------
    - A list of dictionaries, where:
        * Each dictionary represents the frequency of events within the sliding window at the corresponding log entry.
        * Keys are event IDs (int), and values are their counts (int).

    Example:
    --------
    Input:
        logs = [(1, 101), (2, 102), (3, 101), (8, 101), (10, 102), (15, 101)]
        W = 10
    
    Output:
        [
            {101: 1},                # At timestamp 1
            {101: 1, 102: 1},        # At timestamp 2
            {101: 2, 102: 1},        # At timestamp 3
            {101: 3, 102: 1},        # At timestamp 8
            {101: 3, 102: 2},        # At timestamp 10
            {101: 2, 102: 1}         # At timestamp 15
        ]
    """
    def log_process(self, logs, W):
        # First, define the result array
        res = []
        # Then, define the dict to hold the elements up to a certain point
        events_in_range = defaultdict(int)
        
        # Make a variable to be the start pointer to determine how to change the size of the window
        start = 0
        
        # Iterate through the logs with another pointer
        for end in range(len(logs)):
            # Get the information within this log
            timestamp, event_id = logs[end]
            
            # Increment the counter for this event
            # Default dict inits to 0 if DNE
            events_in_range[event_id] += 1
            
            # Then, determine if the element at start is within the range. As long as it is not, keep iterating:
            # (Check if it is outisde of this range and continue if it is)
            while logs[start][0] < timestamp - W:
                # Get this element ID
                event_id = logs[start][1]
                # Remove this element
                events_in_range[event_id] -= 1
                # If this element is already zero, then delete it from the dict
                if events_in_range[event_id] == 0:
                    del events_in_range[event_id]
                # Incremenet the start counter
                start += 1
            
            # At this point, after we remove all of the elements outside of the range (W), this is the result for this item
            res.append(dict(events_in_range))
        
        # At the end, return the array of all results
        return res
