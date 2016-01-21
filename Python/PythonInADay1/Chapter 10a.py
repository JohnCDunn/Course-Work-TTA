someValue = 5

def letsAdd(x,y):
    addition = x + y
    someValue = 10
    return addition

def subtraction(x,y):
    subtract = x- y
    return subtract

def moreSubtraction(x,y,z):
    subtract = x-y-z
    return subtract



print "addition 3+5 = " + str(letsAdd(3, 5))
print "some value " + str(someValue)
print "subtraction 10-4 = " + str(subtraction(10,4))
print "more subtraction 40-3-11 = " + str(moreSubtraction(40,3,11))
