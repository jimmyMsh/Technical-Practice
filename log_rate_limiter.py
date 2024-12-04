class LogRateLimiter:
    """
    Class for implementing a log rate limiter to control the frequency of log messages.

    Problem Statement:
    ------------------
    Design a rate limiter for log messages. A log message should only be printed
    if it has not been printed in the last `T` seconds.

    The class implements the following methods:
    1. `__init__(rate_limit: int)`: Initializes the rate limiter with a time limit (`T`) in seconds.
    2. `shouldPrintMessage(timestamp: int, message: str) -> bool`: Determines whether a log message
       can be printed based on the timestamp.

    Assumptions:
    ------------
    - Timestamps are non-negative integers and strictly increase.
    - The function must run efficiently to handle up to 10^6 calls.

    Usage:
    ------
    Create an instance of the `LogRateLimiter` class and call the `shouldPrintMessage()` method.

    Example:
    --------
    limiter = LogRateLimiter(10)
    print(limiter.shouldPrintMessage(1, "foo"))  # True
    print(limiter.shouldPrintMessage(2, "bar"))  # True
    print(limiter.shouldPrintMessage(3, "foo"))  # False
    print(limiter.shouldPrintMessage(11, "foo"))  # True
    """

    # Define the init part of the class
    def __init__(self, rate_limit):
        # Define the timelimit for this object
        self.rate_limit = rate_limit
        
        # Define the hash table that will serve as the place for message lookups
        self.message_time_sent = {}
    
    
    # Create the method with the given description
    def shouldPrintMessage(self, timestamp, message) -> bool:
        # First, determine if this message has been sent
        if message in self.message_time_sent:
            # Check when the last time it was sent
            last_time_sent = self.message_time_sent[message]
            
            # If it has been sent > than the limit time ago, then we can send it
            if timestamp - last_time_sent > self.rate_limit:
                # Update the last time it was sent
                self.message_time_sent[message] = timestamp
                return True
            # Otherwise, return false
            else:
                return False
            
        else:
            # Otherwise, can send it right away and add it to the map
            self.message_time_sent[message] = timestamp
            return True