class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
      
        n = len(heights)
        if n == 0:
            return 0
        
        left = [0] * n       # First smaller element to the left
        right = [n] * n      # First smaller element to the right
        stack = []
        
        # Step 1: Find boundaries using single-pass stack algorithm
        for i in range(n):
            while stack and heights[i] <= heights[stack[-1]]:
                right[stack.pop()] = i
            left[i] = stack[-1] + 1 if stack else 0
            stack.append(i)
        
        # Step 2: Calculate maximum area using boundaries
        max_area = 0
        for i in range(n):
            width = right[i] - left[i]
            current_area = heights[i] * width
            max_area = max(max_area, current_area)
        
        return max_area
