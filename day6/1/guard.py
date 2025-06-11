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
    
    def inside_map(self, y: int, x: int) -> bool:
        return (0 <= y < self.height and
                0 <= x < self.width)


    def turn(self):
        idx = self.directions.index(self.current_dir)
        self.current_dir = self.directions[(idx + 1) % 4]

    def visited(self):
        print("The guard has visited", self.amount_visited, "squares!")

    def move(self, map: list):
        while True:
            y, x = self.current_pos
            if not self.inside_map(y, x):
                break
            if map[y][x] != 'X':
                map[y][x] = 'X'
                self.amount_visited += 1
            dy = self.guard_dirs.get(self.current_dir)[Y]
            dx = self.guard_dirs.get(self.current_dir)[X]
            if not self.inside_map(y + dy, x + dx):
                    break
            if map[y + dy][x + dx] == WALL:
                self.turn()
                continue
            self.current_pos = (y + dy, x + dx)