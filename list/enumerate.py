lst = [10, 20, 4, 45, 99]
m=max(lst)
x=[a for i,a in enumerate(lst) if a<m]
print(max(x))
