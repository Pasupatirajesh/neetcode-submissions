class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mappings = defaultdict(int)
        if len(nums1) != len(nums2):
            return []
        
        for i in range(len(nums2)):
            if nums2[i] not in mappings:
                mappings[nums2[i]] = i 
        res = []
        for num in nums1:
            if num in nums2:
                res.append(mappings.get(num))
        return res 


        