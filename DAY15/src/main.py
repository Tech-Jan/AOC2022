from DAY15.input.filereader import filereader
from map import Cave,Objects,Sensor,Beacon
from copy import deepcopy
import time

def main():
    # part1
    y=2000000
    cave=Cave()
    for my_sensor in Sensor.instances:
        my_sensor.distances()
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
    print("part1",counter2)

    time.sleep(5)

    #part2
    found=False

    for my_sensor in Sensor.instances:
        my_sensor.distances()

    for y in range(0,4000000):

        print(y)
        if found==True:

            exit()

        my_result = []
        st=time.time()
        for my_sensor in Sensor.instances:
            my_result2=my_sensor.signal_part2(y)
            if my_result2[0]:
                my_result.append(my_result2[1])
                if my_result2[1][0]==0 and my_result2[1][1]==4000000:
                    break
        my_sum_result=my_result[0]
        my_result.pop(0)
        t = 0
        et=time.time()
        st2=time.time()
        while len(my_result)>0:
            t+=1
            if t==100:
                my_sum_result.append(deepcopy(my_result))
                print(my_sum_result)
                print(my_result)
                res=0
                if my_sum_result[0] ==0:
                    print("x is the missing number, in this case x=", my_sum_result[1]+1 )
                    res=my_sum_result[1]+1
                if my_sum_result[1] ==4000000:
                    print("x is the missing number, in this case x=", my_sum_result[0]-1 )
                    res=my_sum_result[0]-1
                print("this is y",y)
                res=res*4000000+y
                print(res)
                found=True
            if my_sum_result[0]==0 and my_sum_result[1==4000000]:
                break
            for result in my_result:
                remove = False
                if result[0]<=my_sum_result[0]<=result[1]:
                    my_sum_result[0]=result[0]
                    remove=True

                if result[0] <= my_sum_result[1] <= result[1]:
                    my_sum_result[1] = result[1]
                    remove=True
                if my_sum_result[0]<result[0] and my_sum_result[1]>result[1]:
                    remove = True

                if remove:
                    my_result.remove(result)

        et2=time.time()



        # for my_sensor in Sensor.instances:
        #     my_sensor.signalx(y)
        # print(max(list(cave.signals),key=lambda obj:obj[0])[0])
        # print(min(list(cave.signals), key=lambda obj: obj[0])[0])



if __name__=="__main__":
    main()
    #13071210703981 to high
    #13071210703981
    #13071206703981
    #130712086703981