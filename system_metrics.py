class Solution:
    """
    Class to calculate the average metric value for each unique metric ID.

    Methods:
    --------
    metric_calculator(input: List[Tuple[int, float]]) -> Dict[int, float]:
        Computes the average value for each metric ID from the input data.

    Expected Input:
    ---------------
    - input: A list of tuples, where each tuple contains:
        * metric_id (int): The unique identifier of a metric.
        * value (float): The value associated with that metric.

    Expected Output:
    ----------------
    - A dictionary where:
        * The key is the metric_id (int).
        * The value is the average of all the metric values associated with that metric ID (float).

    Example:
    --------
    Input:
        metrics = [(1, 10.0), (2, 20.0), (1, 30.0), (2, 40.0), (1, 50.0)]
    
    Output:
        
        {
            1: 30.0,  # Average of [10.0, 30.0, 50.0]
            2: 30.0   # Average of [20.0, 40.0]
        }
    """
    # Define a function that will take the input of metrics from the server
    def metric_calculator(self, input):
        # Define a hash map to hold all of the metric_id, value pairs
        # Hash map allows for O(1) update and retrieve
        metric_value_map = {}
        
        # Have another hash map to hold the number of requests to his node
        metric_requests_map = {}
        
        # We have to parse the input
        for metric_id, value in input:
            # First, update the value in the metric_requests map to account for the extra request
            if metric_id in metric_requests_map:
                metric_requests_map[metric_id] += 1
            # Otherwise, add the entry
            else:
                metric_requests_map[metric_id] = 1
                
            # Now that we accounted for the entry, update the value in the value map
            if metric_id in metric_value_map:
                metric_value_map[metric_id] += value
            else:
                metric_value_map[metric_id] = value
        
        # Once we have gone through all of the metric updates, we can calulate the current averages
        averages = {}
        for key in metric_value_map.keys():
            averages[key] = metric_value_map[key] / metric_requests_map[key]
        
        # Then finally, return the averages
        return averages


    # Optimized solution where the average is caluclated on the fly
    def metric_calc(self, input):
        # Define a map to hold the averages
        metric_average = {}
        
        metric_count = {}
        
        # Loop through the inputs
        for metric_id, val in input:
            # First, check if we have the average caluclated already
            if metric_id in metric_average:
                # Add one to the count
                metric_count[metric_id] += 1
                # Recalculate the average
                metric_average[metric_id] += (val - metric_average[metric_average])/metric_count[metric_id]
            # Otherwise, init the count / average
            else:
                metric_count[metric_id] = 1
                metric_average[metric_id] = val
        
        # Lastly, return the metric average hash as is
        return metric_average