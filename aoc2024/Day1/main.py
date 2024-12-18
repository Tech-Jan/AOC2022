import reader

input=reader.read_input()
print(input)
vals_left=[]
vals_right=[]
for line in input:
    val_left,val_right=line.split()
    vals_left.append(int(val_left))
    vals_right.append(int(val_right))

def sorter(vals:list):
    sorted=[]

    while len(vals)>0:
        min = vals[0]
        i=0
        index=0
        for val in vals:
            if val < min:
                min=val
                index=i
            i+=1
        sorted.append(min)
        vals.pop(index)
    return sorted

def calculator(list1:list,list2:list):
    absolute_difference=0
    for index in range(len(list1)):
        print(list1[index])
        print(list2[index])
        absolute_difference += abs(list1[index]-list2[index])
    return absolute_difference



vals_left_sorted,vals_right_sorted=sorter(vals_left),sorter(vals_right)

result_star1=calculator(vals_left_sorted,vals_right_sorted)
print(result_star1)

def similarties(list1:list,list2:list):
    abs_sim=0
    for val1 in list1:
        counts=list2.count(val1)
        abs_sim+= counts*val1
    return abs_sim

result_star2=similarties(vals_left_sorted,vals_right_sorted)
print(result_star2)