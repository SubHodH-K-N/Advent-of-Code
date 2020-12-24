fin = open('input', 'r')
f = fin.read()
directions = list(f)
santa = directions[0::2]
robot = directions[1::2]
visited = set()
visited.add((0, 0))
x = 0
y = 0
#for direction in directions:
#    if direction == '^':
#        y += 1
#    elif direction == 'v':
#        y -= 1
#    elif direction == '>':
#        x += 1
#    else:
#        x -= 1
#    visited.add((x, y))

def housesCovered(lst, x, y):
    for l in lst:
        if l == '^':
            y += 1
        elif l == 'v':
            y -= 1
        elif l == '>':
            x += 1
        else:
            x -= 1
        visited.add((x, y))
housesCovered(santa, 0, 0)
housesCovered(robot, 0, 0)
print(len(visited))
