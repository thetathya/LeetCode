class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_mx = nums[0]
        mx = nums[0]
        for i in range(1,len(nums)):
            curr_mx = max(nums[i],nums[i]+curr_mx)
            mx = max(curr_mx,mx)
        return mx