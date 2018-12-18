from enum import Enum

class State(Enum):
    LEFT = 1
    STRAIGHT = 2
    RIGHT = 3


class Direction(Enum):
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4

class Train:
    train_directions = ['^', '>', 'v', '<']

    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.state = State.LEFT

        directions = [Direction.UP,Direction.RIGHT,Direction.DOWN,Direction.LEFT]
        self.direction = directions[Train.train_directions.index(direction)]
        
    
    def __repr__(self):
        return f'<{self.x},{self.y}> {self.direction} {self.state}'
    

    def next_state(self):
        if self.state == State.LEFT:
            self.state = State.STRAIGHT
        elif self.state == State.STRAIGHT:
            self.state = State.RIGHT
        elif self.state == State.RIGHT:
            self.state = State.LEFT
    
    def move(self, map):
        if self.direction == Direction.UP:
            self.y -= 1
        elif self.direction == Direction.RIGHT:
            self.x += 1
        elif self.direction == Direction.DOWN:
            self.y += 1
        elif self.direction == Direction.LEFT:
            self.x -= 1
        new_place = map[self.x][self.y]
        # Crash happened
        if new_place in Train.train_directions:
            return True
        # Moving forward, no need to change direction
        elif new_place in ['-', '|']:
            pass
        elif new_place == '/':
            if self.direction == Direction.UP:
                self.direction = Direction.RIGHT
            elif self.direction == Direction.RIGHT:
                self.direction = Direction.UP
            elif self.direction == Direction.DOWN:
                self.direction = Direction.LEFT
            elif self.direction == Direction.LEFT:
                self.direction = Direction.DOWN
        elif new_place == '\\':
            if self.direction == Direction.UP:
                self.direction = Direction.LEFT
            elif self.direction == Direction.RIGHT:
                self.direction = Direction.DOWN
            elif self.direction == Direction.DOWN:
                self.direction = Direction.RIGHT
            elif self.direction == Direction.LEFT:
                self.direction = Direction.UP
        elif new_place == '+':
            if self.state == State.RIGHT:
                if self.direction == Direction.UP:
                    self.direction = Direction.RIGHT
                elif self.direction == Direction.RIGHT:
                    self.direction = Direction.DOWN
                elif self.direction == Direction.DOWN:
                    self.direction = Direction.LEFT
                elif self.direction == Direction.LEFT:
                    self.direction = Direction.UP
            elif self.state == State.STRAIGHT:
                pass
            elif self.state == State.LEFT:
                if self.direction == Direction.UP:
                    self.direction = Direction.LEFT
                elif self.direction == Direction.RIGHT:
                    self.direction = Direction.UP
                elif self.direction == Direction.DOWN:
                    self.direction = Direction.RIGHT
                elif self.direction == Direction.LEFT:
                    self.direction = Direction.DOWN
            self.next_state()


def read_input():
    with open('testinput', 'r') as f:
        lines = f.readlines()
        map = [list(l[0:-1]) for l in lines]
        trains = []
        for x in range(len(map)):
            for y in range(len(map[x])):
                if map[x][y] in Train.train_directions:
                    trains.append(Train(x, y, map[x][y]))
        return (map, trains)

def tick(map, trains):
    pass

def main():
    map, trains = read_input()
    trains[0].move(map)
    print(trains)
    trains[0].move(map)
    print(trains)
    trains[0].move(map)
    print(trains)
    trains[0].move(map)
    print(trains)
    trains[0].move(map)
    print(trains)


main()