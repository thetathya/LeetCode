class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt = 0
        mx=0
        for i in nums:
            if i==1:
                cnt+=1
            else:
                cnt = 0
            mx  = max(cnt,mx)
        return mx