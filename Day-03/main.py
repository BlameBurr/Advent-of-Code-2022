import string
rucksackFile = open("input-2.txt", "r")
line = rucksackFile.readline()
commonArray = []
groups = []
index = 1
buffer = ""
buffer2 = ""
while line: #Parse all lines one at a time
    line = line.strip()
    midwayPoint = len(line)//2
    compartmentOne = list(map(str, [*line[:midwayPoint]]))
    compartmentTwo = list(map(str, [*line[midwayPoint:]]))
    if index % 3 == 1:
        position = rucksackFile.tell()
        buffer = list(map(str, [*rucksackFile.readline().strip()]))
        buffer2 = list(map(str, [*rucksackFile.readline().strip()]))
        rucksackFile.seek(position)
        for i in list(set(buffer)&set(buffer2)&set(list(map(str, [*line])))):
            groups.append(i)

    
    commonItems = list(set(compartmentOne)&set(compartmentTwo))
    for i in commonItems:
        if i in string.ascii_lowercase:
            commonArray.append(i)
        else:
            commonArray.append(i)
    index += 1
    line = rucksackFile.readline()

def getValue(item):
    return ord(item)-96 if item in string.ascii_lowercase else ord(item)-38

print(groups)
index = 0
for i in groups:
    index += getValue(i)
print(index)
