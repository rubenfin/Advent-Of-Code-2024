
def check_arr(arr: list):
        increasing = False
        decreasing = False
        for i in range(0, len(arr) - 1):
            curr = int(arr[i])
            next = int(arr[i+1])
            diff = curr - next
            if increasing and curr > next:
                return False
            if decreasing and next > curr:
                return False
            if not(abs(diff) > 0 and abs(diff) <= 3):
                return False
            if next > curr:
                increasing = True
            else:
                decreasing = True
        return True
    

def main():
    
    with open("../input.txt") as f:
        arr = []
        total = 0
        for line in f:
            line = line.strip('\n')
            arr = line.split(' ')
            if check_arr(arr):
                    total+=1
                    continue
            for i in range(0, len(arr)):
                copy = arr[:]
                copy.pop(i)
                if check_arr(copy):
                    total+=1
                    break
        print(total)


if __name__ == "__main__":
    main()