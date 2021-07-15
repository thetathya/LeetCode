class Solution:
    def jump(self, nums: List[int]) -> int:
        ans = 0
        left = 0
        right = 0
        while right<len(nums)-1:
            far = 0
            for i in range(left,right+1):
                far = max(far, i + nums[i])
            left = right + 1
            right = far
            ans += 1
        return ans