class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_cnt = Counter(nums)
        return heapq.nlargest(k, freq_cnt, key=freq_cnt.get)