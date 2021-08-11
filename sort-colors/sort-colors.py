class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums)==1:
            return nums
        cnt = [0]*(max(nums)+1)
        pnt = 0
        for i in nums:
            cnt[i] += 1

        for i in range(len(nums)):
            while cnt[pnt]==0:
                pnt += 1
            nums[i] = pnt
            cnt[pnt] -=1

        return nums