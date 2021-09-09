class MRUQueue:
    
    def __init__(self, n: int):
        self.nums = []
        for i in range(1,n+1):
            self.nums.append(i)

    def fetch(self, k: int) -> int:
        tmp = self.nums.pop(k-1)
        self.nums.append(tmp)
        return self.nums[-1]
        
# Your MRUQueue object will be instantiated and called as such:
# obj = MRUQueue(n)
# param_1 = obj.fetch(k)