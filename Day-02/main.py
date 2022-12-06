strategyFile = open("input-1.txt", "r")
line = strategyFile.readline()
#AX ROCK | BY PAPER | CZ SCISSORS
myScore = 0
opponentScore = 0
while line: #Parse all lines one at a time
    line = line.strip()
    opponentChoice, myChoice = line.split(" ")
    if myChoice == "X":
        myChoice = "Z" if (opponentChoice == "A") else chr(ord(opponentChoice) + 22)
    elif myChoice == "Y":
        myChoice = chr(ord(opponentChoice)+23)
    else:
        myChoice = "X" if (opponentChoice == "C") else chr(ord(opponentChoice) + 24)

    myChoice = chr(ord(myChoice)-23) # Offset XYZ so they are ABC
    if opponentChoice == myChoice:
        myScore += 3
        opponentScore += 3
    elif (ord(myChoice) - ord(opponentChoice) == 1 or ord(myChoice) - ord(opponentChoice) == -2): #win
        myScore += 6
    else:
        opponentScore +=  6
    opponentScore += ord(opponentChoice)-64 # Subtract by offset of 64 so that A=1 B=2 etc.
    myScore += ord(myChoice)-64
    line = strategyFile.readline()

print(myScore)
print(opponentScore)
