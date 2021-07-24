class Solution:
    def isPow(self,x,n):
        if 2**x==n:
            return True
        elif 2**x>n:
            return False
        return self.isPow(x+1,n)
    def isPowerOfTwo(self, n: int) -> bool:
        return self.isPow(0,n)