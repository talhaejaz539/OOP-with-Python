

def find(people):

    i = 0   # Plate to be picked
    j = 1   # Skip Size

    arr: list = [i + 1 for i in range(people)]

    while len(arr) > 1:  # loop run untill we have only one plate i.e. last plate
        arr.pop(i)
        i = (i + j) % len(arr)
        j += 1

    return arr[0]


testcase = int(input())

for i in range(0, testcase):
    people = int(input())
    print(find(people))

print(3 % 3)
