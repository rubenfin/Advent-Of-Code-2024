class Guard:
    def __init__(self, current_dir: str, current_pos: list):
        self.current_dir = current_dir
        self.current_pos = current_pos
        self.positions = {
            '^' : [-1, 0],
            '>' : [0, 1],
            'v' : [1, 0],
            '<' : [0, -1],
        }
    
    def move(self, map: list):
        