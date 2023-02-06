from objects import *
from copy import deepcopy

indicies={'BB': 1, 'CC': 2, 'DD': 4, 'EE': 8, 'HH': 16, 'JJ': 32}
indiciesreal={'JT': 1, 'PH': 2, 'IR': 4, 'SV': 8, 'UV': 16, 'EZ': 32, 'KE': 64, 'OY': 128, 'NN': 256, 'FU': 512, 'PT': 1024, 'IF': 2048, 'TO': 4096, 'FC': 8192, 'QG': 16384}

def main():
    file="../input/input"
    cave=filereader(file)
    print(cave.valves)
    print(cave.valves[0].adjacent_valves)
    matrix=cave.floydwarshall()
    print(matrix)
    for item in matrix:
        for tak in item:
            if tak==0:
                matrix[matrix.index(item)][item.index(tak)]=10000
    print(matrix)

    def visit(valve, minutes, bitmask, pressure, answer):
        answer[bitmask] = max(answer.get(bitmask, 0), pressure)
        for valve2 in cave.valves:
            flow=valve2.flowrate
            if flow >0:
                remaining_minutes = minutes - matrix[cave.valves.index(valve)] [cave.valves.index(valve2)] -1
                #print(answer[bitmask])
                if indiciesreal[valve2.name] & bitmask or remaining_minutes <=  0: continue
                visit(valve2, remaining_minutes, bitmask | indiciesreal[valve2.name], pressure + flow * remaining_minutes, answer)
        return answer
    #cave.valves[0] in testinput for valve AA
    #cave.valves[52] in input for valve AA
    pex=visit(cave.valves[52], 30, 0, 0, {})
    part1 = max(pex)
    print(pex)
    print(cave.valves[1].flowrate)
    print(part1)
    visited2 = visit(cave.valves[52], 26, 0, 0, {})
    part2 = max(v1 + v2 for bitm1, v1 in visited2.items()
                for bitm2, v2 in visited2.items() if not bitm1 & bitm2)
    print(part2)

if __name__=="__mai" \
             "n__":
    main()