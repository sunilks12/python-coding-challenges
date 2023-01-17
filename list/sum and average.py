start=0
lst=[1,2,4,7]
def sum(lst):

    for i in lst:
        start=i%10
        start=start+i
    return start

def avg(lst):
    avg=sum(lst)/len(lst)
    return avg

avg(lst)
