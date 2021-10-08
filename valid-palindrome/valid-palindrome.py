class Solution:
    def isPalindrome(self, s: str) -> bool:
        f = 0
        i=0
        j=len(s)-1
        s = s.lower()
        while i<j:
            if not s[i].isalnum():
                i+=1
                continue
            if not s[j].isalnum():
                j-=1
                continue
            if s[i]==s[j]:
                i+=1
                j-=1
            else:
                f=1
                break
        return f==0