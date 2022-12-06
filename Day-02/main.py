strategyFile = open("input-1.txt", "r")
line = strategyFile.readline()
#AX ROCK | BY PAPER | CZ SCISSORS
myScore = 0
opponentScore = 0
while line: #Parse all lines one at a time
    line = line.strip()
    opponentChoice, myChoice = line.split(" ")
    if myChoice == "X":
        myChoice = "C" if (opponentChoice == "A") else chr(ord(opponentChoice) -1)
    elif myChoice == "Y":
        myChoice = chr(ord(opponentChoice))
    else:
        myChoice = "A" if (opponentChoice == "C") else chr(ord(opponentChoice) + 1)

    charDif = ord(myChoice) - ord(opponentChoice)
    if charDif == 0:
        myScore += 3
        opponentScore += 3
    elif (charDif == 1 or charDif == -2): # Win conditions
        myScore += 6
    else:
        opponentScore +=  6
    opponentScore += ord(opponentChoice)-64 # Subtract by offset of 64 so that A=1 B=2 etc.
    myScore += ord(myChoice)-64
    line = strategyFile.readline()

print(myScore)
print(opponentScore)
