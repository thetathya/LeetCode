class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        ans = []
        ans.append(releaseTimes[0])
        for i in range(1,len(releaseTimes)):
            ans.append(releaseTimes[i]-releaseTimes[i-1])
        mx = max(ans)
        tmp = []
        for i in range(len(releaseTimes)):
            if ans[i]==mx:
                tmp.append(keysPressed[i])
        tmp.sort()
        return tmp[-1]