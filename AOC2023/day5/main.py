import copy


def read_input(file):
    with open(file) as input:
        input = input.read()
        output = input.split("\n")
    return output


input_list = read_input("input.txt")
print(input_list)

seeds = [int(s) for s in input_list[0].split(": ")[1].split()]
maps = [i for i in range(7)]
print(seeds)


def get_map(i: int) -> list[int, int]:
    z = -1
    endrow = -1
    for row_number, row in enumerate(input_list):
        if "map:" in row:
            z += 1
            if z == i:
                startrow = row_number + 1
            if z == i + 1:
                endrow = row_number - 1
    if endrow == -1:
        endrow = len(input_list) - 1
    return [startrow, endrow]


def turnlineintoint(kist):
    intagaer = [int(a) for a in kist]
    return intagaer


def reformat(trans: list) -> list:
    retu = [rowk.split() for rowk in trans]
    turninint = []
    for row in retu:
        turninint.append(turnlineintoint(row))
    return turninint


def get_map_formated(i):
    lines = get_map(i)
    mylist = input_list[lines[0]:lines[1]]
    formatt = reformat(mylist)
    return formatt


def get_seedoutput(seed, mapz):
    for row in mapz:
        if row[1] <= seed <= row[1] + row[2] - 1:
            seed = row[0] + seed - row[1]
            return seed
    return seed


def get_lowloc(seeds):
    for mapnum in maps:
        print(mapnum)
        map = get_map_formated(mapnum)
        newseeds = []
        k=0
        for seed in seeds:
            k+=1

            print(k,"/",len(seeds))
            refreshseed = get_seedoutput(seed, map)
            newseeds.append(refreshseed)
        seeds = newseeds
    return seeds


locs = get_lowloc(seeds)
print("part1 ",locs)
print(min(locs))

newseeds = []
for linenumb, line in enumerate(seeds):
    if linenumb % 2 == 0:
        start = line
    if linenumb % 2 != 0:
        newline = [kaka for kaka in range(start, start + line)]
        newseeds.extend(newline)
        #print(newseeds)

locs = get_lowloc(newseeds)

print("part2 ",locs)
print(min(locs))