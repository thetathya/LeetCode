class Solution:
    def replaceDigits(self, s: str) -> str:
        s = list(s)
        def shift(c,x):
            return chr(ord(c)+x)
        for i in range(1,len(s),2):
            s[i]= shift(s[i-1],int(s[i]))
        return ''.join(s)