

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

    d = {}

    for x in list2:
        if (d.get(x)):
            d[x] +=1
        else:
            d[x] = 1
    res = 0

    for x in list1:
        found = d.get(x)
        if found == None:
            found = 0
        res += int(x) * found
    
    print(res)

if __name__ == "__main__":
    main()
    