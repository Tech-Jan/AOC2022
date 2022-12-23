import pandas as pd

import filereader


class Map:

    def __init__(self):
        self.height = -1
        self.width = -1
        self.landscape = self.read_input()

    def read_input(self):
        raw_data = filereader.readfile("../input/input")
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
            list_coords=[]
            xy = pd.MultiIndex.to_list(coords.index)
            for coord in xy:
                y,x = coord
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
        self.path = []
        self.movescape=self.landscape.where(self.landscape=="R").fillna("0")

    def possible_moves(self, xyz: dict, my_map: Map,moves_scape: Map, abc: dict) -> list:
        x, y, z = xyz["x"], xyz["y"], xyz["z"]
        possible_moves = []
        new_x = x + 1
        new_y = y
        self.is_possible(xyz, new_x, new_y, my_map, moves_scape, abc, possible_moves)

        new_x = x - 1
        new_y = y
        self.is_possible(xyz, new_x, new_y, my_map,moves_scape, abc, possible_moves)

        new_x = x
        new_y = y + 1
        self.is_possible(xyz, new_x, new_y, my_map,moves_scape, abc, possible_moves)

        new_x = x
        new_y = y - 1
        self.is_possible(xyz, new_x, new_y, my_map,moves_scape, abc, possible_moves)

        return possible_moves

    def is_possible(self, xyz: dict, new_x: int, new_y: int, my_map: Map, movescap :Map, abc: dict, possible_moves: list):
        x, y, z = xyz["x"], xyz["y"], xyz["z"]
        if my_map.in_landscape(new_x, new_y):
            new_z = self.get_z(new_x, new_y, my_map.landscape, abc)
            if int(movescap[new_x][new_y]) < 1 and (new_z - z) < 2:
                new_xyz = {"x": new_x,
                           "y": new_y,
                           "z": new_z, }
                possible_moves.append(new_xyz)

    def move_choice(self,possible_moves:list,movescape:pd.DataFrame)->dict:
        old_value=10000000

        for xyz in possible_moves:
            x, y, z = xyz["x"], xyz["y"], xyz["z"]
            value=int(movescape[x][y])
            if value<old_value:
                new_x=x
                new_y=y
                new_z=z
                old_value=value
        if possible_moves != []:

            new_xyz = {"x": new_x,
                       "y": new_y,
                       "z": new_z, }

            return new_xyz


