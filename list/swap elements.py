'''
Python program to interchange first and last elements in a list
'''
def swap(lst):

    first=lst[0]
    last=lst[-1]
    lst[0]=last
    lst[-1]=first
    return lst
