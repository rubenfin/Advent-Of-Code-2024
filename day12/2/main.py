from collections import Counter

def main():
    with open("../input.txt") as f:
        arr = list(map(int, f.readline().split()))

    counts = Counter(arr)

    for _ in range(75):
        new_counts = Counter()
        for num, cnt in counts.items():
            if num == 0:
                new_counts[1] += cnt
            elif len(str(num)) % 2 == 0:
                s = str(num)
                mid = len(s) // 2
                left, right = int(s[:mid]), int(s[mid:])
                new_counts[left] += cnt
                new_counts[right] += cnt
            else:
                new_counts[num * 2024] += cnt
        counts = new_counts

    print(sum(counts.values()))


if __name__ == "__main__":
    main()
