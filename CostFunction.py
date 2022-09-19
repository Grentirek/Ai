def keykep(dictionary, n):
    if n < 0:
        n += len(dictionary)
    for i, key in enumerate(dictionary.keys()):
        if i == n:
            return key
    raise IndexError("dictionary index out of range")

data = {1:1, 2:2, 3:3}
m = 3 #The number of examples
teta1 = 1 #How do you know that?
teta2 = 0

def h0(x):
    return teta2 + teta1 * x
    
def J(teta1, teta2):
    for i in range(1, m+1):
        resultofJ = 1/(2*m)*((keykep(h0(data), i) - h0(data)[i])^2)
    return resultofJ
    
J(1, 2)