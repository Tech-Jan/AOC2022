def filereader(file):
    with open(file, "r") as f:
        cave=Cave()
        for line in f:
            create_valve_flow(cave,line)
    with open(file, "r") as f:
        for line in f:
            create_tunnel(cave,line)

    return cave

def create_tunnel(cave,line):
    current_line = line
    for valve in cave.valves:
        if valve.name==current_line[6:8]:
            current_valve = valve
    tunnels = current_line[current_line.find("valve"):]
    tunnels = tunnels.split(" ")
    tunnels.pop(0)
    tunnels[-1] = tunnels[-1][0:2]

    for tunnel in tunnels:
        if len(tunnel)==3:
            tunnel=tunnel[0:2]
        for valve in cave.valves:
            if valve.name == tunnel:
                adjacent_valve=valve
        current_valve.adjacent_valves.append(adjacent_valve)


def create_valve_flow(cave,line):
    current_line = line
    my_valve = Valve()
    my_valve.name = current_line[6:8]
    my_valve.flowrate = int(current_line[current_line.find("=") + 1:current_line.find(";")])
    cave.valves.append(my_valve)





class Valve:
    def __init__(self):
        self.name="None"
        self.flowrate="0"
        self.adjacent_valves=[]
        self.open=False

class Human:
    def __init__(self):
        self.pos=None

class Cave:
    def __init__(self):
        self.name="lol"
        self.valves= []
        self.sum_flow=0
        self.current_flow=0

    def count_needed_moves(self, current_valve:Valve, searched_valve:Valve):
        current_valve = [current_valve]
        moves=0
        while searched_valve not in current_valve:
            for i in range(len(current_valve)):
                valve=current_valve[i]
                for adjacent_valve in valve.adjacent_valves:
                    current_valve.append(adjacent_valve)
            moves+=1
        return moves


class Path:
    def __init__(self):
        self.moves=0
        self.current_flow=0
        self.sum_flow=0
        self.path=[]
        self.current_position=None


