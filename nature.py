
import math

list = []
newList = []

testcase = int(input())

for i in range(0, testcase):
    inputLine = input()
    list = inputLine.split(' ')
    list = [int(i) for i in list]

    sum = 0
    for j in range(0, 9):
        if list[j] > 0 and list[j] < 10:
            count = list.count(list[j])
            pOfD = math.log10(1 + 1 / list[j])
            temp = pOfD - count
            sum = sum + temp
    print(sum)
