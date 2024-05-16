class Bullet:
    def __init__(self, mass, radius):
        self.mass = mass
        self.radius = radius
        self.gravity = True


class Bombshell:
    def __init__(self, mass, drill_radius, radius):
        self.mass = mass
        self.drill_radius = drill_radius
        self.radius = radius
        self.gravity = True


class Laser:
    def __init__(self, mass, radius, velocity, impulse, distance):
        self.mass = mass
        self.radius = radius
        self.velocity = velocity
        self.impulse = impulse
        self.distance = distance
        self.gravity = False
