import ast
import os
import pprint
import string
import time

import colorama
import pandas as pd

from map import Map, Labyrinth
from objects import Elf, End, Elf_Army

# the command to clear is `cls` on Windows and `clear` on most everything else
clear = lambda: os.system('cls')

pp = pprint.PrettyPrinter(width=4000)
pd.set_option("display.max_columns", None)


def coords_dictionary():
    abc = dict(zip(string.ascii_lowercase, range(1, 27)))
    abc["E"] = 26
    abc["S"] = 1

    return abc


def main():
    # part1
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
    #
    #
    lab.search_end(end, my_elf_army, lab, my_map, abc, )

    # part2
    my_elf_army2 = Elf_Army()
    lab2 = Labyrinth()
    # print(lab2.movescape)
    new_ground = Elf()
    new_ground.name = "a"
    starting_positions = my_map.find_coords("a", landscape, abc, multi=True)
    # print(starting_positions)
    for starting_position in starting_positions:
        new_elf = Elf()
        new_elf.move(new_elf.current_pos, starting_position, landscape, lab2.movescape)
        my_elf_army2.army.append((new_elf))
    # print(lab2.movescape.to_string(index=False))
    lab2.paths = [[{'x': 1, 'y': 0, 'z': 1}]]
    #
    #
    # lab.search_end(end, my_elf_army2, lab2, my_map, abc, )

    # part3
    with open("C:\\Users\\trewe\PycharmProjects\AOC2022\Day12\src\mypath", "r") as f:
        my_path = f.read()
    my_path = my_path.split("\n")
    wanderer = Elf()
    lab3 = Labyrinth()
    colorama.init(autoreset=True)
    # print(Fore.RED + my_map.landscape.to_string(index=False, header=False))
    lab3.movescape = my_map.landscape
    lab3.give_colors(abc)
    print(lab3.movescape.to_string(index=False, header=False))

    for step in my_path:
        try:
            ast.literal_eval(step)
        except:
            break
        else:
            step = ast.literal_eval(step)

        wanderer.move(wanderer.current_pos, step, my_map.landscape, lab3.movescape)
        time.sleep(0.03)
        clear()
        print(f"{lab3.movescape.to_string(index=False, header=False)}", end="\r")

    for i in range(200):
        time.sleep(0.1)
        print(lab3.movescape.to_string(index=False, header=False))


if __name__ == "__main__":
    main()
    # 6816 to high
