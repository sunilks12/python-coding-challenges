'''
Given a Integer array A[] of n elements. Your task is to complete the function PalinArray.
Which will return 1 if all the elements of the Array are palindrome otherwise it will return 0.
'''

# easy method
# Function should return True/False or 1/0
def PalinArray(arr ,n):

    # Code here
    for i in range(n):
        if str(arr[i]) != str(arr[i])[::-1]:
            return 0
    return 1
        

  # Your task is to complete this function
# Function should return True/False or 1/0
def PalinArray(arr ,n):
    counter=0
    for i in range(n):
        if (arr[i]==reverse(arr[i])):
            counter+=1
    if counter==n: return 1
    else: return 0

def reverse(num):
    revNum=0;
    while (num!=0):
        digit=num%10
        revNum=revNum*10+digit
        num=num//10
    return revNum
