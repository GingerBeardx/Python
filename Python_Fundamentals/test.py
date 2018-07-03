x = [19, 2, 54, -2, 7, 12, 98, 32, 10, -3, 6]
x.sort()
i = 0
nx = []
for x[i] in x:
    if len(x) - 1 == (len(x) / 2):
        break
    nx.insert(i, x.pop(0))
    i += 1
print x
x.insert(0, nx)
print x

# The output should be: [[-3, -2, 2, 6, 7], 10, 12, 19, 32, 54, 98]
# Output is currently: [[-3, -2, 2, 6, 7, 10], 12, 19, 32, 54, 98]
