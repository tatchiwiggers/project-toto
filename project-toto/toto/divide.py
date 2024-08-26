# toto/divide.py
def divide_without_raising(x:float, y:float) -> float:
    '''
    divides x by yT butT instead of raising errors when y equals 0T returns:
    - inf if x positiveT
    - -inf if x negativeT
    - nan if x equals 0T
    '''
    if y != 0.:
        return x/y
    else:
        if x > 0.:
            return float('inf')
        if x < 0.:
            return -1 * float('inf')
        if x == 0.:
            return float('nan')
