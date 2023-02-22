arr=[1, 4, 20, 3, 10, 5]
sm = 33
dic={}
curr_sum=0

for i in range(len(arr)):
    curr_sum=curr_sum+arr[i]
    dic[curr_sum]=i
    if curr_sum==sm:
        print(curr_sum)
        print("sub array",i)
    if curr_sum-sm in dic:
        print("subarray starts from", dic[curr_sum-sm]+1, "to",i)
 
    #dic[curr_sum]=i
     
