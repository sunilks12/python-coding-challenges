min1 = l[0]
 
for i in range(len(l)):
 
    # If the other element is min than first element
    if l[i] < min1:
        min1 = l[i] #It will change
 
print("The smallest element in the list is ",min1)
