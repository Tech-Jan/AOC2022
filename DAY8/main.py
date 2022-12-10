from filereader import readfile

a=readfile("input")
print(a)

# print(a[2][4])

i=1
i_len=len(a[0])
print(i_len)
b=1
b_len = len (a)
print(b_len)


def maxs_r_to_l():
    counter = 0
    coord = []
    for b in range(0,b_len):
        #print(a[b])
        max=int(a[b][0])
        coord.append([b, 0])
        for i in range(0,i_len):
            k=i
            #print(a[b][i])
            c=int(a[b][i])
            if c > max:
                max=c
                coord.append([b,i])
                counter+=1
    return coord
print(maxs_r_to_l())

def maxs_l_to_r():
    counter = 0
    coord = []
    for b in range(0,b_len):
        print(a[b])
        max=int(a[b][i_len-1])
        coord.append([b,i_len-1])
        for i in range(1,i_len):
            k=i
            print(a[b][i_len-i])
            c=int(a[b][i_len-i])
            if c > max:
                max=c
                coord.append([b, i_len-i])
                counter+=1
    return coord

def maxs_t_to_b():
    counter = 0
    coord = []
    for i in range(0,i_len):
        #print(a[b])
        max=int(a[0][i])
        coord.append([0, i])
        #print(f"this iffs {max}")
        for b in range(0,b_len):
            k=i
            #print(a[b][i])
            c=int(a[b][i])
            if c > max:
                max=c
                # print(f"this is {max}")
                coord.append([b, i])
                counter+=1
    return coord

def maxs_b_to_t():
    counter = 0
    coord = []
    for i in range(0,i_len):
        #print(a[b])
        max=int(a[b_len-1][i])
        coord.append([b_len-1, i])
        for b in range(1,b_len):
            k=i
            #print(a[b][i])
            c=int(a[b_len-b][i])
            if c > max:
                max=c
                # print(f"this is {max}")
                coord.append([b_len-b, i])
                counter+=1
    return coord
sumlist=[]
number1 = maxs_r_to_l()

number2 = maxs_l_to_r()
number3 = maxs_t_to_b()
number4 = maxs_b_to_t()

for number in number1:
    sumlist.append(tuple(number))

for number in number2:
    sumlist.append(tuple(number))
for number in number3:
    sumlist.append(tuple(number))
for number in number4:
    sumlist.append(tuple(number))

print(sorted((set(sorted(sumlist)))))
print(len(set(sumlist)))
print(i_len)
print(b_len)
print(number4)



print(a[4][i_len-1])