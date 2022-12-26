from map import *


def main():
    my_map = Cave()
    my_sand = Sand()
    my_sand.paintsand(my_map)
    while not my_map.cave_full:
        my_sand_particle = SandParticle(my_map)
        my_sand_particle.fall_part2()


    # print(sorted(my_map.stone_list, key=lambda x:x["x"]))


if __name__ == "__main__":
    main()
