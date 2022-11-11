from statistics import harmonic_mean


class Rider:
    def __init__(self, name):
        self.name = name


class Horse:
    def __init__(self, name, rider):
        self.name = name
        self.rider = rider


the_rider = Rider("Sally")
harry_the_horse = Horse("Harry", the_rider)

print("The name of House is {}".format(harry_the_horse.name))
print("The name of Rider is {}".format(harry_the_horse.rider.name))
