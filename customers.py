

list = []
maxSum = []

inputLine = input()
list = inputLine.split(' ')
customers = int(list[0])
availableStock = int(list[1])

inputLine = input()
list = inputLine.split(' ')
stockA = int(list[0])
stockB = int(list[1])
totalStock = stockA * stockB

for i in range(0, customers):
    inputLine = input()
    list = inputLine.split(' ')
    maxSum.append((int(list[0]) * stockA) + (int(list[1]) * stockB))

maxSum2 = maxSum.copy()
maxSum.sort()

# Sorting Positions
s = maxSum2
li = []

for i in range(len(s)):
    li.append([s[i], i])
li.sort()
sort_index = []

for x in li:
    sort_index.append(x[1] + 1)


# Final
indexlist = []
i = 0
while(True):
    demand = maxSum[i]
    if demand <= availableStock:
        availableStock = availableStock - demand
        indexlist.append(sort_index[i])
        i = i + 1
    else:
        break

print(len(indexlist))
for i in range(0, len(indexlist)):
    print(indexlist[i], end=' ')
