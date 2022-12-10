# Capitalizes First Letter
def capitalizeFirst_1(string):
    stringL = string.split(" ")
    string2 = ""
    for i in range(0, len(stringL)):
        buffer = ""
        for j in range(0,len(stringL[i])):
            buffer += stringL[i][j].upper() if j == 0 else stringL[i][j]
        stringL[i] = buffer
        string2 += f"{stringL[i]} " if i != (len(stringL)-1) else f"{stringL[i]}"
    return string2