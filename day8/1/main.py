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
    end = 


if __name__ == "__main__":
    main()
