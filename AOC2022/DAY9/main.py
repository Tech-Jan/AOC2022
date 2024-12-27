from filereader import readfile
from copy import deepcopy
from painters import paint_head, paint_head2

commands = readfile("D:\python\pycharmprojects\AOC2022\AOC2022\DAY9\input")
# commands = readfile("/home/jew/PycharmProjects/AOC2022/DAY9/testinput")

pos_h = [0, 0]
pos_h_list = []
pos_t = [0, 0]
pos_t_list = []


def move_h(direction, currentpos_h):
    if direction == "R":
        currentpos_h[0] += 1
    if direction == "L":
        currentpos_h[0] -= 1
    if direction == "U":
        currentpos_h[1] += 1
    if direction == "D":
        currentpos_h[1] -= 1
    return currentpos_h


def get_command(command, pos_h, pos_t):
    direction = command[:1]
    amount = int(command[1:])
    for i in range(0, amount):
        pos_h = move_h(direction, pos_h)
        pos_h_list.append(list(pos_h))
        pos_t = move_t(pos_h, pos_t)
    return pos_h, pos_t


def move_t(currentpos_h, currentpos_t):
    hx, hy = currentpos_h
    tx, ty = currentpos_t
    distance = ((hx - tx) ** 2 + (hy - ty) ** 2) ** 0.5
    if distance > 2 ** 0.5:
        currentpos_t = pos_h_list[-2]
    pos_t_list.append(currentpos_t)
    return currentpos_t


for command in commands:
    pos_h, pos_t = get_command(command, pos_h, pos_t)

abc = []
for pos in pos_t_list:
    add = (pos[0], pos[1])
    abc.append(add)
print(len(set(abc)))
# paint_head(pos_h_list,pos_t_list)
'''end of part 1'''
'''start of part 2'''


def get_command2(command, positions_snake):
    direction = command[:1]
    amount = int(command[1:])
    for b in range(0, amount):
        positions_snake[0] = move_h(direction, positions_snake[0])
        # pos_h_list.append(list(positions_snake[0]))
        for i in range(1, len(positions_snake)):
            positions_snake = move_t2(positions_snake, i)
        klara = deepcopy(positions_snake)
        positions_snake_list.append(klara)
    return positions_snake


def move_t2(positions_snake, i):
    hx, hy = positions_snake[i - 1]
    tx, ty = positions_snake[i]
    x, y = hx - tx, hy - ty
    abs_x = abs(x)
    abs_y = abs(y)
    if abs_x > 1 or abs_y > 1:
        positions_snake[i][0] = positions_snake[i][0] + (0 if x == 0 else x // abs_x)
        positions_snake[i][1] = positions_snake[i][1] + (0 if y == 0 else y // abs_y)
        return positions_snake

    return positions_snake

    # distance = ((hx - tx) ** 2 + (hy - ty) ** 2) ** 0.5
    # if distance > 2 ** 0.5:
    #     if hy > ty:
    #         positions_snake[i][0],positions_snake[i][1] =
    #         positions_snake_list[-1][i - 1][0],positions_snake_list[-1][i - 1][1]
    #     else:
    #         positions_snake[i] = positions_snake_list[-1][i - 1]
    # return positions_snake


pos_h_list = []
positions_snake = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
positions_snake_list = []

for command in commands:
    positions_snake = get_command2(command, positions_snake)

abc = []
for pos in positions_snake_list:
    loss = tuple(pos[-1])
    abc.append(loss)
print(abc)
print(len(set(abc)))

paint_head2(positions_snake_list)
