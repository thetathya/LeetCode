class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        cni = 0
        cdi = 0
        for i in range(1,len(nums)):
            if nums[i-1]==nums[i]:
                continue
            elif nums[i-1]<=nums[i]:
                cni+=1
            elif nums[i-1]>=nums[i]:
                cdi+=1
        return cni==0 or cdi==0
        