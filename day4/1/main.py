def find_xmas(arr: list, y: int, x: int, size: int, xmas: list, curr: int, dy: int, dx: int) -> int:
    if curr == 4:
        return 1
    if x < 0 or y < 0 or y >= size or x >= size:
        return 0
    if arr[y][x] != xmas[curr]:
        return 0
    return find_xmas(arr, y + dy, x + dx, size, xmas, curr + 1, dy, dx)

def main():
    xmas = ['X', 'M', 'A', 'S']
    arr = []
    with open("../input.txt") as f:
        arr = f.read().split('\n')

    size = len(arr)
    total = 0
    for y in range(0, size):
        for x in range(0, size):
            for dy in range(-1, 2):
                for dx in range(-1, 2):
                    if dy == 0 and dx == 0:
                        continue
                    total += find_xmas(arr, y, x, size, xmas, 0, dy, dx)

    print(total) 

if __name__ == "__main__":
    main()