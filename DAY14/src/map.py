import time

import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

MAP_INPUT = "..\input\\input"

with open(MAP_INPUT, "r") as myinput:
    myinput = [line.split("->") for line in myinput.read().split("\n")]

stone_vector_list = [[{"item": "stone",
                       "x": int(val.split(",")[0]),
                       "y": int(val.split(",")[1])} for val in item] for item in myinput]

max_x = max(val["x"] for item in stone_vector_list for val in item)
max_y = max(val["y"] for item in stone_vector_list for val in item)
min_x = min(val["x"] for item in stone_vector_list for val in item)
min_y = min(val["y"] for item in stone_vector_list for val in item)
map_size = {"max_x": max_x,
            "max_y": max_y,
            "min_x": min_x,
            "min_y": min_y}


class Cave:
    def __init__(self):
        self.stone_vector_list = stone_vector_list
        self.items = self.stones(self.stone_vector_list)
        self.sand_particles = []
        self.map_size = map_size
        self.map = self.mapstyler(self.map_size)
        self.size_y = self.map_size["max_y"] - self.map_size["min_y"]
        self.size_x = self.map_size["max_x"] - self.map_size["min_x"]
        self.paint_stones()
        self.cave_full=False

    def mapstyler(self, map_size: dict):
        size_y = map_size["max_y"] - map_size["min_y"] + 10
        size_x = map_size["max_x"] - map_size["min_x"] + 10
        mymap = pd.DataFrame(index=[map_size["min_y"] - 5 + i for i in range(size_y)],
                             columns=[map_size["min_x"] - 5 + i for i in range(size_x)])
        mymap.fillna(".", inplace=True)
        return mymap

    def stones(self, stone_vector_list: list):
        stone_list = [vector for row in stone_vector_list for vector in row]
        for row in stone_vector_list:
            start_vector = row[0]
            for vector_point in row[1:]:
                delta_x, delta_y = [vector_point["x"] - start_vector["x"],
                                    vector_point["y"] - start_vector["y"]]
                if delta_y != 0:
                    sign = int(delta_y / (abs(delta_y)))
                    newlist = [{"item": "stone",
                                "x": start_vector["x"],
                                "y": y} for y in range(start_vector["y"], vector_point["y"], sign)]
                    newlist.pop(0)
                    for item in newlist:
                        stone_list.append(item)
                    start_vector = vector_point

                elif delta_x != 0:
                    sign = int(delta_x / (abs(delta_x)))
                    newlist = [{"item": "stone",
                                "x": x,
                                "y": start_vector["y"]} for x in range(start_vector["x"], vector_point["x"], sign)]
                    newlist.pop(0)
                    for item in newlist:
                        stone_list.append(item)
                    start_vector = vector_point
                else:
                    print("This shouldnt happen")
                    exit()
        return stone_list

    def paint_stones(self):
        self.map = self.mapstyler(self.map_size)
        for item in self.items:
            if item["item"] == "stone":
                self.map[item["x"]][item["y"]] = "#"
            if item["item"] == "sand":
                self.map[item["x"]][item["y"]] = "o"
        for item in self.sand_particles:
            self.map[item["x"]][item["y"]] = "o"
        self.map[500][0] = "x"


class Sand:
    def __init__(self):
        self.sand = "o"
        self.particles = []

    def paintsand(self, cave: Cave):
        cave.map[492][4] = "o"


class SandParticle(Sand):
    def __init__(self, cave: Cave):
        super().__init__()
        self.coord = {"item": "sand",
                      "x": 500,
                      "y": 1}
        self.cave = cave
        self.add_sand_to_map()

    def add_sand_to_map(self):
        self.cave.sand_particles.append(self.coord)

    def possible_moves(self):
        left = {"x": -1,
                "y": 1}
        right = {"x": 1,
                 "y": 1}
        down = {"x": 0,
                "y": 1}
        blocked = {"x": 0,
                   "y": 0}
        downblocked = False
        leftblocked = False
        rightblocked = False

        for item in self.cave.items:
            if item["x"] == self.coord["x"] + down["x"] and item["y"] == self.coord["y"] + down["y"]:
                downblocked = True

        for item in self.cave.items:
            if item["x"] == self.coord["x"] + left["x"] and item["y"] == self.coord["y"] + left["y"]:
                leftblocked = True

        for item in self.cave.items:
            if item["x"] == self.coord["x"] + right["x"] and item["y"] == self.coord["y"] + right["y"]:
                rightblocked = True
        if not downblocked:
            return down
        if not leftblocked:
            return left
        if not rightblocked:
            return right
        else:
            return blocked

    def check_full(self):
        if self.coord["y"]>self.cave.map_size["max_y"]:
            return False
        else:
            return True

    def fall(self):
        stone_roll = True
        while stone_roll:
            if self.check_full():
                possible_move = self.possible_moves()
                if possible_move["x"] == 0 and possible_move["y"] == 0:
                    self.cave.items.append(self.coord)
                    stone_roll = False
                    if len(self.cave.sand_particles)%20==0:
                        self.cave.paint_stones()
                        print(self.cave.map.to_string())

                else:
                    self.coord["x"] += possible_move["x"]
                    self.coord["y"] += possible_move["y"]
            else:
                stone_roll = False
                self.cave.cave_full=True
