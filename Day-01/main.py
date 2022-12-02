caloryFile = open("input.txt", "r")
elfCount = 0
line = caloryFile.readline()
caloryTally = [[]]
calorySums = []
topThreeElves = []

while line: #Parse all lines one at a time
    line = line.strip()
    if line == "": #Where a line is blank the next line will be a new elf
        elfCount += 1
        caloryTally.append([])
    else:
        caloryTally[elfCount].append(int(line)) #Add to current elf's tally
    line = caloryFile.readline()

for elf in caloryTally: #Sum up and store each elf's total calories so we can work out the top calory count
    calorySums.append(sum(elf))

print("Elf no. %d has the most calories (%d)" %(calorySums.index(max(calorySums))+1, max(calorySums)))

cumulativeTopTotal = 0
for i in range(3):
    topThreeElves.append([]) #Add a blank array for elf
    index = calorySums.index(max(calorySums)) #Get index to store elf number and get max
    topThreeElves[i].append(index+1) #Store elf number in element 0 (future-proofing)
    calories = calorySums.pop(index) #Pops max from sum array so that in the next iteration, it's the next highest
    topThreeElves[i].append(calories)
    cumulativeTopTotal += calories #Add to running total for task answer

print(topThreeElves)
print(cumulativeTopTotal)
