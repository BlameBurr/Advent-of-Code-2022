pairFile = open("input-3.txt", "r")
line = pairFile.readline()
fullOverlapCount = 0
partOverlapCount = 0
while line: #Parse all lines one at a time
    line = line.strip()
    elfOne, elfTwo = line.split(",")
    elfOneList = range(int(elfOne.split("-")[0]), int(elfOne.split("-")[1])+1)
    elfTwoList = range(int(elfTwo.split("-")[0]), int(elfTwo.split("-")[1])+1)
    if any(numbers in elfOneList for numbers in elfTwoList) or any(numbers in elfTwoList for numbers in elfOneList):
        partOverlapCount += 1
    if all(numbers in elfOneList for numbers in elfTwoList) or all(numbers in elfTwoList for numbers in elfOneList):
        fullOverlapCount += 1
    line = pairFile.readline()

print(fullOverlapCount)
print(partOverlapCount)
