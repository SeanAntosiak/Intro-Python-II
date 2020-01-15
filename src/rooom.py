# Implement a class to hold room information. This should have name and
# description attributes.


class Room():
    def __init__(self, name, desc, key, list=None, n_to=None,
                 e_to=None, s_to=None, w_to=None
                 ):
        self.name = name
        self.desc = desc
        self.key = key
        self.list = list
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to
        if self.list is None:
            self.list = []
