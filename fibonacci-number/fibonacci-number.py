def fibo(f1,f2,count,n):
    f3 = f2 + f1
    if count==n:
        return f3
    return fibo(f2,f3,count+1,n)
class Solution:
    def fib(self, n: int) -> int:
        if n<=1:
            return n
        else:
            return fibo(0,1,2,n)