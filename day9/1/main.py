def main():
    storage = ""
    with open("../input.txt") as f:
        line = f.readline()
    id = 0
    for n in range(len(line)):
        if n % 2 == 0:
            storage += str(id) * int(line[n])
            id+=1
        else:
            storage += '.' * int(line[n])
    begin = 0
    end = len(storage) - 1
    res = int(0)
    
    while begin <= end:
        if storage[begin] != '.':
            res += begin * int(storage[begin])
        else:
            while end > 0 and storage[end] == '.':
                end-=1
            print(begin, end)
            print(storage[begin], storage[end])
            if begin > end:
                break
            res += begin * int(storage[end])
            end-=1
        begin+=1
    print(res)

if __name__ == "__main__":
    main()
