import pprint
import string
import time

import pandas as pd

from map import Map, Labyrinth
from objects import Elf, End, Elf_Army

pp = pprint.PrettyPrinter(width=4000)
pd.set_option("display.max_columns", None)


def coords_dictionary():
    abc = dict(zip(string.ascii_lowercase, range(1, 27)))
    abc["E"] = 26
    abc["S"] = 1

    return abc


def main():
    #part1
    # get enumerated dictionary
    abc = coords_dictionary()
    # get my_map as dataframe
    my_map = Map()
    landscape = my_map.landscape
    # create my elfarmy and endpoint
    my_elf_army = Elf_Army()
    me = Elf()
    me.current_pos = my_map.find_coords(me.name, landscape, abc)
    my_elf_army.army.append(me)
    end = End()
    end.current_pos = my_map.find_coords(end.name, landscape, abc)
    lab = Labyrinth()

    # find start coords
    me.current_pos = my_map.find_coords(me.name, landscape, abc)
    lab.movescape[me.current_pos["x"]][me.current_pos["y"]] = 1
    z = 0
    found_end = False
    while not found_end:
        possible_xyz = []
        for b in range(len(my_elf_army.army)):
            elf = my_elf_army.army[b]
            new_possible_xyz = lab.possible_moves(elf.current_pos, my_map, lab.movescape, abc)
            for item in new_possible_xyz:
                if item not in possible_xyz:
                    possible_xyz.append(item)
        my_elf_army.army = []

        for xyz in (possible_xyz):
            newme = Elf()
            newme.move(newme.current_pos, xyz, landscape, lab.movescape)
            my_elf_army.army.append(newme)
            if newme.current_pos == end.current_pos:
                z += 1
                print("UUU DUUUDIIIDIIIT")
                print(z)
                found_end=True
                break
        z += 1
        # print(lab.movescape.to_string(index=False))

    #part2
    my_elf_army2=Elf_Army()
    lab2 = Labyrinth()
    print(lab2.movescape)
    new_ground = Elf()
    new_ground.name="a"
    starting_positions=my_map.find_coords("a",landscape,abc,multi=True)
    print(starting_positions)
    for starting_position in starting_positions:
        new_elf=Elf()
        new_elf.move(new_elf.current_pos,starting_position,landscape,lab2.movescape)
        my_elf_army2.army.append((new_elf))
    print(lab2.movescape.to_string(index=False))
    lab2.path=[[{'x': 1, 'y': 0, 'z': 1}]]
    z=0
    found_end = False
    while not found_end:
        possible_xyz = []
        for b in range(len(my_elf_army2.army)):
            elf = my_elf_army2.army[b]
            new_possible_xyz = lab2.possible_moves(elf.current_pos, my_map, lab2.movescape, abc)
            for item in new_possible_xyz:
                if item not in possible_xyz:
                    possible_xyz.append(item)

        # lab2.path = [path for path in lab2.path if len(path) > z-1]
        # for xyz in (possible_xyz):
        #     lab2.path.append(lab2.path[0])
        #     for path in lab2.path:
        #         for elf in my_elf_army2.army:
        #             if elf.current_pos in path:
        #                 path.append(xyz)
        #                 testvar=len(path)


        my_elf_army2.army = []
        for xyz in (possible_xyz):


            newme = Elf()
            newme.move(newme.current_pos, xyz, landscape, lab2.movescape)
            my_elf_army2.army.append(newme)


            if newme.current_pos == end.current_pos:
                z += 1
                print("UUU DUUUDIIIDIIIT")
                print(z)
                found_end=True
                break



        time.sleep(0.1)
        #print(lab2.movescape.to_string(index=False))
        z += 1
        # pp.pprint (lab2.path)
        # print(len(lab2.path[0]))



if __name__ == "__main__":
    main()
    # 6816 to high
