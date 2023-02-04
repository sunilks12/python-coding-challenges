

res = []
for ele in test_list:
    sum = 0
    for digit in str(ele):
        sum += int(digit)
    res.append(sum)
     
# printing result
print ("List Integer Summation : " + str(res))


