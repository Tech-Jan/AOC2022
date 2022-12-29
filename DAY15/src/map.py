import pandas as pd

from DAY15.input.filereader import filereader

FILE = "../input/input"


class Cave:
    def __init__(self):
        self.data = filereader(FILE)
        self.objects = []
        self.datareader()
        self.map_size = {}

        self.dataframe = None

        self.signals=set([])



    def paint_map(self,signals:list):
        for signal in signals:
            self.dataframe[signal[0]][signal[1]]="#"

    def dataframe_creator(self):
        if self.map_size["max_x"] < 1000:
            dataframe = pd.DataFrame(index=range(self.map_size["min_y"], self.map_size["max_y"] + 1),
                                     columns=range(self.map_size["min_x"], self.map_size["max_x"] + 1))
            self.dataframe = dataframe

    def datareader(self):
        for sensorbeacon in self.data:
            sensor = sensorbeacon[0]
            beacon = sensorbeacon[1]
            sensor = Sensor(sensor[0], sensor[1],self)
            beacon = Beacon(beacon[0], beacon[1],self)
            sensor.closest_beacon = beacon
            beacon.closest_sensor = sensor
            self.objects.append(sensor)
            self.objects.append(beacon)

    def mapsize(self):
        mapsize = {"max_x": 20,
                   "max_y": 20,
                   "min_x": 0,
                   "min_y": 0, }

        # max_x_object = max(self.signals, key=lambda obj: obj[0])
        # mapsize["max_x"] = max_x_object[0]
        # max_y_object = max(self.signals, key=lambda obj: obj[1])
        # mapsize["max_y"] = max_y_object[1]
        # min_x_object = min(self.signals, key=lambda obj: obj[0])
        # mapsize["min_x"] = min_x_object[0]
        # min_y_object = min(self.signals, key=lambda obj: obj[1])
        # mapsize["min_y"] = min_y_object[1]
        self.map_size = mapsize





class Objects:

    def __init__(self, x: int, y: int, cave:Cave):
        self.coords = {"x": x, "y": y}
        self.cave=cave


class Sensor(Objects):
    instances = []

    def __init__(self, *args):
        super().__init__(*args)
        self.name = "Sensor"
        self.closest_beacon = None
        self.__class__.instances.append(self)
        self.distance=0



    def distances(self):
        distance_x = abs(self.closest_beacon.coords["x"] - self.coords["x"])
        distance_y = abs(self.closest_beacon.coords["y"] - self.coords["y"])
        self.distance= distance_x + distance_y

    @property
    def signal(self):
        linex=20
        liney=20
        signals = set([])
        print("NEXT")
        signals.add((self.coords["x"], self.coords["y"]))
        for b in range(0, self.distance+1):
            print(len(signals))
            for j in range(0,self.distance+1-b):
                signalx = self.coords["x"] + b
                signaly = self.coords["y"] + j
                if self.cave.map_size["max_x"]>=signalx>=self.cave.map_size["min_x"] and self.cave.map_size[
                    "max_y"]>=signaly>=self.cave.map_size["min_y"]:
                    signals.add((signalx, signaly))
                signalx = self.coords["x"] - b
                signaly = self.coords["y"] + j
                if self.cave.map_size["max_x"]>=signalx>=self.cave.map_size["min_x"] and self.cave.map_size[
                    "max_y"]>=signaly>=self.cave.map_size["min_y"]:
                    signals.add((signalx, signaly))
                signalx = self.coords["x"] + b
                signaly = self.coords["y"] - j
                if self.cave.map_size["max_x"]>=signalx>=self.cave.map_size["min_x"] and self.cave.map_size[
                    "max_y"]>=signaly>=self.cave.map_size["min_y"]:
                    signals.add((signalx, signaly))
                signalx = self.coords["x"] -b
                signaly = self.coords["y"] - j
                if self.cave.map_size["max_x"]>=signalx>=self.cave.map_size["min_x"] and self.cave.map_size[
                    "max_y"]>=signaly>=self.cave.map_size["min_y"]:
                    signals.add((signalx, signaly))
        for signal in signals:
            self.cave.signals.add(signal)
        return set(signals)


    def signal_part2(self,line:int) -> list:


        if abs(self.coords["y"]-line)<=abs(self.distance):
            myrange=abs(self.distance-abs(self.coords["y"]-line))

            start=self.coords["x"]-(myrange)+1
            end= self.coords["x"]+myrange

            start-=1
            if start < 0 and end >0:
                start=0
            if start < 4000000 and end >4000000:
                end=4000000
            my_range=[start,end]
            return [True,my_range]
        else:
            return [False,[0,0]]




    def signalx(self,line):

        objectx = self.coords["x"]
        objecty = self.coords["y"]
        signals = set([])


        if self.coords["y"]>line:
            for b in range(0, self.distance+1):
                if self.coords["y"]-b==line:
                    for j in range(0,self.distance+1-b):
                        signalx = self.coords["x"] + j
                        signaly = self.coords["y"] - b
                        signals.add((signalx, signaly))
                        signalx = self.coords["x"] - j
                        signaly = self.coords["y"] - b
                        signals.add((signalx, signaly))
        elif self.coords["y"]<=line:
            for b in range(0, self.distance+1):
                if self.coords["y"]+b==line:

                    for j in range(0,self.distance+1-b):
                        signalx = self.coords["x"] + j
                        signaly = self.coords["y"] + b
                        signals.add((signalx, signaly))
                        signalx = self.coords["x"] - j
                        signaly = self.coords["y"] + b
                        signals.add((signalx, signaly))
        for signal in signals:
            self.cave.signals.add(signal)
        return set(signals)





class Beacon(Objects):
    instances = []

    def __init__(self, *args):
        super().__init__(*args)
        self.name = "Beacon"
        self.closest_sensor = None
        self.__class__.instances.append(self)

    @property
    def distance(self):
        distance_x = abs(self.closest_sensor.coords["x"] - self.coords["x"])
        distance_y = abs(self.closest_sensor.coords["y"] - self.coords["y"])
        return distance_x + distance_y
