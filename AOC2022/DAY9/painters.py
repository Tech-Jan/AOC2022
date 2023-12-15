import pprint
import time
import os

pp = pprint.PrettyPrinter(width=2000)


def paint_head(pos_h_list, pos_t_list):
    listaa = []
    for x in range(0, 20):
        listaa.append([" "])
        for y in range(0, 20):
            listaa[x].append([" "])

    for i in range(len(pos_h_list)):
        listaa = []
        for x in range(0, 20):
            listaa.append([" "])
            for y in range(0, 20):
                listaa[x].append([" "])

        hX, hY = pos_h_list[i]
        tX, tY = pos_t_list[i]
        hX = hX % 20
        hY = hY % 20
        tX = tX % 20
        tY = tY % 20

        listaa[-hY - 1][hX + 1] = (["X"])
        listaa[-tY - 1][tX + 1] = (["T"])
        pp.pprint(listaa)
        time.sleep(0.5)
        os.system('clear')


def paint_head2(positions_snake_list):
    listaa = []
    for x in range(0, 36):
        listaa.append([" "])
        for y in range(0, 36):
            listaa[x].append([" "])

    for i in range(len(positions_snake_list)):
        listaa = []
        for x in range(0, 36):
            listaa.append([" "])
            for y in range(0, 36):
                listaa[x].append([" "])

        hX, hY = positions_snake_list[i][0]
        t1X, t1Y = positions_snake_list[i][1]
        t2X, t2Y = positions_snake_list[i][2]
        t3X, t3Y = positions_snake_list[i][3]
        t4X, t4Y = positions_snake_list[i][4]
        t5X, t5Y = positions_snake_list[i][5]
        t6X, t6Y = positions_snake_list[i][6]
        t7X, t7Y = positions_snake_list[i][7]
        t8X, t8Y = positions_snake_list[i][8]
        t9X, t9Y = positions_snake_list[i][9]
        # t10X, t10Y = positions_snake_list[i][10]
        hX = hX % 36
        hY = hY % 36
        t1X = t1X % 36
        t2X = t2X % 36
        t3X = t3X % 36
        t4X = t4X % 36
        t5X = t5X % 36
        t6X = t6X % 36
        t7X = t7X % 36
        t8X = t8X % 36
        t9X = t9X % 36

        t1Y = t1Y % 36
        t2Y = t2Y % 36
        t3Y = t3Y % 36
        t4Y = t4Y % 36
        t5Y = t5Y % 36
        t6Y = t6Y % 36
        t7Y = t7Y % 36
        t8Y = t8Y % 36
        t9Y = t9Y % 36

        listaa[-hY][hX] = (["H"])
        listaa[-t1Y][t1X] = (["X"])
        listaa[-t2Y][t2X] = (["X"])
        listaa[-t3Y][t3X] = (["X"])
        listaa[-t4Y][t4X] = (["X"])
        listaa[-t5Y][t5X] = (["X"])
        listaa[-t6Y][t6X] = (["X"])
        listaa[-t7Y][t7X] = (["X"])
        listaa[-t8Y][t8X] = (["X"])
        listaa[-t9Y][t9X] = (["X"])
        # listaa[-t10Y - 12][t10X + 12] = (["T"])

        pp.pprint(listaa)
        time.sleep(0.1)
        os.system('clear')
