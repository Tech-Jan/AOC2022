with open ("scores") as f:
    lines = f.read()
lines=lines.split("\n")

value_dict = {
        "A": 1,
        "B": 2,
        "C": 3,
        "X": 1,
        "Y": 2,
        "Z": 3,
        }

def compare(line):
    if value_dict[line[0]] == value_dict[line[2]]:
        return "draw"
    if value_dict[line[0]] < value_dict[line[2]]:
        if abs(value_dict[line[0]] - value_dict[line[2]]) == 1:
            return "win"
        else:
            return "lose"
    if value_dict[line[0]] > value_dict[line[2]] and abs(value_dict[line[0]] - value_dict[line[2]]) == 1:
        return "lose"
    else:
        return "win"

print(lines)
print (f)
points_sum = 0

for line in lines:
    points_sum +=value_dict[line[2]]
    if compare(line) == "lose":
        points_sum += 0
    elif compare(line) == "draw":
        points_sum += 3
    elif compare(line) == "win":
        points_sum += 6

    # print(line)
    # print(compare(line))
    # print(points_sum)

value_dict2 = {
        "A": 1,
        "B": 2,
        "C": 3,
        "X": "lose",
        "Y": "draw",
        "Z": "win",
        }
def compare2(line):
    if value_dict2[line[2]] == "draw":
        abc = line[0]
        line = abc + " "+ line[0]
        return line
    if value_dict2[line[2]] == "lose":
        if line[0] == "A":
            line = line[0] + " " + "C"
            return line
        elif line[0] == "B":
            line = line[0] + " " + "A"
            return line
        if line[0] == "C":
            line = line[0] + " " +  "B"
            return line
    if value_dict2[line[2]] == "win":
        if line[0] == "A":
            line = line[0] + " " + "B"
            return line
        elif line[0] == "B":
            line = line[0] + " " + "C"
            return line
        if line[0] == "C":
            line = line[0] + " " +  "A"
            return line
    else:
        return "non2"
i=0
for linepart2 in lines:
    lines[i] = compare2(linepart2)
    i += 1
print(lines)

points_sum=0

for line in lines:
    points_sum +=value_dict[line[2]]
    if compare(line) == "lose":
        points_sum += 0
    elif compare(line) == "draw":
        points_sum += 3
    elif compare(line) == "win":
        points_sum += 6

    print(line)
    print(compare(line))
    print(points_sum)
