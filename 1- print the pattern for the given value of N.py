'''
You are given a number N. You need to print the pattern for the given value of N.

For N = 2 the pattern will be 
2 2 1 1
2 1

For N = 3 the pattern will be 
3 3 3 2 2 2 1 1 1
3 3 2 2 1 1
3 2 1

Note: Instead of printing a new line print a "$" without quotes. After printing the total output, end of the line is expected.
'''


def printPat(n):
    #Code here
    s=""
    for i in range(n,0,-1):
        for j in range(n,0,-1):
            s+=(str(j)+" ")*i
        s+="$"
    print(s)

