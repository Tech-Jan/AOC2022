from objects import *
from copy import deepcopy

M=[[0, 1, 2, 1, 2, 3, 4, 5, 1, 2], [1, 0, 1, 2, 3, 4, 5, 6, 2, 3], [2, 1, 0, 1, 2, 3, 4, 5, 3, 4], [1, 2, 1, 0, 1, 2, 3, 4, 2, 3], [2, 3, 2, 1, 0, 1, 2, 3, 3, 4], [3, 4, 3, 2, 1, 0, 1, 2, 4, 5], [4, 5, 4, 3, 2, 1, 0, 1, 5, 6], [5, 6, 5, 4, 3, 2, 1, 0, 6, 7], [1, 2, 3, 2, 3, 4, 5, 6, 0, 1], [2, 3, 4, 3, 4, 5, 6, 7, 1, 0]]

def search_max_flow(cave,current_valve,t,time):
    global M
    max_flow=0
    max_valve=None
    max_needed_moves=0
    for valve in cave.valves:
        abc=valve.name
        bbb=current_valve.name
        current_valve_pos=cave.valves.index(current_valve)
        valve_pos=cave.valves.index(valve)
        needed_moves=cave.count_needed_moves(current_valve,valve)
        timeleft=time-needed_moves-t
        possible_flow=timeleft*valve.flowrate
        if possible_flow>max_flow:
            max_flow=possible_flow
            max_valve=valve
            max_needed_moves=needed_moves
    return max_flow,max_valve,max_needed_moves

def create_path():
    pass

def main():
    time=30
    cave=filereader("../input/testinput")
    human=Human()
    human.pos=cave.valves[0]
    t=0
    path=Path()
    path.path.append(human.pos)
    path.current_position=human.pos
    paths=[path]






    t=1
    for t in range(30):
        print(t)
        for path_pos in range(len(paths)):
            path=paths[path_pos]

            path.sum_flow+=path.current_flow

            for adjacent_valve in path.current_position.adjacent_valves:
                newpath=Path()
                newpath.path=deepcopy(path.path)
                newpath.current_position=adjacent_valve

                paths.append(newpath)
            if path.path[-1].open==False:
                path.path[-1].open=True


        # if t>1:
        #     for path in paths:
        #         flow=path.sum_flow
        #         position=path.current_position
        #
        #         for compare in paths:
        #             compare_flow=compare.sum_flow
        #             compare_pos=compare.current_position
        #
        #             if flow<=compare_flow and position==compare_pos:
        #                 paths.remove(path)
        #                 break

        print(len(paths))

    max=0
    for path in paths:
        path.calc_current_flow()
        print(path.sum_flow)
        if path.sum_flow>max:
            max=path.sum_flow
    print(max)

    max_flow,max_valve,max_needed_moves=search_max_flow(cave,current_valve,t,time)





if __name__=="__main__":
    main()