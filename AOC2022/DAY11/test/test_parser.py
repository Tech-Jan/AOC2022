import pytest


@pytest.fixture
def monkey_list():
    monkey0 = Monkey("monkey0")
    monkey0.items = [79, 98]
    monkey0.operation = "old * 19"
    monkey0.diviser = 23
    monkey0.targets = [2, 3]

    monkey1 = Monkey("monkey1")

    monkey1.items = [54, 65, 75, 74]
    monkey1.operation = "old + 6"
    monkey1.diviser = 19
    monkey1.targets = [2, 0]

    monkey2 = Monkey("monkey2")
    monkey2.items = [79, 60, 97]
    monkey2.operation = "old * old"
    monkey2.diviser = 13
    monkey2.targets = [1, 3]

    monkey3 = Monkey("monkey3")
    monkey3.items = [74]
    monkey3.operation = "old + 3"
    monkey3.diviser = 17
    monkey3.targets = [0, 1]
    monkey_lista = [monkey0, monkey1, monkey2, monkey3]
    return monkey_lista


# not nescasarry needed. but usefull to create resultlists etc
@pytest.fixture
def inspection_results():
    results = [[6, 4, 3, 2], [10, 10, 6, 3], [16, 14, 12, 3], [20, 20, 16, 3], [26, 24, 22, 4], [30, 30, 26, 4],
               [37, 33, 33, 4], [40, 40, 36, 4], [47, 43, 43, 4], [50, 50, 46, 4], [58, 54, 52, 5], [60, 60, 56, 5],
               [68, 64, 62, 5], [71, 69, 67, 5], [78, 74, 72, 6], [81, 79, 77, 6], [88, 84, 82, 7], [93, 89, 87, 7],
               [98, 94, 92, 8], [103, 99, 97, 8], [108, 104, 102, 8], [113, 109, 107, 8], [118, 114, 112, 8],
               [123, 119, 117, 8], [129, 125, 121, 8], [133, 129, 127, 8], [139, 135, 131, 9], [143, 139, 137, 9],
               [151, 147, 139, 9], [153, 149, 147, 9], [161, 157, 149, 10], [163, 159, 157, 10], [171, 167, 159, 10],
               [173, 169, 167, 11], [181, 177, 169, 11], [184, 180, 176, 11], [191, 187, 179, 12], [194, 190, 186, 12],
               [201, 197, 189, 12], [205, 201, 195, 13], [211, 207, 199, 13], [215, 211, 205, 13], [221, 217, 209, 13],
               [225, 221, 215, 14], [231, 227, 219, 14], [235, 231, 225, 14], [241, 237, 229, 14], [245, 241, 235, 14],
               [251, 247, 239, 14], [255, 251, 245, 14], [262, 258, 248, 14], [265, 261, 255, 14], [272, 268, 258, 14],
               [275, 271, 265, 14], [282, 278, 268, 15], [285, 281, 275, 15], [292, 288, 278, 15], [295, 291, 285, 15],
               [301, 298, 288, 16], [304, 301, 295, 16], [311, 308, 298, 17], [315, 312, 304, 17], [321, 318, 308, 18],
               [326, 323, 313, 18], [331, 328, 318, 19], [336, 333, 323, 19], [341, 338, 328, 19], [346, 343, 333, 19],
               [351, 348, 338, 19], [357, 354, 342, 19], [361, 358, 348, 20], [367, 364, 352, 20], [372, 369, 357, 20],
               [378, 375, 361, 20], [383, 380, 366, 20], [388, 385, 371, 20], [393, 390, 376, 20], [398, 395, 381, 21],
               [403, 400, 386, 21], [408, 405, 391, 21], [413, 411, 395, 22], [417, 415, 401, 22], [423, 421, 405, 22],
               [428, 426, 410, 23], [434, 432, 414, 23], [439, 437, 419, 23], [444, 442, 424, 24], [449, 447, 429, 25],
               [454, 452, 434, 25], [459, 457, 439, 25], [464, 462, 444, 25], [470, 468, 448, 25], [475, 473, 453, 25],
               [480, 478, 458, 25], [486, 484, 462, 25], [491, 489, 467, 25], [497, 495, 471, 25], [501, 499, 477, 25],
               [507, 505, 481, 25], [511, 509, 487, 25], [517, 515, 491, 25], [521, 519, 497, 25], [528, 526, 500, 25],
               [532, 530, 506, 25], [538, 536, 510, 25], [543, 541, 515, 25], [549, 547, 519, 26], [554, 552, 524, 26],
               [559, 557, 529, 26], [564, 562, 534, 26], [569, 567, 539, 26], [574, 572, 544, 26], [579, 577, 549, 26],
               [585, 583, 553, 27], [590, 588, 558, 28], [596, 594, 562, 28], [600, 598, 568, 28], [607, 605, 571, 28],
               [611, 609, 577, 28], [617, 615, 581, 28], [621, 619, 587, 28], [627, 625, 591, 29], [631, 629, 597, 29],
               [638, 636, 600, 29], [642, 640, 606, 29], [649, 647, 609, 29], [653, 651, 615, 29], [659, 657, 619, 29],
               [664, 662, 624, 29], [670, 668, 628, 29], [674, 672, 634, 30], [679, 678, 638, 31], [683, 682, 644, 31],
               [689, 688, 648, 31], [695, 694, 652, 31], [700, 699, 657, 31], [706, 705, 661, 31], [711, 710, 666, 32],
               [716, 715, 671, 32], [722, 721, 675, 32], [726, 725, 681, 32], [732, 731, 685, 32], [736, 735, 691, 32],
               [742, 741, 695, 33], [746, 745, 701, 33], [754, 753, 703, 33], [756, 755, 711, 33], [765, 764, 712, 34],
               [767, 766, 720, 34], [775, 774, 722, 34]]
    # input_expected = [[i, item[0] * item[1]] for i, item in enumerate(results, 1)]
    # print(input_expected)
    return results


