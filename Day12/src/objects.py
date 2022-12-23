import pandas as pd

from map import *


class Elf:
    def __init__(self):
        self.name = "S"

        self.current_pos = {"x": -1,
                            "y": -1,
                            "z": -1, }
        self.path = []
        self.moved = False

    @property
    def x(self):
        return self.current_pos["x"]

    @property
    def y(self):
        return self.current_pos["y"]

    @property
    def z(self):
        return self.current_pos["z"]

    def move(self, xyz :dict, new_xyz: dict, map: pd.DataFrame, movescape:pd.DataFrame) -> dict:
        if new_xyz is not None:
            x, y, z = xyz["x"], xyz["y"], xyz["z"]
            new_x, new_y, new_z = new_xyz["x"], new_xyz["y"], new_xyz["z"]
            xyz["x"], xyz["y"], xyz["z"] = new_x, new_y, new_z
            self.path.append([new_x,new_y,new_z])
            movescape[new_x][new_y]=int(movescape[new_x][new_y])+1
            return xyz


class End:
    def __init__(self):
        self.name = "E"
        self.current_pos = {}

class Elf_Army():
    def __init__(self):
        self.army=[]
        self.numbermoves=0



