from logger import *

OUT = "/root/workspace/logs/tunnel_logs.txt"

def test_1():
    log("WARNING TEST",WARNING,OUT)
    log("ERROR TEST",ERROR,OUT)
    log("MESSEGE TEST",MESSAGE,OUT)
    log("SUCCESS TEST",SUCCESS,OUT)
    HEADER.color = COLORS['white']
    HEADER.header = "GET"
    log("request successfull !",HEADER)

test_1()