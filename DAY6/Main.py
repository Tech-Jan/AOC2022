import filereader

list = filereader.readfile("Input")
print(list)

# part1
result = filereader.analyzefile(list, 4)
print(result)

# part2
result = filereader.analyzefile(list, 14)
print(result)
