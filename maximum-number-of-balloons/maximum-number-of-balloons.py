class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        cnt = defaultdict(int)
        balloons = ['b', 'a', 'l','o','n']
        for i in text:
            cnt[i]+=1
        mn = float('inf')
        for i in balloons:
            if i=='l' or i=='o':
                mn = min(mn,cnt[i]//2)
                continue
            mn = min(mn,cnt[i])
        return mn