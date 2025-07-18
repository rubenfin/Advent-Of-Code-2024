def main():
    storage = []
    with open("../input.txt") as f:
        line = f.readline().strip()
    
    id = 0
    for n in range(len(line)):
        if n % 2 == 0:
            storage.extend([id] * int(line[n]))
            id += 1
        else:
            storage.extend(['.'] * int(line[n]))
    
    begin = 0
    end = len(storage) - 1
    res = 0
    
    while begin <= end:
        if storage[begin] != '.':
            res += begin * storage[begin]
        else:
            while end > 0 and storage[end] == '.':
                end -= 1
            if begin > end:
                break
            res += begin * storage[end]
            end -= 1
        begin += 1
    
    print(res)

if __name__ == "__main__":
    main()