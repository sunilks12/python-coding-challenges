lst=[9,10,8,7,11,10,12,11]
new_lst=[]
for i in range(len(lst)-2):
    if lst[i]<lst[i+1] and lst[i+1]>lst[i+2]:
        a=lst[i+1]
        new_lst.append(a)
new_lst
