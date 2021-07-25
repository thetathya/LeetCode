class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def inv(s):
            x = ""
            for i in reversed(range(len(s))):
                if s[i]=="0":
                    x+="1"
                else:
                    x+="0"
            return x

        s = "0"
        for i in range(n-1):
            s+= "1" + inv(s)
        return s[k-1]
        