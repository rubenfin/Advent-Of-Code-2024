import copy

Y = 0
X = 1
WALL = '#'

class Guard:
    def __init__(self, current_dir: str, current_pos: list, height: int, width: int):
        self.current_dir = current_dir
        self.current_pos = current_pos
        self.original_dir = current_dir  # Store original direction
        self.original_pos = current_pos.copy()  # Store original position
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
        self.visited_positions = set()
    
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

    def simulate(self, grid: list, obstacle_y: int, obstacle_x: int):
        if (obstacle_y, obstacle_x) == tuple(self.original_pos):
            return
        
        grid_copy = copy.deepcopy(grid)
        if not self.inside_map(obstacle_y, obstacle_x) or grid_copy[obstacle_y][obstacle_x] == WALL:
            return
            
        grid_copy[obstacle_y][obstacle_x] = WALL
        
        pos = list(self.original_pos)
        direction = self.original_dir
        visited_states = set()
        
        while True:
            y, x = pos
            if not self.inside_map(y, x):
                break
                
            state = (y, x, direction)
            if state in visited_states:
                self.total_obstacles += 1
                return
            visited_states.add(state)
            
            dy, dx = self.get_coordinates_for_turn(direction)
            next_y, next_x = y + dy, x + dx
            
            if not self.inside_map(next_y, next_x):
                break
                
            if grid_copy[next_y][next_x] == WALL:
                direction = self.get_next_direction(direction)
                continue
                
            pos = [next_y, next_x]

    def move(self, grid: list):
        while True:
            y, x = self.current_pos
            if not self.inside_map(y, x):
                break
                
            if (y, x) not in self.visited_positions:
                self.visited_positions.add((y, x))
                if grid[y][x] != WALL:
                    grid[y][x] = 'X'
                self.amount_visited += 1
            
            dy, dx = self.get_coordinates_for_turn(self.current_dir)
            next_y, next_x = y + dy, x + dx
            
            if not self.inside_map(next_y, next_x):
                break
                
            if grid[next_y][next_x] == WALL:
                self.turn()
                continue
                
            self.current_pos = [next_y, next_x]
        
        for pos_y, pos_x in self.visited_positions:
            self.simulate(grid, pos_y, pos_x)