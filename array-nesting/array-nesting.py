class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        val=0
        cnt_mx = 0
        for j in range(len(nums)):
            cnt = 0
            i = j
            val=0
            while val!=-1:
                val = nums[i]
                # print('Hey')
                nums[i] = -1
                i = val
                if val==-1:
                    break
                cnt+=1
            cnt_mx = max(cnt_mx, cnt)
        return cnt_mx