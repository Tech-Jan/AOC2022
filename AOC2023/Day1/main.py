import copy


def read_input(file):
    with open(file) as input:
        input=input.read()
        output= input.split("\n")
    return output

input_list=read_input("input.txt")

##part1
def adder(input_list):
    result=0

    for line in input_list:
        number=[number for number in line if number.isnumeric()]
        print(line)
        result+=int(number[0]+number[-1])
        print(f"{number} +++ {result}")
    return result

result=adder(input_list)



##part2
numbers_dict={"one":1,
              "two":2,
              "three":3,
              "four":4,
              "five":5,
              "six":6,
              "seven":7,
              "eight":8,
              "nine":9}


input_list=read_input("input.txt")
def transform(input_list:list):
    outputs=[]
    for line in input_list:
        found= {}
        print(line)
        for number in numbers_dict.keys():
            index=0
            oldindex=-1
            while index!=oldindex:
                oldindex=index
                if number in line[index:]:
                    index=line[index:].find(number)+index
                    found[index]=numbers_dict[number]
                    index+=1

        for value in numbers_dict.values():
            index=0
            oldindex=-1
            while index!=oldindex:
                oldindex=index
                if str(value) in line[index:]:
                    index = line[index:].find(str(value))+index
                    found[index] = value
                    index+=1

        outputs.append(found)
    return outputs

transformed_input=transform(input_list)

print(transformed_input)



import re

nums = 'one|two|three|four|five|six|seven|eight|nine'
nums_re = re.compile(r'(?=(\d|%s))' % nums)
nums = nums.split('|')

with open('input.txt') as f:
    total = 0
    biglist=[]
    for line in f:
        digits = []
        for num in nums_re.findall(line):
            if num in nums:
                num = str(nums.index(num) + 1)
            digits.append(num)
        biglist.append(digits)
        total += int(digits[0] + digits[-1])
    print(total)

maxxxx = 0
i = 0
for index_dict in transformed_input:
    current = index_dict.items()
    print(current)
    mina = min(current, key=lambda t: t[0])
    maxa = max(current, key=lambda t: t[0])
    suma = str(mina[1]) + str(maxa[1])
    print(suma)
    correction=biglist[i][0] + biglist[i][-1]
    print(suma,correction)
    if suma!=correction:
        print("wrooooooong",i)
        exit()
    maxxxx += int(suma)
    i += 1
print(maxxxx)

