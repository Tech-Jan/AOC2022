from objects import filereader, Mesh
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def main():
    data=filereader()
    my_mesh=Mesh(data)
    print(my_mesh.zmax)
    print(my_mesh.mesh)

    for xyz in data:
        my_mesh.mesh[xyz[0],xyz[1],xyz[2]]=1
    free_side=0
    for xyz in data:
        if my_mesh.mesh[xyz[0]-1, xyz[1], xyz[2]] == 0:
            free_side+=1
        if my_mesh.mesh[xyz[0]+1, xyz[1], xyz[2]] == 0:
            free_side+=1
        if my_mesh.mesh[xyz[0], xyz[1]-1, xyz[2]] == 0:
            free_side+=1
        if my_mesh.mesh[xyz[0], xyz[1]+1, xyz[2]] == 0:
            free_side+=1
        if my_mesh.mesh[xyz[0], xyz[1], xyz[2]-1] == 0:
            free_side+=1
        if my_mesh.mesh[xyz[0], xyz[1], xyz[2]+1] == 0:
            free_side+=1
    print("freeside",free_side)
    print(my_mesh.mesh)

    pocket=0
    xyzcoordpcket=[]
    for x in range(my_mesh.xmax-2):
        for y in range(my_mesh.ymax-2):
            for z in range(my_mesh.zmax-2):
                if ((my_mesh.mesh[x+1,y,z]) ==1 and
                    (my_mesh.mesh[x - 1, y, z]) == 1 and
                    (my_mesh.mesh[x, y+1, z]) == 1 and
                    (my_mesh.mesh[x, y-1, z]) == 1 and
                    (my_mesh.mesh[x, y, z+1]) == 1 and
                    (my_mesh.mesh[x, y, z-1]) == 1 and
                    (my_mesh.mesh[x, y, z]) != 1):
                    pocket+=1
                    xyzcoordpcket.append([x,y,z])
    print("pocket",pocket, xyzcoordpcket)
    free_sidep=0
    for pckt in xyzcoordpcket:
        if my_mesh.mesh[pckt[0] - 1, pckt[1], pckt[2]] == 1:
            free_sidep += 1
        if my_mesh.mesh[pckt[0] + 1, pckt[1], pckt[2]] == 1:
            free_sidep += 1
        if my_mesh.mesh[pckt[0], pckt[1] - 1, pckt[2]] == 1:
            free_sidep += 1
        if my_mesh.mesh[pckt[0], pckt[1] + 1, pckt[2]] == 1:
            free_sidep += 1
        if my_mesh.mesh[pckt[0], pckt[1], pckt[2] - 1] == 1:
            free_sidep += 1
        if my_mesh.mesh[pckt[0], pckt[1], pckt[2] + 1] == 1:
            free_sidep += 1
    print(free_sidep)
    result = free_side-free_sidep
    print("result",result)
    pikx=[]
    piky=[]
    pikz=[]
    for item in xyzcoordpcket:
        pikx.append(item[0])
        piky.append(item[1])
        pikz.append(item[2])

    z, x, y = my_mesh.mesh.nonzero()
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    #ax2 = fig.add_subplot(111, projection='3d')
    ax.scatter(x, y, z, zdir='z', c='red')
    ax.scatter(pikx, pikz , piky, zdir='z', c='blue')
    plt.savefig("demo.png")

    print(x)
    plt.show()


if __name__ == "__main__":
    main()
    #3252 to high