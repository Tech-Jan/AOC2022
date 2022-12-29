from map import Cave, Sensor, Beacon
import time
from copy import deepcopy

from map import Cave, Sensor, Beacon


def part1(cave):
    line_number = 2000000

    for sensor in Sensor.instances:
        print(Sensor.instances.index(sensor), "/", len(Sensor.instances))
        sensor.signalx(line_number)

    beacons = set([])
    for beacon in Beacon.instances:
        beacons.add((beacon.coords["x"], beacon.coords["y"]))
    set3 = cave.signals - beacons

    counter2 = 0
    for signal in set3:
        if signal[1] == line_number:
            counter2 += 1

    print("part1", counter2)

def sum_ranges(sum_ranges_line,my_sum_result):
    for result in sum_ranges_line:
        remove = False
        if result[0] <= my_sum_result[0] <= result[1]:
            my_sum_result[0] = result[0]
            remove = True

        if result[0]-1 <= my_sum_result[1] <= result[1]:
            my_sum_result[1] = result[1]
            remove = True
        if my_sum_result[0] < result[0] and my_sum_result[1] > result[1]:
            remove = True
        if remove:
            sum_ranges_line.remove(result)

def empty_space_found(my_sum_result,sum_ranges_line,max_size,line_number):
    my_sum_result.append(sum_ranges_line)
    print(my_sum_result)
    print(sum_ranges_line)
    res = 0
    if my_sum_result[0] == 0:
        print("x is the missing number, in this case x=", my_sum_result[1] + 1)
        res = my_sum_result[1] + 1
    if my_sum_result[1] == max_size:
        print("x is the missing number, in this case x=", my_sum_result[0] - 1)
        res = my_sum_result[0] - 1
    print("this is y", line_number)
    res = res * 40000000 + line_number
    print("resultpar2=", res)
    exit()
    found = True

def range_sensor_equilizer(sum_ranges_line:list,max_size:int,line_number:int):
    my_sum_result = sum_ranges_line[0]
    sum_ranges_line.pop(0)
    t = 0
    found= False
    while len(sum_ranges_line) > 0 and not found:
        t += 1
        if my_sum_result[0] == 0 and my_sum_result[1 == max_size]:
            break
        sum_ranges(sum_ranges_line,my_sum_result)
        if t == 100:
            found=True
            empty_space_found(my_sum_result,sum_ranges_line,max_size,line_number)
            break

def part2():
    found = False
    max_size = 4000000
    for line_number in range(0, max_size):
        if line_number%1000==0:
            print(round(line_number/max_size*100,1),"/100 percent scanned")
        sum_ranges_line = []
        for my_sensor in Sensor.instances:
            range_sensor_for_line = my_sensor.signal_part2(line_number,max_size)
            if range_sensor_for_line[0]:
                sum_ranges_line.append(range_sensor_for_line[1])
                if range_sensor_for_line[1][0] == 0 and range_sensor_for_line[1][1] == max_size:
                    break

        range_sensor_equilizer(sum_ranges_line, max_size,line_number)



    # for my_sensor in Sensor.instances:
    #     my_sensor.signalx(y)
    # print(max(list(cave.signals),key=lambda obj:obj[0])[0])
    # print(min(list(cave.signals), key=lambda obj: obj[0])[0])


def main():
    # part1
    cave = Cave()
    part1(cave)
    time.sleep(5)

    # part2
    part2()


if __name__ == "__main__":
    main()
    # 13071210703981 to high
    # 13071210703981
    # 13071206703981
    # 130712086703981
