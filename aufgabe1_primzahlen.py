num = []
i = 2
for i in range(2, 100):
    j = 2
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        num.append(i)
print(num)
# Output: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
