class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ans = defaultdict(int)
        lst = []
        f = 0
        s = 0
        for i in range(1,len(nums)+1):
            ans[i]=0
        for i in nums:
            ans[i]+=1
        for i in ans:
            if ans[i]==0:
                s=i
            if ans[i]==2:
                f=i
        lst.append(f)
        lst.append(s)
        return lst