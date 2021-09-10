class Solution:
    def secondHighest(self, s: str) -> int:
        numbers = "0123456789"
        ans = []
        for i in s:
            if i in numbers:
                ans.append(i)

        ans = list(set(ans))
        ans = sorted(ans)
        if len(ans)>1:
            return ans[-2]
        return -1