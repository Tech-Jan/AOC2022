import numpy as np


def filereader():
    with open("../input/input","r") as f:
        data = f.read().split("\n")
        data_2=[]
        for item in data:
            items=item.split(",")
            row=[int(numba) for numba in items]
            data_2.append(row)
        data= np.array(data_2)
        return data


class Mesh():
    def __init__(self, data):
        self.data=data
        self.xmax=np.max(self.data[:,0])+3
        self.ymax = np.max(self.data[:, 1])+3
        self.zmax = np.max(self.data[:, 2])+3
        self.mesh = np.zeros((self.xmax,self.ymax,self.zmax))