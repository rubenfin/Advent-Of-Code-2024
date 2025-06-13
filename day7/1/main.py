def do_operations(values: list, operations: list):
    result = 0
    stack = values.copy()
    stack.reverse()
    for i in range(0, len(operations)):
        num1 = stack.pop()
        num2 = stack.pop()
        print(num1, operations[i], num2)
        if operations[i] == '+':
            stack.append(num1+num2)
        else:
            stack.append(num1*num2)
            print(num1*num2)
    print("RESULT", stack[0])
    return stack[0]

def add_operation(operations: list):
    operations.insert(0, '+')
    operations.pop()

def calculate(result: int, values: list):
    length = len(values)
    operations = ['*'] * (length - 1)
    accepted = [0] * length
    res = 0
    for i in range(0, length):
        while True:
                for i in range(0, operations):
                    for j in range(0, operations):
                add_operation(operations)
                if res == result:
                    accepted[i] = 1
                if '*' not in operations:
                    break
    return accepted

def go_through_numbers(results: list, arr: list):
    idx = 0
    for idx in range(0, len(results)):
        calculate(results[idx], arr[idx])

def main():
    with open("../input.txt") as f:
        lines = f.readlines()
        results = []
        arr = list()
        for line in lines:
            result = line[:line.find(':')]
            line = line[line.find(':') + 2:]
            results.append(result)
            numbers = []
            while line:
                space = line.find(' ')
                if space == -1:
                    space = line.find('\n')
                if space == -1:
                    break
                numbers.append(int(line[:space]))
                line = line[space+1:]
            arr.append(numbers)
        go_through_numbers(results, arr)
            
if __name__ == "__main__":
    main()
