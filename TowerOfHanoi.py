from featureArd.TerminalColor import *
from featureArd.StringOperation import printWithNull, printWithSpace


columnA: list = []
columnB: list = []
columnC: list = []
columnABackup: list = []
stepsUsed: list = []
validCommands: list = ["AB", "AC", "BA", "BC", "CA", "CB",
"EXIT", "SHOWSTEPS", "COUNTSTEPS", "SHOW", "SUBMIT", "MODE 1", "MODE 2", "HELP", "COMMANDS"]
displayMode = 1

brickCount = int(input(f"{COL_CYAN}How many brick do you need? {COL_RESET}"))
if brickCount < 3:
    print(f"{COL_RED}Program terimated. Number of brick can not be less than three.{COL_RESET}")
    exit()
digitLength = len(str(brickCount))

for i in range(0,brickCount):
    columnA.append(brickCount-i)
    columnABackup.append(brickCount-i)
    columnB.append(None)
    columnC.append(None)


def consoleDispaly():
    print(f"{COL_CYAN}A: {COL_RESET}{columnA}")
    print(f"{COL_CYAN}B: {COL_RESET}{columnB}")
    print(f"{COL_CYAN}C: {COL_RESET}{columnC}")
# print(f"{type(a)}")

def towerDisplay():
    for row in range(0, brickCount):
        
        printWithNull("  ")
        if columnA[brickCount- row - 1] != None:
            printWithNull(f"={str(columnA[brickCount- row - 1]).zfill(digitLength)}=")
        else:
            printWithNull(f" ")
            for ele in range(0,digitLength):
                printWithNull("|")
            printWithNull(f" ")

        printWithNull("  ")
        if columnB[brickCount- row - 1] != None:
            printWithNull(f"={str(columnB[brickCount- row - 1]).zfill(digitLength)}=")
        else:
            printWithNull(f" ")
            for ele in range(0,digitLength):
                printWithNull("|")
            printWithNull(f" ")
        printWithNull("  ")
        if columnC[brickCount- row - 1] != None:
            printWithNull(f"={str(columnC[brickCount- row - 1]).zfill(digitLength)}=")
        else:
            printWithNull(f" ")
            for ele in range(0,digitLength):
                printWithNull("|")
            printWithNull(f" ")
        print("")
    totalWidth = (2*6+digitLength*3)
    for i in range(0,totalWidth):
        printWithNull("-")
    print("")
    for i in range(0,totalWidth):
        if i == int(totalWidth/4)+0:
            printWithNull("A")
        elif i == int(2*totalWidth/4)+1:
            printWithNull("B")
        elif i == int(3*totalWidth/4)+2:
            printWithNull("C")
        else:
            printWithNull(" ")
    print("")

def showCommands():    
    printWithSpace(f"{COL_CYAN}Commands available: {COL_RESET}")
    for i in validCommands:
        printWithSpace(f"{COL_ORANGE}{i}{COL_CYAN},{COL_RESET}")
    print("")  

def help():
    print(f"{COL_CYAN} AB {COL_YELLOW} - Move top Brick from A -> B.{COL_RESET}")
    print(f"{COL_CYAN} AC {COL_YELLOW} - Move top Brick from A -> C.{COL_RESET}")
    print(f"{COL_CYAN} BA {COL_YELLOW} - Move top Brick from B -> A.{COL_RESET}")
    print(f"{COL_CYAN} BC {COL_YELLOW} - Move top Brick from B -> C.{COL_RESET}")
    print(f"{COL_CYAN} CA {COL_YELLOW} - Move top Brick from C -> A.{COL_RESET}")
    print(f"{COL_CYAN} CB {COL_YELLOW} - Move top Brick from C -> B.{COL_RESET}")
    print(f"{COL_CYAN} EXIT {COL_YELLOW} - Exit out of this game.{COL_RESET}")
    print(f"{COL_CYAN} SHOWSTEPS {COL_YELLOW} - Displays every valid steps you have used.{COL_RESET}")
    print(f"{COL_CYAN} COUNTSTEPS {COL_YELLOW} - Counts every valid moves you have used.{COL_RESET}")
    print(f"{COL_CYAN} SHOW {COL_YELLOW} - Shows the tower again.{COL_RESET}")
    print(f"{COL_CYAN} SUBMIT {COL_YELLOW} - Checks if game is complete or not. Shows yor valid moves and Exits if game is solved.{COL_RESET}")
    print(f"{COL_CYAN} MODE 1 {COL_YELLOW} - Shows visuals in Column mode.{COL_RESET}")
    print(f"{COL_CYAN} MODE 2 {COL_YELLOW} - Shows visuals in List mode. [useful for debugging]{COL_RESET}")
    print(f"{COL_CYAN} HELP {COL_YELLOW} - Shows this screen{COL_RESET}")

    print(f"\n{COL_CYAN} Note: CASE InSensitive.{COL_RESET}")

    print(f'''\n\n{COL_CYAN} Comming Soon [May Be] [Not A Promise]{COL_YELLOW}
    UNDO Command,
    Game mode [Precise Move Mode, Limited Move Mode, Free Move Mode],
    Automatic game complete detection
    Add README.md for github explaining many things{COL_RESET}\n\n''')

