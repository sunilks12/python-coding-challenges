
class Solution:
    def MissingNumber(self,array,n):
        answer=n*(n+1)//2-sum(array)
        return answer

            
                
