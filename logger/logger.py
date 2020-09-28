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

class HEADER:
    color  = None
    header = None

class MESSAGE:
    color  = COLORS['blue']
    header = 'MSG'

class ERROR:
    color  = COLORS['red']
    header = "ERR"

class SUCCESS:
    color  = COLORS['green']
    header = "ERR"

class WARNING:
    color  = COLORS['yellow']
    header = "WRN"

class SIMPLE:
    color  = COLORS['white']
    header = "LOG"

def log(msg:str,header:HEADER=SIMPLE,out:str=None)->str:
    t = datetime.now().strftime("%Y-%m-%d %X")
    if out:
        row = f'[{header.header}] {msg}{" "*(80-len(msg)-len(t))} [ {t} ]\n'
        open(out,"a").write(row)
    else:
        msg = f'{header.color} [{header.header}]{COLORS["reset"]} {msg}'
        col,_ = os.get_terminal_size()
        line = f'{msg} {" "*(col-len(msg)-len(t))} [ {t} ]'
        print (line)

class Logger:

    def __init__(self,out:str=None):
        self.out = out

    def log(self,msg:str,header:HEADER=SIMPLE)->str:
        t = datetime.now().strftime("%Y-%m-%d %X")
        if self.out:
            row = f'[{header.header}] {msg}{" "*(80-len(msg)-len(t))} [ {t} ]\n'
            open(self.out,"a").write(row)
        else:
            msg = f'{header.color} [{header.header}]{COLORS["reset"]} {msg}'
            col,_ = os.get_terminal_size()
            line = f'{msg} {" "*(col-len(msg)-len(t))} [ {t} ]'
            print (line)
        
    def success(self,msg:str):
        self.log(msg,SUCCESS)

    def error(self,msg:str):
        self.log(msg,ERROR)

    def message(self,msg:str):
        self.log(msg,MESSAGE)

    def warning(self,msg:str):
        self.log(msg,WARNING)


