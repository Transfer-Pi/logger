from logger import *

def test_1():
    print (warning("WARNING TEST"))
    print (error("ERROR TEST"))
    print (message("MESSEGE TEST"))
    print (success("SUCCESS TEST"))
    print (custom("GET","request successfull !",))

test_1()