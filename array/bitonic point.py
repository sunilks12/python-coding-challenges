class Solution:

    def findMaximum(self,arr, n):
        # code here
        i = 0
        while i < n - 1:
            if arr[i] > arr[i + 1]:
                return arr[i]
            i += 1
        return arr[i]
                
