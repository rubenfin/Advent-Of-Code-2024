from collections import defaultdict

def main():
    garden = []
    with open("../input.txt") as f:
        for line in f:
            line = line.rstrip('\n')
            garden.append(line)
    h = len(garden)
    w = len(garden[0])
    area = defaultdict(int)
    perimeter = defaultdict(int)
    seen = set()
    def find_perimeter(y, x, find, total_areas):
        if y == 0 or garden[y-1][x] != find:
            perimeter[total_areas]+=1
        if x == 0 or garden[y][x-1] != find:
            perimeter[total_areas]+=1
        if y + 1 >= h or garden[y+1][x] != find:
            perimeter[total_areas]+=1
        if x + 1 >= w or garden[y][x+1] != find:
            perimeter[total_areas]+=1

    def find_area(y, x, find, total_areas):
        if y >= h or x >= w or y < 0 or x < 0:
            return
        if garden[y][x] != find or (y, x) in seen:
            return
        seen.add((y, x)) 
        area[total_areas] +=1
        find_perimeter(y, x, find, total_areas)
        find_area(y+1, x, find, total_areas)
        find_area(y-1, x, find, total_areas)
        find_area(y, x+1, find, total_areas)
        find_area(y, x-1, find, total_areas)

    total_areas = 0
    for y in range(h):
        for x in range(w):
            find_area(y, x, garden[y][x], total_areas)
            total_areas+=1
    print(seen)
    print(area)
    print(perimeter)
    res = 0
    for key, value in area.items():
        res += perimeter[key] * value
    print(res)

if __name__ == "__main__":
    main()
