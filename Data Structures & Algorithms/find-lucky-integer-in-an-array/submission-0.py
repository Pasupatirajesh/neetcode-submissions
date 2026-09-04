class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count = Counter(arr)
        largest = -1
        for num, freq in count.items():
            if num == freq:
                largest = max(largest, num)
         
                
        
        return largest