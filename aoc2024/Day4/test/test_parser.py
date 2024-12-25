from aoc2024.Day4.src import za
from aoc2024.Day4.src import main
from aoc2024.Day4.src import reader

#case1=real case2=test
case=1

def resultat1():
    resultat1= za.main(case)
    return set(resultat1)

def resultat2():
    input = reader.read_input(case)
    resultat2 = main.puzzle(input).res_part2
    return set(resultat2)

def testaa():
    assert resultat1()==resultat2()

def test2():
    print("the difference between the real results and actual results is:")

    assert resultat1()-resultat2()==set(), "theresadiffer"



