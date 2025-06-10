from collections import defaultdict

def allowed(order: list, instructions: list, num: int, idx: int):
    required = order[num]

    for page in required:
        if page not in instructions:
            continue

        page_idx = instructions.index(page)

        if page_idx >= idx:
            return False

    return True

def change_places(order: list, instructions: list, num: int, idx: int):
    

def main():
    order = defaultdict(list)
    instructions = []
    with open("../input.txt") as f:
        while True:
            line = f.readline()
            if line == '\n':
                instructions = f.read().split('\n')
                break
            middle = line.find('|')
            first = line[:middle]
            second = line[middle+1:].strip()
            order[second].append(first)
    instructions = [instruction.split(',') for instruction in instructions]
    total = 0
    length = len(instructions)
    print(order)
    for y in range(0, length):
        size = len(instructions[y])
        for x in range(0, size):
            num = instructions[y][x]
            if not allowed(order, instructions[y], num, x):
                
                total +=  
    print(total)



if __name__ == "__main__":
    main()