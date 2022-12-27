from map import *
import time

# made some performance tests.
# using set is fastest-> 6-9 sec
# using dataframe is alot slower -> 60-70 sec
# because adding data to dataframe and reading data is very time consuming
# using list is alot slower-> 3000 sec

def main():
    st = time.time()
    st5 = time.time()
    my_map = Cave()
    my_sand = Sand()
    et5=time.time()
    st2 = time.time()
    i=0
    while not my_map.cave_full:
        my_sand_particle = SandParticle(my_map)
        my_sand_particle.fall_part2()
        # if i%100==0:
        #     print(my_map.map.to_string())
        # i+=1

    et2 = time.time()
    st3 = time.time()
    # my_map.paint_stones()
    et3 = time.time()
    st4 = time.time()
    print(my_map.map.to_string())
    et4 = time.time()


    et = time.time()

    # get the execution time
    elapsed_time = et - st
    elapsed_time2=et2-st2
    elapsed_time3=et3-st3
    elapsed_time4 = et4 - st4
    elapsed_time5=et5-st5
    with open("timesmeasured","a") as f:
        f.write(f"elapsed_time1= {elapsed_time},createobjects= {elapsed_time5}, fillsand= elapsed_time2= {elapsed_time2}, time_refresh dataframe= {elapsed_time3}, time print data= {elapsed_time4}\n")
    print(elapsed_time,elapsed_time2,elapsed_time3,elapsed_time4)


if __name__ == "__main__":
    for i in range(5):
        main()


    #52.3
    #41.1
