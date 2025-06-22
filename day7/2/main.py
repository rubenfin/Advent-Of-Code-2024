from itertools import product

def do_operations(values: list, operations: list):
    stack = values.copy()
    stack.reverse()
    for i in range(len(operations)):
        num1 = stack.pop()
        num2 = stack.pop()
        if operations[i] == '+':
            stack.append(num1 + num2)
        elif operations[i] == '*':
            stack.append(num1 * num2)
        else:
            stack.append((int(str(num1) + str(num2))))
    return stack[0]


def calculate(target: int, values: list)-> int:
    n = len(values)
    if n == 0:
        return 0
    
    for ops in product(['+', '*', '||'], repeat=n-1):
        result = do_operations(values, list(ops))
        if result == target:
            return result
    return 0

def go_through_numbers(results: list, arr: list):
    sum = 0
    for i in range(len(results)):
        target = results[i]
        numbers = arr[i]
        sum += calculate(target, numbers)
    print(sum)

def main():
    with open("../input.txt") as f:
        lines = f.readlines()
        results = []
        arr = []
        for line in lines:
            if ':' not in line:
                continue
            result_str, numbers_str = line.strip().split(':')
            results.append(int(result_str.strip()))
            numbers = list(map(int, numbers_str.strip().split()))
            arr.append(numbers)
        go_through_numbers(results, arr)

if __name__ == "__main__":
    main()
