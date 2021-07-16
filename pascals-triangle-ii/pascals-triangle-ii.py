class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        x = []
        for i in range(rowIndex+1):
            y = []
            for j in range(i+1):
                if j==0 or j==i:
                    y.append(1)
                else:
                    y.append(x[-1][j]+x[-1][j-1])
            x.append(y)
        return x[-1]