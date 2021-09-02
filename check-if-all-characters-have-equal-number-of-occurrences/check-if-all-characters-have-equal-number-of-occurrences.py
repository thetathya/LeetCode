class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        # from collections import defaultdict
        d = defaultdict(int)
        for i in s:
            d[i]+=1
        d = list(d.values())
        d = set(d)
        return len(d)==1