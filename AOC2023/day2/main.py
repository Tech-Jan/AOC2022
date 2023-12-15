def read_input(file):
    with open(file) as input:
        input=input.read()
        output= input.split("\n")
    return output

input_list=read_input("input.txt")

i=0

rules={"red":12,
       "green":13,
       "blue":14}
def check(rule):
    number,color=rule
    if rules[color] >= int(number):
        return 1
    else:
        return 0


def minsballs(rule):
        number, color = rule
        return int(number),color

solution2=0
for round in input_list:
    input = round.split(":")[1].split(";")
    possible = []
    minsballs_dict={"red":0,
       "green":0,
       "blue":0}

    for game in input:
        c=[i.split(" ") for i in  game[1:].split(", ")]

        for item in c:
            possible.append(check(item))
            number,color=minsballs(item)
            if minsballs_dict[color]<number:
                minsballs_dict[color]=number

        product=1
    for val in minsballs_dict.values():
        product*=val
    solution2+=product


    if 0 not in possible:
        kaka=int(round.split(":")[0].split(" ")[1])
        print(kaka,input)
        i+=int(round.split(":")[0].split(" ")[1])

print(i)
print(solution2)