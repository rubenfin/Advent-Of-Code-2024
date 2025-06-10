


def equal_to_guard(c: str) -> bool:
    return (c in '^>v<')
    

def find_guard(mmap: list, height: int, width: int)-> list:
    for y in range(0, height):
        for x in range(0, width):
            if mmap[y][x] in '^>v<':
                return (y, x)

def move(mmap: list):


def main():
    guard = {
    '^': [-1, 0],
    '>': [0, 1],
    'v': [1, 0],
    '<': [0, -1]
    }
    wall = '#'
    mmap = []
    with open("../input.txt") as f:
        mmap = f.read().split('\n')
    height = len(mmap)
    width = len(mmap[0])
    g_location = find_guard(mmap, height, width)
    move(mmap)
    print(g_location)


if __name__ == "__main__":
    main()