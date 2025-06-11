from guard import Guard

def find_guard(mmap: list, height: int, width: int)-> list:
    for y in range(0, height):
        for x in range(0, width):
            if mmap[y][x] in '^>v<':
                return (y, x)

def main():
    mmap = []
    with open("../input.txt") as f:
        mmap = f.read().split('\n')
    mmap = [list(row) for row in mmap]
    height = len(mmap)
    width = len(mmap[0])
    g_location = find_guard(mmap, height, width)
    y, x = g_location[0], g_location[1]
    g = Guard(mmap[y][x], g_location,height, width)
    g.move(mmap)
    g.visited()
    g.obstacles()

if __name__ == "__main__":
    main()