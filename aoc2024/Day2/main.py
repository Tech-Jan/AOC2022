import reader


input_raw = reader.read_input("input.txt")
input = [list(map(int, x.split())) for x in input_raw]
dampened_list = []


def dampener(levels: list, index: int):
    del levels[index]
    return levels


def damp_system(levels: list, index: int, curr_level):
    damps = []
    global dampened_list
    for i in range(-1, 2):
        corrected = dampener(levels.copy(), index + i)
        dampened_list.append([curr_level, corrected.copy()])


def give_levels(report: str):
    levels_str = report.split()
    levels_int = [int(x) for x in levels_str]
    return levels_int


def safetycheck1(levels: list, currlev: int):
    decreasing = True
    increasing = True
    value = levels[0]
    dampened_status = 0
    for index, level in enumerate(levels[1:]):
        if level >= value:
            decreasing = False
        if level <= value:
            increasing = False
        if decreasing == False and increasing == False:
            damp_system(levels.copy(), index, currlev)
        value = level
    if decreasing == True or increasing == True:
        return True
    else:
        return False


def safetycheck2(levels: list, currlev: int):
    differcheck = True
    value = levels[0]
    dampened_status = 0
    for index, level in enumerate(levels[1:]):
        differ = abs(value - level)
        if differ < 1 or differ > 3:
            differcheck = False
            damp_system(levels.copy(), index, currlev)
        value = level
    return differcheck


safe_reps_part1 = []

def part1(input):
    safe_reports = 0
    global safe_reps_part1
    for currlev, report in enumerate(input):
        safety1 = safetycheck1(report, currlev)
        safety2 = safetycheck2(report, currlev)
        if safety1 and safety2:
            safe_reports += 1
            safe_reps_part1.append(currlev)
    return safe_reports


saferesulst1 = part1(input)




def part2(input):
    safe_reports = 0
    saved_index = []
    for report in input:
        safe = False
        safety1 = safetycheck1(report[1], report[0])
        safety2 = safetycheck2(report[1], report[0])

        if safety1 and safety2 and report[0] not in saved_index:
            safe_reports += 1
            saved_index.append(report[0])
            safe = True
        #print(report, safe)
    # temp3 = [item for item in safetasline if item not in saved_index and item not in safe_reps_part1]
    # print(safetasline)
    # print(saved_index)
    # print(temp3)

    return safe_reports


newshit = dampened_list.copy()
listofindex = [x[0] for x in newshit]

# print(dampened_list)
saferesults2 = part2(newshit)
print(saferesulst1)
print(saferesults2)

print("xxx")
print("part2result=", saferesulst1 + saferesults2)
