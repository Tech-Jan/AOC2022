from DAY15.input.filereader import filereader
from map import Cave,Objects,Sensor,Beacon

def main():
    # part1
    y=2000000
    cave=Cave()
    for sensor in Sensor.instances:
        print (sensor.distance)
        sensor.signalx(y)
    beacons=set([])
    for beacon in Beacon.instances:
        beacons.add((beacon.coords["x"],beacon.coords["y"]))
    set3=cave.signals-beacons
    counter2=0
    for signal in set3:
        if signal[1]==y:
            counter2+=1
    print(counter2)
    exit()
    #part2

    y=2000000
    cave=Cave()
    for sensor in Sensor.instances:
        print (sensor.distance)
        sensor.signal
    beacons=set([])
    for beacon in Beacon.instances:
        beacons.add((beacon.coords["x"],beacon.coords["y"]))
    set3=cave.signals-beacons
    counter2=0
    for signal in set3:
        if signal[1]==y:
            counter2+=1


if __name__=="__main__":
    main()