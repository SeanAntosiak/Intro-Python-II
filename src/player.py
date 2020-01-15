# Write a class to hold player information, e.g. what room they are in
# currently.


class Player():
    def __init__(self, name, room, inv=None):
        self.name = name
        self.room = room
        self.inv = inv
        if self.inv is None:
            self.inv = []
