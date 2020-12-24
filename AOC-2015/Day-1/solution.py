def partOne(instructions):
    count = 0
    for inst in instructions:
        if inst == '(':
            count += 1
        else:
            count -= 1

    print(count)

def partTwo(instructions):
    count = 0
    for i in range(len(instructions)):
        if instructions[i] == '(':
            count += 1
        else:
            count -= 1

        if count == -1:
            print(i+1)
            break

inputFile = open('input', 'r')

floors = inputFile.read().rstrip()

instructions = list(floors)

#Solutions
print('2015 Day 1 Part 1 Solution:')
partOne(instructions)
print('2015 Day 1 Part 2 Solution:')
partTwo(instructions)
