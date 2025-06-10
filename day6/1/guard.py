Y = 0
X = 1
WALL = '#'

class Guard:
    def __init__(self, current_dir: str, current_pos: list, height: int, width: int):
        self.current_dir = current_dir
        self.current_pos = current_pos
        self.height = height
        self.width = width
        self.guard_dirs = {
            '^' : [-1, 0],
            '>' : [0, 1],
            'v' : [1, 0],
            '<' : [0, -1],
        }
    
    def inside_map(self) -> bool:
        return (0 <= self.current_pos[Y] < self.height and
                0 <= self.current_pos[X] < self.width)

    def turn(self):
        

    def move(self, map: list):
        while True:
            if not self.inside_map():
                break
            y, x = self.current_pos
            dy = self.guard_dirs.get(self.current_dir)[Y]
            dx = self.guard_dirs.get(self.current_dir)[X]
            if map[y + dy][x + dx] == WALL:
