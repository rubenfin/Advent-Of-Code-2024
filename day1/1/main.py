

def main():
    list1 = []
    list2 = []
    with open("../input.txt") as f:
        for line in f:
            space = line.find(' ')
            list1.append(line[:space])
            list2.append(line[space+3:-1])
    
    list1.sort()
    list2.sort()

    
    diff = 0
    for i, line in enumerate(list1):
        diff += abs(int(list1[i]) - int(list2[i]))
    print(diff)

if __name__ == "__main__":
    main()
    