input_expected = [[1, 24], [2, 100], [3, 224], [4, 400], [5, 624], [6, 900], [7, 1221], [8, 1600], [9, 2021],
                  [10, 2500], [11, 3132], [12, 3600], [13, 4352], [14, 4899], [15, 5772], [16, 6399], [17, 7392],
                  [18, 8277], [19, 9212], [20, 10197], [21, 11232], [22, 12317], [23, 13452], [24, 14637], [25, 16125],
                  [26, 17157], [27, 18765], [28, 19877], [29, 22197], [30, 22797], [31, 25277], [32, 25917],
                  [33, 28557], [34, 29237], [35, 32037], [36, 33120], [37, 35717], [38, 36860], [39, 39597],
                  [40, 41205], [41, 43677], [42, 45365], [43, 47957], [44, 49725], [45, 52437], [46, 54285],
                  [47, 57117], [48, 59045], [49, 61997], [50, 64005], [51, 67596], [52, 69165], [53, 72896],
                  [54, 74525], [55, 78396], [56, 80085], [57, 84096], [58, 85845], [59, 89698], [60, 91504],
                  [61, 95788], [62, 98280], [63, 102078], [64, 105298], [65, 108568], [66, 111888], [67, 115258],
                  [68, 118678], [69, 122148], [70, 126378], [71, 129238], [72, 133588], [73, 137268], [74, 141750],
                  [75, 145540], [76, 149380], [77, 153270], [78, 157210], [79, 161200], [80, 165240], [81, 169743],
                  [82, 173055], [83, 178083], [84, 182328], [85, 187488], [86, 191843], [87, 196248], [88, 200703],
                  [89, 205208], [90, 209763], [91, 214368], [92, 219960], [93, 224675], [94, 229440], [95, 235224],
                  [96, 240099], [97, 246015], [98, 249999], [99, 256035], [100, 260099], [101, 266255], [102, 270399],
                  [103, 277728], [104, 281960], [105, 288368], [106, 293763], [107, 300303], [108, 305808],
                  [109, 311363], [110, 316968], [111, 322623], [112, 328328], [113, 334083], [114, 341055],
                  [115, 346920], [116, 354024], [117, 358800], [118, 367235], [119, 372099], [120, 379455],
                  [121, 384399], [122, 391875], [123, 396899], [124, 405768], [125, 410880], [126, 419903],
                  [127, 425103], [128, 432963], [129, 439568], [130, 447560], [131, 452928], [132, 460362],
                  [133, 465806], [134, 474032], [135, 482330], [136, 489300], [137, 497730], [138, 504810],
                  [139, 511940], [140, 520562], [141, 526350], [142, 535092], [143, 540960], [144, 549822],
                  [145, 555770], [146, 567762], [147, 570780], [148, 584460], [149, 587522], [150, 599850]]


@pytest.mark.parametrize("test_input,expected", input_expected)
def test_result_p2(test_input, expected, monkey_list, inspection_results):
    for i in range(test_input):
        inspection_counter_p2(monkey_list)
        inspections = sorted([monkey.inspections for monkey in monkey_list], reverse=True)
    assert inspections[0] * inspections[1] == expected

def test_result_p1(monkey_list):
    for i in range(20):
        inspection_counter_p1(monkey_list)
        inspections = sorted([monkey.inspections for monkey in monkey_list], reverse=True)
    assert inspections[0] * inspections[1] == 10605