
def main():
    with open("../input.txt") as f:
         lines = [line.rstrip('\n') for line in f]
    h = len(lines)
    w = len(lines[0])
    trail = [[int(lines[y][x]) for x in range(w)] for y in range(h)]
    res = 0
    def find_trail(y, x, elevation):
        nonlocal total_trails
        if y >= h or y < 0 or x >= w or x < 0:
            return
        if trail[y][x] != elevation:
            return
        if elevation == 9:
            total_trails += 1
            return
        find_trail(y + 1, x, elevation+1)
        find_trail(y - 1, x, elevation+1)
        find_trail(y, x+1, elevation+1)
        find_trail(y, x-1, elevation+1)
    for y in range(h):
        for x in range(w):
            if trail[y][x] == 0:
                total_trails = 0
                find_trail(y, x, 0)
                res += total_trails
    print(res)
    return res
if __name__ == "__main__":
    main()