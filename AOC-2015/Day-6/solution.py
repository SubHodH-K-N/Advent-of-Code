f = open('input', 'r')
lines = f.readlines()
instructions = [line.rstrip() for line in lines]

lights = [[False for _ in range(1000)] for _ in range(1000)]
brightness = [[0 for _ in range(1000)] for _ in range(1000)]

count = 0
bright = 0

for instruction in instructions:
	command = instruction.split()
	
	if command[0] == 'toggle':
		startRow, startCol = map(int, command[1].split(','))
		endRow, endCol = map(int, command[3].split(','))
		for row in range(startRow, endRow + 1):
			lights[row][startCol:endCol + 1] = [not l for l in lights[row][startCol:endCol + 1]]
			brightness[row][startCol:endCol + 1] = [b + 2 for b in brightness[row][startCol:endCol + 1]]
	else:
		startRow, startCol = map(int, command[2].split(','))
		endRow, endCol = map(int, command[4].split(','))

		if command[1] == 'on':
			for row in range(startRow, endRow + 1):
				lights[row][startCol:endCol + 1] = [True for _ in lights[row][startCol:endCol + 1]]
				brightness[row][startCol:endCol + 1] = [ b + 1 for b in brightness[row][startCol:endCol + 1]]
		else:
			for row in range(startRow, endRow + 1):
				lights[row][startCol:endCol + 1] = [False for _ in lights[row][startCol:endCol + 1]]
				brightness[row][startCol:endCol + 1] = [b - 1 if b != 0 else 0 for b in brightness[row][startCol:endCol + 1]]
for row in range(1000):
	for col in range(1000):
		if lights[row][col] == True:
			count += 1
		bright += brightness[row][col]
print(count, " ", bright)