showCommands()
print("\n\n")
towerDisplay() if displayMode == 1 else consoleDispaly()

def execute(source: list, destination:list):
    sucessFlag = 0
    if source[0] == None:
        print(f"{COL_RED}Empty source{COL_RESET}")
        return [sucessFlag, source, destination]
    if destination[brickCount-1] != None:
        print(f"{COL_RED}Destination Full{COL_RESET}")
        return [sucessFlag, source, destination]
    topOfSourceD = 0 # topmost DATA_SLOT of source
    while source[topOfSourceD] != None:
        if topOfSourceD == brickCount - 1:
            break
        if source[topOfSourceD + 1] == None:
            break
        topOfSourceD += 1
    topOfDestinationE = 0 # bottom-most EMPTY_SLOT of destination OR one step top of all data
    while destination[topOfDestinationE] != None:
        topOfDestinationE += 1
        if topOfDestinationE == brickCount - 1:
            break
    if topOfDestinationE == 0:
        destination[topOfDestinationE] = source[topOfSourceD]
        source[topOfSourceD] = None
        sucessFlag = 1
        return [sucessFlag, source, destination]
    if destination[topOfDestinationE-1] < source[topOfSourceD]:
        print(f"{COL_RED}Invalid Step{COL_RESET}")
        return [sucessFlag, source, destination]
    destination[topOfDestinationE] = source[topOfSourceD]
    source[topOfSourceD] = None
    sucessFlag = 1
    return [sucessFlag, source, destination]

def showSteps():
    for i in stepsUsed:
        print(f"{COL_CYAN}{i}{COL_RESET}")
    countSteps()

def countSteps():
    print(f"{COL_CYAN}{len(stepsUsed)} steps used so far.{COL_RESET}")

def submit():
    if columnABackup == columnC:
        showSteps()
        print(f"{COL_LIME}Congrats! you have done it sucessfully. Well Done!{COL_RESET}")
        exit()
    else:
        print(f'''{COL_ORANGE}Nope! Answer is not complete yet.
        All element of column a should be in column C in exact order{COL_RESET}''')

while True:
    uCommand = str(input(f"{COL_CYAN}Enter your command: {COL_RESET}")).upper()
    if uCommand not in validCommands:
        print(f"{COL_RED}Wrong Command!{COL_RESET}")
        showCommands()
        continue
    elif uCommand == "AB":
        ret = execute(columnA, columnB)
        if (ret[0]) == 1:
            stepsUsed.append("A -> B")
            columnA, columnB = ret[1], ret[2]
            towerDisplay() if displayMode == 1 else consoleDispaly()
            continue
        continue
    elif uCommand == "AC":
        ret = execute(columnA, columnC)
        if (ret[0]) == 1:
            stepsUsed.append("A -> C")
            columnA, columnC = ret[1], ret[2]
            towerDisplay() if displayMode == 1 else consoleDispaly()
            continue
        continue
    elif uCommand == "BA":
        ret = execute(columnB, columnA)
        if (ret[0]) == 1:
            stepsUsed.append("B -> A")
            columnB, columnA = ret[1], ret[2]
            towerDisplay() if displayMode == 1 else consoleDispaly()
            continue
        continue
    elif uCommand == "BC":
        ret = execute(columnB, columnC)
        if (ret[0]) == 1:
            stepsUsed.append("B -> C")
            columnB, columnC = ret[1], ret[2]
            towerDisplay() if displayMode == 1 else consoleDispaly()
            continue
        continue
    elif uCommand == "CA":
        ret = execute(columnC, columnA)
        if (ret[0]) == 1:
            stepsUsed.append("C -> A")
            columnC, columnA = ret[1], ret[2]
            towerDisplay() if displayMode == 1 else consoleDispaly()
            continue
        continue
    elif uCommand == "CB":
        ret = execute(columnC, columnB)
        if (ret[0]) == 1:
            stepsUsed.append("C -> B")
            columnC, columnB = ret[1], ret[2]
            towerDisplay() if displayMode == 1 else consoleDispaly()
            continue
        continue
    elif uCommand == "EXIT":
        print(f"{COL_CYAN}Closing Game...{COL_RESET}")
        exit()
    elif uCommand == "SHOWSTEPS":
        showSteps()
        continue
    elif uCommand == "COUNTSTEPS":
        countSteps()
        continue
    elif uCommand == "SHOW":
        towerDisplay() if displayMode == 1 else consoleDispaly()
        continue
    elif uCommand == "SUBMIT":
        submit()
        continue
    elif uCommand == "MODE 1":
        displayMode = 1
        continue
    elif uCommand == "MODE 2":
        displayMode = 2
        continue
    elif uCommand == "COMMANDS":
        showCommands()
        continue
    elif uCommand == "HELP":
        help()
        continue
    else:
        continue



# Special thanks to Santosh Bhandari [https://www.github.com/?????]
# for guiding me through Data structure and algorithm 