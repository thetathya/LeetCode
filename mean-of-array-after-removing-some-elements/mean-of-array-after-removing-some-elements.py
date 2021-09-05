class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        chng = int(len(arr)*0.05)
        arr = arr[chng:len(arr)-chng]
        return sum(arr)/len(arr)