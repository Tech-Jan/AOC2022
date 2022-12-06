import random


class Crane:
    """big crane. 2models availabe model '9001' and '9000'
    please enter in which storage this crane is working"""

    def __init__(self, storage, model):
        self.model = model
        self.storage = storage
        self.move_box = []

    def movebox(self, amount_boxes, storage_from, storage_to):
        self.move_box = []
        for i in range(amount_boxes):
            self.pickup(storage_from)
        for i in range(len(self.move_box)):
            self.drop(storage_to)

    def pickup9000(self, storage_from):
        x = storage_from
        y = self.storage.topbox(x)
        if y > self.storage.floorlevel:
            self.move_box.append(self.storage.shelf[-y][x])
            self.storage.shelf[-y][x] = " "

    def pickup9001(self, storage_from):
        x = storage_from
        y = self.storage.topbox(x)
        if y > self.storage.floorlevel:
            self.move_box.append(self.storage.shelf[-y][x])
            self.storage.shelf[-y][x] = " "

    def pickup(self, storage_from):
        self.storage.isspace()
        if self.model == "9000":
            self.pickup9000(storage_from)
        if self.model == "9001":
            self.pickup9001(storage_from)

    def drop(self, storage_to):
        self.storage.isspace()
        if self.model == "9000":
            self.drop9000(storage_to)
        if self.model == "9001":
            self.drop9001(storage_to)

    def drop9000(self, storage_to):
        coordinates = self.checkiffull(storage_to)
        x = coordinates[0]
        y = coordinates[1]
        self.storage.shelf[-y][x] = self.move_box[0]
        del self.move_box[0]

    def drop9001(self, storage_to):
        coordinates = self.checkiffull(storage_to)
        x = coordinates[0]
        y = coordinates[1]
        self.storage.shelf[-y][x] = self.move_box[-1]
        del self.move_box[-1]

    def checkiffull(self, storage_to):
        coordinates = []
        x = storage_to
        # +1 because you want to drop the box on top of the topbox
        y = self.storage.topbox(x) + 1
        while y > self.storage.storeheight:
            if x == self.storage.width-1:
                x -= 1
                y = self.storage.topbox(x) + 1
            elif x == 0:
                x += 1
                y = self.storage.topbox(x) + 1
            else:
                x += random.choice((-1, 1))
                y = self.storage.topbox(x) + 1
        coordinates.append(x)
        coordinates.append(y)
        return list(coordinates)
