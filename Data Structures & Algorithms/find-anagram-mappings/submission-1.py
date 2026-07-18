class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mappings = {}
        if len(nums1) != len(nums2):
            return []
        for i in range(len(nums2)):
            if nums2[i] not in mappings:
                mappings[nums2[i]] = i 
        return [mappings[val] for val in nums1]


        