lines = open("vm/SimpleAdd.vm", "r")
linesPassed = 0

for line in lines:
    stripped_line = line.strip("\n")
    print(f'{stripped_line}')
