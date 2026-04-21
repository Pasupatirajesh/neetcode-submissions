class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        triplet_set = set()
        # found_x = found_y = found_z = False
        # for x, y, z in triplets:
            
        #     if x <= target[0] and y <= target[1] and z <= target[2]:
        #         if x == target[0]: found_x = True
        #         if y == target[1]: found_y = True
        #         if z == target[2]: found_z = True
            
        
        for t in triplets:
            if all(t[i] <= target[i] for i in range(3)):
                for i in range(3):
                    if t[i] == target[i]:
                        triplet_set.add(i)
        return len(triplet_set) ==3 