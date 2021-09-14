class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        maping = {'0': 0, '1':1, '2':2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

        cnt = len(num1)-1
        sm1 = 0
        for i in range(len(num1)):
            sm1 += maping[num1[i]]*(10**cnt)
            cnt -=1

        cnt = len(num2)-1
        sm2 = 0
        for i in range(len(num2)):
            sm2 += maping[num2[i]]*(10**cnt)
            cnt -=1
        return str(sm1*sm2)