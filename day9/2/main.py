def check_space(storage, idx, c, front):
    space = 1
    while idx > 0 and idx < len(storage) and storage[idx] == c:
        if front:
            idx+=1
        else:
            idx-=1
        space+=1
    return space

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
    while begin < end:
        # check for next .
        while begin < len(storage) and storage[begin] != '.':
            begin+=1
        if begin >= end:
            break
        #check how long the dot is
        to_fill = check_space(storage, begin, '.', True)
        # skip all dots to find the next number\
        while end > 0 and storage[end] == '.':
            end-=1
        #check the amount of numbrs
        needed = check_space(storage, end, storage[end], False)
        print(to_fill, needed)
        if to_fill < needed:
            while end > 0 and storage[end] != '.':
                end-=1
            continue
        else:                
            i = 0
            while i < needed:
                print(storage[begin], storage[end])
                storage[begin], storage[end] = storage[end], storage[begin]
                i+= 1
                begin +=1
        begin += 1

    print(storage)
    # print(res)

if __name__ == "__main__":
    main()