import random as r
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.original = nums.copy()
        

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.original

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        n = len(self.nums)
        for i in range(n):
            rand = r.randint(0, n-1)
            self.nums[i], self.nums[rand] = self.nums[rand], self.nums[i]
        return self.nums
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()