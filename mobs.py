# classes for mobs
class Mob(object):
    """ Base class, which all others will be derived from """
    def __init__(self, name, level = 1):
        self.name = name
        self.level = level
        
    def __str__(self):
        rep = "\nName: "
        rep += self.name
        rep += "\nLevel: "
        rep += str(self.level)

class Human(Mob):
    """ A human """


class Dwarf(Mob):
    """ A dwarf """


class Rept(Mob):
    """ A rept """
