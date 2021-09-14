class Solution:
    def reverseParentheses(self, s: str) -> str:
        s = list(s)
        fo = []
        i = 0
        while i<len(s):
            if s[i]=='(':
                fo.append(i)
            elif s[i]==')':
                s[fo[-1]+1:i] = reversed(s[fo[-1]+1:i])
                fo.pop()
            i+=1
        ts = []
        for i in range(len(s)):
            if not( s[i]=='(' or s[i]==')'):
                ts.append(s[i])
        return ''.join(ts)