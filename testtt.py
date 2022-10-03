arr = [2, 3, 4]
subsets = [[]]
for num in arr:
    print(num)
    size = len(subsets)
    for y in range(size):
        subsets.append(subsets[y]+[num])
print(subsets)