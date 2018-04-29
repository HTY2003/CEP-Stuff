import sys
import random

# Object Models
class NamedObject(object):
    def __init__(self, name):
        self.name = name.lower()

class MobileObject(NamedObject):
    def __init__(self, name, location):
        super().__init__(name)
        self.location = location

    def install(self):
        self.location.add_thing(self)

class Ship(MobileObject):
    def __init__(self, name, birthplace, threshold):
        super().__init__(name, birthplace)
        self.threshold = threshold
        self.is_alive = True
        self.install()

    def move(self):
        if self.threshold < 0:
            pass
        elif random.randint(0, self.threshold) == 0:
            self.act()

    def act(self):
        new_location = self.location.random_neighbor()
        if new_location:
            self.move_to(new_location)

    def move_to(self, new_location):
        if self.location == new_location:
            print(self.name, "is already at", new_location.name)
        elif new_location.accept_ship():
            print(self.name, "moves from", self.location.name, "to", new_location.name)
            self.location.remove_thing(self)
            new_location.add_thing(self)
            self.location = new_location
        else:
            print(self.name, "can't move to", new_location.name)

    def go(self, direction):
        new_place = self.location.neighbors_towards(direction)
        if new_place:
            self.move_to(new_place)
        else:
            print("You cannot go", direction, "from", self.location.name)

    def shoot(self, ship_name):
        target_ships = list(filter(lambda ship: ship.name == ship_name, self.location.things))
        if len(target_ships) > 0:
            target_ship = target_ships[0]
            print(self.name, "opens fire at", target_ship.name)
            target_ship.destroy()

    def destroy(self):
        print(self.name, "destroyed!")
        self.is_alive = False
        self.move_to(HEAVEN)

class EnemyShip(Ship):
    def act(self):
        ships = list(filter(lambda thing: isinstance(thing,Ship), self.location.things))
        other_ships = list(filter(lambda ship: ship != self, ships))

        if len(other_ships) == 0:
            super().act()
        else:
            ship_names = list(map(lambda ship: ship.name, other_ships))
            self.shoot(random.choice(ship_names))

class Place(NamedObject):
    def __init__(self, name):
        super().__init__(name)
        self.things = []
        self.neighbors = {}

    def exits(self):
        return list(self.neighbors.keys())

    def accept_ship(self):
        return True

    def add_neighbor(self, direction, place):
        if direction in self.neighbors:
            print("There is already a neighbor in the", direction, "direction")
        else:
            self.neighbors[direction] = place

    def neighbors_towards(self, direction):
        if direction in self.neighbors:
            return self.neighbors[direction]
        else:
            return None

    def random_neighbor(self):
        if len(self.neighbors) > 0:
            random_exit = random.choice(self.exits())
            return self.neighbors[random_exit]
        else:
            return None

    def add_thing(self, thing):
        self.things.append(thing)

    def remove_thing(self, thing):
        self.things.remove(thing)


# Manages the clock
class Clock(object):
    def __init__(self):
        self.time = 0

    def tick(self, ships):
        self.time += 1
        for ship in ships:
            ship.move()

class Game(object):
    def __init__(self, enterprise, enemy_ships):
        self.clock = Clock()
        self.is_active = True
        self.enterprise = enterprise
        self.enemy_ships = enemy_ships

        self.ships = [enterprise]
        self.ships.extend(enemy_ships)

    def print_state(self):
        things_name = list(map(lambda thing: thing.name, self.enterprise.location.things))
        print("Enterprise is at:", self.enterprise.location.name)
        print("You see:")
        print(things_name)
        print()
        print("Exits:")
        print(self.enterprise.location.exits())

    def process_command(self, command):
        tokens = command.split(' ')

        if len(tokens) > 0:
            if tokens[0] == "quit":
                self.is_active = False
            elif tokens[0] == "wait":
                self.clock.tick(self.ships)
                pass
            else:
                try:
                    getattr(self.enterprise, tokens[0])(*tokens[1:])
                except Exception as e:
                    print("No such command:", e.args)

            self.ships = list(filter(lambda ship: ship.is_alive, self.ships))
            self.clock.tick(self.ships)


    def start(self):
        while self.is_active:
            # Print the state of the game
            self.print_state()

            # Get the command from the user
            print("Command: ", end='')
            command = input()
            print()

            # Process the command
            self.process_command(command)
            print()

# Default locations
EARTH = Place("earth")
MARS = Place("mars")
SPACE = Place("space")
DEEP_SPACE = Place("deep_space")
DEEPER_SPACE = Place("deeper_space")
BLACK_HOLE = Place("black_hole")
HEAVEN = Place("heaven")

SOUTH = "south"
NORTH = "north"
EAST = "east"
WEST = "west"

# Paths to connect between places
def can_go_both_ways(place_a, direction, reverse_direction, place_b):
    place_a.add_neighbor(direction, place_b)
    place_b.add_neighbor(reverse_direction, place_a)

can_go_both_ways(BLACK_HOLE, SOUTH, NORTH, DEEPER_SPACE)
can_go_both_ways(SPACE, WEST, EAST, EARTH)
can_go_both_ways(SPACE, EAST, WEST, MARS)
can_go_both_ways(DEEP_SPACE, SOUTH, NORTH, SPACE)
can_go_both_ways(DEEPER_SPACE, SOUTH, NORTH, DEEP_SPACE)
can_go_both_ways(DEEP_SPACE, EAST, WEST, DEEP_SPACE)
can_go_both_ways(DEEPER_SPACE, EAST, WEST, DEEPER_SPACE)


ENTERPRISE = Ship("enterprise", EARTH, -1)
WARBIRD = EnemyShip("warbird", BLACK_HOLE, 2)
FALCON = EnemyShip("falcon", SPACE, 3)
DEATHSTAR = EnemyShip("deathstar", DEEPER_SPACE, 1)

game = Game(ENTERPRISE, [WARBIRD, FALCON, DEATHSTAR])
game.start()
