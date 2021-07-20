class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        max_height = 0
        ocean_view = []
        for i in reversed(range(len(heights))):
            if heights[i]>max_height:
                max_height = heights[i]
                ocean_view.append(i)
        ocean_view.sort()
        return ocean_view