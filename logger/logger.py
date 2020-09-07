import time
import os

from datetime import datetime


COLORS = {
    "reset":"\u001b[0m",
    "red":"\u001b[31m",
    "black": "\u001b[30m",
    "green": "\u001b[32m",
    "yellow": "\u001b[33m",
    "blue": "\u001b[34m",
    "white": "\u001b[37m",
}


def error(msg:str)->str:
    t = datetime.now().strftime("%Y-%m-%d %X")
    col,_ = os.get_terminal_size()
    msg = f'{COLORS["red"]} [ERR]{COLORS["reset"]} {msg}'
    return f'{msg} {" "*(col-len(msg)-len(t))} [ {t} ]'

def warning(msg:str)->str:
    t = datetime.now().strftime("%Y-%m-%d %X")
    col,_ = os.get_terminal_size()
    msg = f'{COLORS["yellow"]} [WRN]{COLORS["reset"]} {msg}'
    return f'{msg} {" "*(col-len(msg)-len(t))} [ {t} ]'

def success(msg:str)->str:
    t = datetime.now().strftime("%Y-%m-%d %X")
    col,_ = os.get_terminal_size()
    msg = f'{COLORS["green"]} [SUC]{COLORS["reset"]} {msg}'
    return f'{msg} {" "*(col-len(msg)-len(t))} [ {t} ]'

def message(msg:str)->str:
    t = datetime.now().strftime("%Y-%m-%d %X")
    col,_ = os.get_terminal_size()
    msg = f'{COLORS["blue"]} [MSG]{COLORS["reset"]} {msg}'
    return f'{msg} {" "*(col-len(msg)-len(t))} [ {t} ]'

def custom(head:str,msg:str,color:str="white")->str:
    t = datetime.now().strftime("%Y-%m-%d %X")
    col,_ = os.get_terminal_size()
    msg = f'{COLORS[color]} [{head}]{COLORS["reset"]} {msg}'
    return f'{msg} {" "*(col-len(msg)-len(t))} [ {t} ]'

def test():
    print (warning("WARNING TEST"))
    print (error("ERROR TEST"))
    print (message("MESSEGE TEST"))
    print (success("SUCCESS TEST"))
    print (custom("GET","request successfull !",))

if __name__ == "__main__":
    test()