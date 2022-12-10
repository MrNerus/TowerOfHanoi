
# "None" is received, it converts to ""
def noneFilter(inp, out):
    return out if inp in [None, None] else inp 

def capitalizeFirst(x: str):
    xRaw = x.split(" ")
    buffer = ""
    for i in range (0, len(xRaw)):
        xRaw[i] = xRaw[i][0].upper() + xRaw[i][1:]
        buffer += xRaw[i] + " "
    return buffer[:-1] # Removes extra Space

def sFill(x: str, char: str, totalLen: int, pos: str):
    toFillLen = totalLen - len(x)
    if toFillLen < 0:
        return x[:totalLen]
    else:
        newStr = ""
        for i in range(0,toFillLen):
            newStr += str(char)
    if pos.upper() == "LEFT":
        newStr += x
    else:
        newStr = x + newStr
    return newStr
            
def printWithNull(x):
    print(x, end = "")
def printWithSpace(x):
    print(x, end = " ")
def printWithKeyCode(x, keyCode: int):
    # print with keyCode 8 for intresting result. It is backspace.
    print(x, end = chr(keyCode))

    