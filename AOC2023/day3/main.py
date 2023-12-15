import copy

def read_input(file):
    with open(file) as input:
        input = input.read()
        output = input.split("\n")
    return output


input_list = read_input("input.txt")
print(input_list)


def x_coordinates(row):
    start = False
    end = False
    numeric = False
    x_list = []
    symbol_list = []

    for x, point in enumerate(row):
        if point != ".":
            if point.isnumeric():
                if not start:
                    startpoint = x
                    start = True
                    numeric = True
            else:
                if start:
                    endpoint = x - 1
                    start = False
                    x_list.append([numeric, startpoint, endpoint])
                x_list.append([False, x, x])
        if (point == "." and start == True) or (x == len(row) - 1 and start == True):
            if x == len(row) - 1 and point != ".":
                endpoint = x
            else:
                endpoint = x - 1

            x_list.append([numeric, startpoint, endpoint])
            start = False
            numeric = False

    return x_list


def get_number(row, point):
    numba = input_list[row][point[1]:point[2] + 1]
    return int(numba)


def xmin(checkval):
    if checkval[1] - 1 < 0:
        return 0
    else:
        return checkval[1] - 1


def xmax(checkval):
    if checkval[2] + 1 > len(input_list[0]):
        return checkval[2]
    else:
        return checkval[2] + 1


def ymin(checkval):
    if checkval - 1 < 0:
        return 0
    else:
        return checkval - 1


def ymax(checkval):
    if checkval + 1 > len(input_list) - 1:
        return checkval
    else:
        return checkval + 1


def check_surround(row, point):
    surround = ""
    xminval = xmin(point)
    xmaxval = xmax(point)
    yminval = ymin(row)
    ymaxval = ymax(row)
    dict = {"xminval": xminval,
            "xmaxval": xmaxval,
            "yminval": yminval,
            "ymaxval": ymaxval, }

    return dict


def get_surround(coords):
    sourround = ""
    for y in range(coords["yminval"], coords["ymaxval"] + 1):
        for point in input_list[y][coords["xminval"]:coords["xmaxval"] + 1]:
            sourround += point
    return sourround


def counts(sourround):
    counts = False
    for point in sourround:
        if point != "." and not point.isnumeric():
            counts = True
    return counts


result = 0
x_coord_list = [x_coordinates(row) for row in input_list]
for row, points in enumerate(x_coord_list):
    for point in points:
        if point[0]:
            mynumber = get_number(row, point)
            coords = check_surround(row, point)
            sourround = get_surround(coords)
            if counts(sourround):
                result += mynumber
                print(mynumber)
                print(sourround)
            else:
                pass
print(result)


def getnumba2(coords, resultstarts,ruff):
    numbas = []
    for row, points in enumerate(x_coord_list):
        for point in points:
            if point[0]:
                for y in range(coords["yminval"], coords["ymaxval"] + 1):
                    if y == row:
                        if coords["xminval"] <= point[1] <= coords["xmaxval"] or coords["xminval"] <= point[2] <= \
                                coords["xmaxval"]:
                            numbas.append([row,point])

    if len(numbas)==2:
        resultstarts.append(numbas)


resultstarts = []
for row, points in enumerate(x_coord_list):
    for point in points:
        if not point[0]:
            if input_list[row][point[1]] == "*":
                coords = check_surround(row, point)
                print(coords)
                sourroundx = get_surround(coords)
                getnumba2(coords, resultstarts,row)
print(resultstarts)
resj2=0
for resultxx in resultstarts:
    numba1,numba2=resultxx
    numba1=get_number(numba1[0],numba1[1])
    numba2 = get_number(numba2[0], numba2[1])
    print(numba1,numba2)
    resj2+=numba1*numba2
print(resj2)