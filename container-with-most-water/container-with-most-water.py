class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height)-1
        space = 0
        max_space = 0
        while i<j:
            space = min(height[i],height[j])*(j-i)
            if space>max_space:
                max_space = space
            if height[i] < height[j]:
                i = i + 1
            else:
                j = j - 1
        return max_space