class Player:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '{}'.format(self.name)


class Roll:
    def __init__(self, name, defeats, defeatedby):
        self.name = name,
        self.defeats = defeats,
        self.defeatedby = defeatedby

    def __repr__(self):
        return '{} defeats {} and is defeated by {}'.format(self.name, self.defeats, self.defeatedby)

