my_list = [1, 2, 3, "x", 4, "x", "x"]
counts = {}
for element in my_list:
    if element not in counts:
        count = 0
        for i in my_list:
            if i == element:
                count += 1
        counts[element] = count
print(counts)
