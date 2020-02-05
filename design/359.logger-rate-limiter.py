class Logger:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.memo = {} 

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        if message in self.memo:
            if timestamp - self.memo[message] >= 10:
                self.memo[message] = timestamp
                return True
            return False
        else:
            self.memo[message] = timestamp
            return True
