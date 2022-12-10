    
class TerminalColor:
    # For text color.        COL_<NAME> = '\033[38;5;<VALUE>m'
    # Eg...                  COL_GREEN = '\033[38;5;2m'  # Green Text Color

    # For Background color.  COL_<NAME> = '\033[48;5;<VALUE>m'
    # Eg...                  COL_GREEN_BG = '\033[48;5;2m'  # Green Background Color

    # To reset color,        COL_RESET = '\033[0m'    # Reset color


    COL_RED = '\033[38;5;196m'
    COL_ORANGE = '\033[38;5;202m'
    COL_BROWN = '\033[38;5;130m'
    COL_YELLOW = '\033[38;5;226m'

    COL_GREEN = '\033[38;5;2m'
    COL_LIME = '\033[38;5;46m'
    COL_SPRINGGREEN = '\033[38;5;48m'
    
    COL_CYAN = '\033[38;5;51m'
    COL_STEELBLUE = '\033[38;5;39m'
    COL_BLUE = '\033[38;5;21m'
    
    COL_PURPLE = '\033[38;5;129m'
    COL_PINK = '\033[38;5;201m'
    COL_FUCHAIA = '\033[38;5;198m'
    
    COL_WHITE = '\033[38;5;255m'
    
    COL_BLACK = '\033[38;5;16m'
    COL_RESET = '\033[0m'  # Color Reset 


class StringOperation:
    # Capitalizes First Letter
    def capitalizeFirst(string):
        stringL = string.split(" ")
        string2 = ""
        for i in range(0, len(stringL)):
            buffer = ""
            for j in range(0,len(stringL[i])):
                buffer += stringL[i][j].upper() if j == 0 else stringL[i][j]
            stringL[i] = buffer
            string2 += f"{stringL[i]} " if i != (len(stringL)-1) else f"{stringL[i]}"
        return string2

    # "None" is received, it converts to ""
    def noneFilter(inp):
        return "" if inp != None else inp 
