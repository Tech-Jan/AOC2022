from filereader import readfile

a = readfile("input")
print(a)

# print(a[2][4])

i = 1
x_len = len(a[0])

b = 1
y_len = len(a)

myposition = 3, 2

print(a[3][2])


def checksouth(y, x):
    height = a[y][x]
    i = 0
    border = False
    for counter in range(y + 1, y_len):
        print(f"south {a[counter][x]}")
        current_height = a[counter][x]
        if current_height <= height:
            i += 1
            if current_height == height:
                return i
    if i == 0:
        i += 1
    return i


def checknorth(y, x):
    height = a[y][x]
    i = 0
    border = False
    for counter in range(y - 1, -1, -1):
        print(f"north {a[counter][x]}")
        current_height = a[counter][x]
        if current_height <= height:
            i += 1
            if current_height == height:
                return i
    if i == 0:
        i += 1
    return i


def checkwest(y, x):
    height = a[y][x]
    i = 0
    border = False
    for counter in range(x - 1, -1, -1):
        print(f"west {a[y][counter]}")
        current_height = a[y][counter]
        if current_height <= height:
            i += 1
            if current_height == height:
                return i
    if i == 0:
        i += 1
    return i


def checkeast(y, x):
    height = a[y][x]
    i = 0
    border = False
    for counter in range(x + 1, x_len):
        print(f"east {a[y][counter]}")
        current_height = a[y][counter]
        if current_height <= height:
            i += 1
            if current_height == height:
                return i
    if i == 0:
        i += 1
    return i


def checkpos(y, x):
    height = a[y][x]
    print(checknorth(y, x))
    print(checkwest(y, x))
    print(checksouth(y, x))
    print(checkeast(y, x))
    result = checknorth(y, x) * checkwest(y, x) * checksouth(y, x) * (checkeast(y, x))
    return result


currentmax = 0
for y in range(0, y_len):
    for x in range(0, x_len):
        current = checkpos(y, x)
        if current > currentmax:
            currentmax = current

print(currentmax)
