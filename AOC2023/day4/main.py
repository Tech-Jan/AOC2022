import copy

def read_input(file):
    with open(file) as input:
        input = input.read()
        output = input.split("\n")
    return output


input_list = read_input("input.txt")
print(input_list)

games=[]
winners=[]
gaymers=[]
for game in input_list:
    splitgame=game.split(": ")[1]

    winner=splitgame.split("|")[0].split()
    gaymer=splitgame.split("|")[1].split()
    winners.append(winner)
    gaymers.append(gaymer)
    games.append([winner,gaymer])
print(winners)
print(gaymers)

def formula(gains):
    if gains==0:
        return 0
    else:
        return 2**(gains-1)
points=0
for winner,gaymer in games:
    print(winner,gaymer)
    gains=0
    for number in winner:
        for possible in gaymer:
            if number==possible:
                gains+=1
    points+=formula(gains)
    print(points)
import numpy as np

stacks=np.ones(len(games))
for gaym,[winner,gaymer] in enumerate(games):

    gains = 0
    for number in winner:
        for possible in gaymer:
            if number == possible:
                gains += 1
    for j in range(int(stacks[gaym])):
        for i in range(1,gains+1):

            try:
                stacks[gaym+i]+=1
            except:
                pass



print(stacks)
print(sum(stacks))