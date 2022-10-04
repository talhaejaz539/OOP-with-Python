

from imaplib import Int2AP


def newIndex(start, value, list=[]):
    for i in range(start + 1, len(list)):
        if list[i] == value:
            return i


list = []
listA = []
listB = []
maxSum = []
indexlist = []

firstline = input()
secondline = input()

list = firstline.split(' ')
customers = int(list[0])
availableStock = int(list[1])

list = secondline.split(' ')
stockA = int(list[0])
stockB = int(list[1])
totalStock = stockA * stockB

for i in range(0, customers):
    customerline = input()
    list = customerline.split(' ')
    listA.append(int(list[0]))
    listB.append(int(list[1]))
    maxSum.append((listA[i] * stockA) + (listB[i] * stockB))

print(maxSum)

maxSum2 = []
maxSum2 = maxSum

while(True):
    demand = min(maxSum)
    if demand <= availableStock:
        a = maxSum2.index(demand) + 1
        if a in indexlist:
            print("a", a)
            indexlist.append(a)
        elif a not in indexlist:
            b = newIndex(a, demand, maxSum2)
            print("b", b)
            indexlist.append(b)
        availableStock = availableStock - demand
        maxSum.remove(demand)
        print(maxSum)
    else:
        break

print(len(indexlist))
for i in range(0, len(indexlist)):
    print(indexlist[i], end=' ')
