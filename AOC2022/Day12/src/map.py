import copy

import filereader
from objects import *


class Map:

    def __init__(self):
        self.height = -1
        self.width = -1
        self.landscape = self.read_input()

    def read_input(self):
        raw_data = filereader.readfile("D:\python\pycharmprojects\AOC2022\AOC2022\Day12\input\input")
        data_frame = pd.DataFrame(raw_data)
        self.height = data_frame.shape[0] - 1
        self.width = data_frame.shape[1] - 1
        return data_frame

    def get_z(self, x: int, y: int, landscape: pd.DataFrame, abc: dict) -> int:
        height = abc[landscape.loc[y, x]]
        return height

    def find_coords(self, searched_value: str, map: pd.DataFrame, abc: dict, multi=False) -> dict:
        coords = map.where(map == searched_value).stack()
        if multi:
            list_coords = []
            xy = pd.MultiIndex.to_list(coords.index)
            for coord in xy:
                y, x = coord
                if searched_value in abc:
                    z = abc[searched_value]
                my_coords = {"x": x,
                             "y": y,
                             "z": z, }
                list_coords.append(my_coords)

            return list_coords
        else:
            y, x = pd.MultiIndex.to_list(coords.index)[0]

            if searched_value in abc:
                z = abc[searched_value]
            else:
                print("ERROOR")
                z = -1
            my_coords = {"x": x,
                         "y": y,
                         "z": z, }
            return my_coords

    def in_landscape(self, x: int, y: int) -> bool:
        if self.width >= x >= 0 and self.height >= y >= 0:
            return True
        else:
            return False


