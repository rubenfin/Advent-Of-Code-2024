def valid(c: str) ->bool:
    return (c == 'M' or c == 'S')

def is_valid_X(top_left: str, top_right: str, bottom_left: str, bottom_right: str) -> bool:
    if not all(valid(c) for c in [top_left, top_right, bottom_left, bottom_right]):
        return False
    return top_right != bottom_left and top_left != bottom_right

def main():
    arr = []
    with open("../input.txt") as f:
        arr = f.read().split('\n')

    size = len(arr)
    total = 0
    for y in range(1, size - 1):
        for x in range(1, size - 1):
            if arr[y][x] == 'A':
                found_top_left = arr[y - 1][x - 1]
                found_top_right = arr[y - 1][x + 1]
                found_bottom_right = arr[y + 1][x + 1]
                found_bottom_left= arr[y + 1] [x - 1]
                total += is_valid_X(found_top_left, found_top_right, found_bottom_left, found_bottom_right)
    print(total)


if __name__ == "__main__":
    main()