import copy 

Y = 0
X = 1
WALL = '#'

class Guard:
    def __init__(self, current_dir: str, current_pos: list, height: int, width: int):
        self.current_dir = current_dir
        self.current_pos = current_pos
        self.height = height
        self.width = width
        self.directions = ['^', '>', 'v', '<']
        self.guard_dirs = {
            '^' : [-1, 0],
            '>' : [0, 1],
            'v' : [1, 0],
            '<' : [0, -1],
        }
        self.amount_visited = 0
        self.total_obstacles = 0
    
    def inside_map(self, y: int, x: int) -> bool:
        return (0 <= y < self.height and
                0 <= x < self.width)


    def turn(self):
        idx = self.directions.index(self.current_dir)
        self.current_dir = self.directions[(idx + 1) % 4]

    def visited(self):
        print("The guard has visited", self.amount_visited, "squares!")

    def obstacles(self):
        print("You can place a total of", self.total_obstacles, "where the guard ends in a loop!")

    def get_next_direction(self, curr_dir: str) -> str:
        idx = self.directions.index(curr_dir)

        return self.directions[(idx + 1) % 4]

    def get_coordinates_for_turn(self, curr_dir: str) -> list:
        dy = self.guard_dirs.get(curr_dir)[Y]
        dx = self.guard_dirs.get(curr_dir)[X]

        return dy, dx

    def simulate(self, map: list, y: int, x: int):
        map_dc = copy.deepcopy(map)
        if not self.inside_map(y, x):
            return
        dy, dx = self.get_coordinates_for_turn(self.current_dir)
        if not self.inside_map(dy, dx):
            return
        map_dc[dy][dx] = WALL
        walked = set()
        dir = self.current_dir
        pos = (y, x)
        while True:
            y, x = pos
            if not self.inside_map(y, x):
                break
            dy, dx = self.get_coordinates_for_turn(dir)
            if (y, x, dy, dx) in walked:
                self.total_obstacles +=1
                break
            walked.add((y, x, dy, dx))
            if not self.inside_map(y + dy, x + dx):
                    break
            print(self.width, x + dx)
            if map_dc[y + dy][x + dx] == WALL:
                dir = self.get_next_direction(dir)
                continue
            pos = (y + dy, x + dx)

    def move(self, map: list):
        while True:
            y, x = self.current_pos
            if not self.inside_map(y, x):
                break
            dy, dx = self.get_coordinates_for_turn(self.current_dir)

            self.simulate(map, y, x)
            if map[y][x] != 'X':
                map[y][x] = 'X'
                self.amount_visited += 1
            if not self.inside_map(y + dy, x + dx):
                    break
            if map[y + dy][x + dx] == WALL:
                self.turn()
                continue
            self.current_pos = (y + dy, x + dx)