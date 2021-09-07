class Solution:
    def addDigits(self, num: int) -> int:
        while True:
            tmp = str(num)
            sm = 0
            for i in tmp:
                sm += int(i)
            num = str(sm)
            if len(num)==1:
                break
        return num