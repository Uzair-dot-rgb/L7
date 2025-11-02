# Check identity operater 
x = 5
if (type(x) is int):
    print("true")
else :
    print("false")
    
x = 5.0
if (type(x) is not float):
    print("false")   
else :
    print("true")
    
x = 20
y = 20
if x is y :
    print("x and y has the same identity")
y = 30
if x is not y :
    print("x and y don't have the same value")