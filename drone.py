

def find(people):
    list = []
    newList = []

    for i in range(1, people + 1):
        list.append(i)

    # Programming Logic

    for i in range(1, people + 1):
        # if i == 1:
        newList.append(i)
        newList.append(i+2)
        # list.remove(i)
        # list.remove(i+2)
        # # elif i == 2:
        # newList.append(i)
        # newList.append(i+2)
        # list.remove(i)
        # list.remove(i+2)

    print(newList)


testcase = int(input())

for i in range(0, testcase):
    people = int(input())
    find(people)
