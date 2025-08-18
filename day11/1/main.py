def main():
    with open("../input.txt") as f:
        arr = list(map(int, f.readline().split()))
    print(arr)

    for _ in range(25):
        copy = []
        for num in arr:
            if num == 0:
                copy.append(1)
            elif len(str(num)) % 2 == 0:
                s = str(num)
                mid = len(s) // 2
                left, right = int(s[:mid]), int(s[mid:])
                copy.extend([left, right])
            else:
                copy.append(num * 2024)
        arr = copy

    print(len(arr))


if __name__ == "__main__":
    main()
