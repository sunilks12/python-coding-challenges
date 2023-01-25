from typing import List


class Solution:
    def convertToWave(self, n : int, a : List[int]) -> None:
        # code here
        for i in range(0, n-1, 2):
            a[i], a[i + 1] = a[i + 1], a[i]

            



class Solution:
    def convertToWave(self, n : int, a : List[int]) -> None:
        # code here
        if(n%2!=0):
            i=0
            while(i<n-2):
                a[i],a[i+1]=a[i+1],a[i]
                i+=2
        if(n%2==0):
            i=0
            while(i<n-1):
                a[i],a[i+1]=a[i+1],a[i]
                i+=2
        



