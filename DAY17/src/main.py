import numpy as np

from objects import filereader, stones, map


def main():
    my_reader = filereader()
    my_data = my_reader.input
    my_stones = stones()
    my_map = map()
    move_down = [1, 0]

    stone_fell = 0
    move = [1, 0]
    steps = 0
    curr_s = 0
    schtep = 0
    IkA = 0
    stone_to_fall = 0
    add_heigh_min = 0
    height_after_2022 = 0
    go = True
    while stone_fell < 6000:
        current_stone = stone_fell % 5
        my_stones.current_object = my_stones.objects[current_stone]
        my_map.add_object(my_stones)
        notcrashed = True
        while notcrashed:

            if move == [1, 0]:
                current_step = steps % len(my_data)
                move = [0, my_data[current_step]]
                steps += 1
            else:
                move = move_down

            notcrashed = my_map.move(my_stones, move)

        my_map.landscape = my_map.landscape[~np.all(my_map.landscape == 0, axis=1)]
        stone_fell += 1

        if my_map.landscape.shape[0] // 2768 > curr_s:
            print("stoneFLEL", stone_fell, "stone diff", stone_fell - schtep)
            schtep = stone_fell
            print("LandscapeHEIH", my_map.landscape.shape[0], "Landscaheih diff", my_map.landscape.shape[0] - IkA)
            IkA = my_map.landscape.shape[0]
            curr_s += 1
            if go:
                stone_to_fall = 1382
                go = False
        if stone_to_fall == 1382:
            add_heigh_min = my_map.landscape.shape[0]
        if stone_to_fall == 0:
            add_heigh_max = my_map.landscape.shape[0]
            print("MYDIFF=", add_heigh_max - add_heigh_min)
            go = True
        stone_to_fall -= 1
        if stone_fell == 2022:
            height_after_2022 = my_map.landscape.shape[0]

    print("finish 2022part1", height_after_2022 - 1)
    # compare
    last_chance = 0
    for i in range(1, 9000):
        if np.array_equal(my_map.landscape[1:100], my_map.landscape[1 + i:100 + i]):
            repitition = i
            print(repitition - last_chance)
            last_chance = repitition

    # part2
    # stone fallen  till first repition starts =1778
    # height till first repition starts= 2770
    # stone fallen between repitition = 1755
    # heigh diff between repition = 2768
    # repitition= (1000000000000-1778)//1755
    # stone_to_fall_at the end = (1000000000000-1778)%1755 = 1382
    # MYDIFF= 2193 = stone_to_fall_at the end * height diff.
    # total height= (height_per_step * repitition) + start_height + missing height -(1)
    # total height=(2768*repitition)+2770+2193 (-1)


if __name__ == "__main__":
    main()
    # 1575402847027 to low
    # 1577207977187