class Labyrinth(Map):
    def __init__(self):
        super().__init__()
        self.name = "Lab"
        self.paths = []
        self.movescape = self.landscape.where(self.landscape == "R").fillna("0")

    def possible_moves(self, xyz: dict, my_map: Map, moves_scape: Map, abc: dict) -> list:
        x, y, z = xyz["x"], xyz["y"], xyz["z"]
        possible_moves = []
        new_x = x + 1
        new_y = y
        self.is_possible(xyz, new_x, new_y, my_map, moves_scape, abc, possible_moves)

        new_x = x - 1
        new_y = y
        self.is_possible(xyz, new_x, new_y, my_map, moves_scape, abc, possible_moves)

        new_x = x
        new_y = y + 1
        self.is_possible(xyz, new_x, new_y, my_map, moves_scape, abc, possible_moves)

        new_x = x
        new_y = y - 1
        self.is_possible(xyz, new_x, new_y, my_map, moves_scape, abc, possible_moves)

        return possible_moves

    def is_possible(self, xyz: dict, new_x: int, new_y: int, my_map: Map, movescap: Map, abc: dict,
                    possible_moves: list):
        x, y, z = xyz["x"], xyz["y"], xyz["z"]
        if my_map.in_landscape(new_x, new_y):
            new_z = self.get_z(new_x, new_y, my_map.landscape, abc)
            if int(movescap[new_x][new_y]) < 1 and (new_z - z) < 2:
                new_xyz = {"x": new_x,
                           "y": new_y,
                           "z": new_z, }
                possible_moves.append(new_xyz)

    def move_choice(self, possible_moves: list, movescape: pd.DataFrame) -> dict:
        old_value = 10000000

        for xyz in possible_moves:
            x, y, z = xyz["x"], xyz["y"], xyz["z"]
            value = int(movescape[x][y])
            if value < old_value:
                new_x = x
                new_y = y
                new_z = z
                old_value = value
        if possible_moves != []:
            new_xyz = {"x": new_x,
                       "y": new_y,
                       "z": new_z, }

            return new_xyz

    def start_path(self, elf_army: Elf_Army, possible_xyz: list):
        for elf in elf_army.army:
            self.paths.append([elf.current_pos])

    def write_path(self, elf_army: Elf_Army, possible_xyz: list):
        for elf in elf_army.army:
            for path in self.paths:
                if path[-1] == elf.current_pos:

                    for pos in possible_xyz:
                        if abs(elf.current_pos["x"] - pos["x"]) + abs(elf.current_pos["y"] - pos["y"]) < 2 and pos["z"] - elf.current_pos["z"] <=1:
                            if not any(pos in sublist for sublist in self.paths):
                                self.paths.append(copy.deepcopy(path))
                                self.paths[-1].append(pos)
                    # print(path)

    def del_stopped_path(self):
        maxi = max(self.paths, key=len)
        i = 0
        newlist = [path for path in self.paths if len(path) == len(maxi)]
        self.paths = newlist

        # for path in self.paths:
        #     pass

    def search_end(self, target: Elf, elf_army: Elf_Army, lab, cur_map: Map, abc: dict, ):
        self.paths = []
        possible_xyz = []
        z = 0
        found_end = False
        self.start_path(elf_army, possible_xyz)
        while not found_end:
            possible_xyz = []
            for b in range(len(elf_army.army)):
                elf = elf_army.army[b]
                new_possible_xyz = lab.possible_moves(elf.current_pos, cur_map, lab.movescape, abc)
                for item in new_possible_xyz:
                    if item not in possible_xyz:
                        possible_xyz.append(item)
            self.write_path(elf_army, possible_xyz)
            self.del_stopped_path()
            elf_army.army = []

            for xyz in (possible_xyz):
                newme = Elf()
                newme.move(newme.current_pos, xyz, cur_map.landscape, lab.movescape)
                elf_army.army.append(newme)
                if newme.current_pos == target.current_pos:
                    z += 1
                    print("UUU DUUUDIIIDIIIT")
                    print(z)
                    for path in self.paths:
                        if path[-1] == target.current_pos:
                            print(path)
                            with open("mypath", "w") as file:
                                for step in path:
                                    file.write(f"{str(step)}\n")
                    found_end = True
                    break

            z += 1
            print(z)
            # print(lab.movescape.to_string(index=False))

    def give_colors(self, abc: dict):

        # self.movescape = self.landscape.where(self.landscape == "a").fillna(Fore.GREEN+"0")
        for key in abc:
            value = abc[key]
            style = {1: "DIM",
                     2: "NORMAL",
                     3: "BRIGHT",
                     }
            print(value)
            u = 1
            if value == u:
                self.movescape.replace(key, Fore.GREEN + key, inplace=True)
            u += 1
            if value == u:
                self.movescape.replace(key, Fore.LIGHTGREEN_EX + key, inplace=True)
            u += 1
            if value == u:
                self.movescape.replace(key, Fore.YELLOW + key, inplace=True)

            u += 1
            if value == u:
                self.movescape.replace(key, Fore.LIGHTYELLOW_EX + key, inplace=True)
            u += 1
            if value == u:
                self.movescape.replace(key, Fore.RED + key, inplace=True)
            u += 1
            if value == u:
                self.movescape.replace(key, Fore.LIGHTRED_EX + key, inplace=True)
            u += 1
            if value == u:
                self.movescape.replace(key, Fore.BLACK + key, inplace=True)
            u += 1
            if value == u:
                self.movescape.replace(key, Fore.BLACK + key, inplace=True)
            u += 1
            if value == u:
                self.movescape.replace(key, Fore.BLACK + key, inplace=True)
            u += 1
            if value == u:
                self.movescape.replace(key, Fore.LIGHTBLACK_EX + key, inplace=True)
            u += 1
            if value == u:
                self.movescape.replace(key, Fore.LIGHTBLACK_EX + key, inplace=True)
            u += 1
            if value == u:
                self.movescape.replace(key, Fore.LIGHTBLACK_EX + key, inplace=True)
            u += 1
            if value == u:
                self.movescape.replace(key, Fore.MAGENTA + key, inplace=True)
            u += 1
            if value == u:
                self.movescape.replace(key, Fore.LIGHTMAGENTA_EX + key, inplace=True)
            u += 1
            if value == u:
                self.movescape.replace(key, Fore.CYAN + key, inplace=True)
            u += 1
            if value == u:
                self.movescape.replace(key, Fore.LIGHTCYAN_EX + key, inplace=True)
            u += 1
            if value == u:
                self.movescape.replace(key, Fore.BLUE + key, inplace=True)
            u += 1
            if value == u:
                self.movescape.replace(key, Fore.BLUE + key, inplace=True)
            u += 1
            if value == u:
                self.movescape.replace(key, Fore.LIGHTBLUE_EX + key, inplace=True)
            u += 1
            if value == u:
                self.movescape.replace(key, Fore.LIGHTBLUE_EX + key, inplace=True)
            u += 1
            if value == u:
                self.movescape.replace(key, Fore.WHITE + key, inplace=True)
            u += 1
            if value >= u:
                self.movescape.replace(key, Fore.LIGHTWHITE_EX + key, inplace=True)

            else:
                self.movescape.replace(key, Fore.BLACK + key, inplace=True)
            self.movescape.replace("E", Fore.RED + "E", inplace=True)
