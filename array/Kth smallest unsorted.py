arr={7, 10, 4, 3, 20, 15}
K = 3 
l=[]
arr1=sorted(arr)

for i in range(len(arr1)):
    l.append(arr1[i])
print(l[K-1])
