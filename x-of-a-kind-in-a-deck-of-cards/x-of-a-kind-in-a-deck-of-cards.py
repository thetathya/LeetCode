class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        if len(deck)==1:
            return False
        d = defaultdict(int)
        for i in deck:
            d[i]+=1
        lst = list(d.values())
        x = reduce(gcd, lst)
        if x==1:
            return False
        for i in d:
            if d[i]%x==0:
                continue
            else:
                return False
        return True