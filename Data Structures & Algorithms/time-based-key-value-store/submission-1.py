class TimeMap:

    def __init__(self):
        self.hashmap = {}  # Dictionary to store {key: [(value, timestamp)]}

    def set(self, key: str, value: str, timestamp: int) -> None:
        """Stores the (timestamp, value) pair for the given key."""
        if key not in self.hashmap:
            self.hashmap[key] = []
        self.hashmap[key].append((value, timestamp))  # Store value first, timestamp second

    def get(self, key: str, timestamp: int) -> str:
        """Retrieves the latest value for key at a timestamp ≤ given timestamp."""
        if key not in self.hashmap:
            return ""
        
        values = self.hashmap[key]  # List of (value, timestamp) pairs
        return self.binary_search(values, timestamp)

    def binary_search(self, values, timestamp):
        """Performs binary search to find the latest timestamp ≤ given timestamp."""
        lo, hi = 0, len(values) - 1
        best_index = -1

        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if values[mid][1] <= timestamp:  # Corrected: Compare using timestamp, not value
                best_index = mid
                lo = mid + 1  # Look for later timestamps
            else:
                hi = mid - 1  # Look for earlier timestamps

        return values[best_index][0] if best_index != -1 else ""  # Return corresponding value
