class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = defaultdict(int)
        for i in range(len(nums)):
            var = target - nums[i]
            if var in d:
                return [d[var],i]
            d[nums[i]]+=i