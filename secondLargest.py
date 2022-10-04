
from ast import Num

# list = [10, 50, 60, 100, 20]


def find(list=[]):

    if list[0] < list[1]:
        largest = list[1]
        second = list[0]

    else:
        largest = list[0]
        second = list[1]

    i = 2
    while i < 5:
        if list[i] > largest:
            second = largest
            largest = list[i]

        elif list[i] > second and list[i] != largest:
            second = list[i]

        i = i + 1

    print("Second Largest Element is", second)


# Main
list = []
n = int(input('Enter Number of elements: '))

for i in range(0, n):
    element = int(input())
    list.append(element)

find(list)
