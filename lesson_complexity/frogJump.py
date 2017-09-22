import math

# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"
# COUNT = 0
def solution(X, Y, D):
    # write your code in Python 2.7
    print 'X: {0}'.format(X)
    print 'Y: {0}'.format(Y)
    if (X < Y):
        return solution(X+D, Y, D) + 1
    else:
        return 0

def solution2(X, Y, D):
    # write your code in Python 2.7
    if ((X<=Y) and (X>=1 and X<=1000000000) and (Y>=1 and Y<=1000000000) and (D>=1 and D<=1000000000)):
        newX = X - X
        newY = Y - X
        newD = D
        print 'step1: {0}'.format(newX)
        print 'step2: {0}'.format(newY)
        print 'step3: {0}'.format(newD)
        result = float(newY) / float(newD)
        resultDiv = newY / newD
        if (result-resultDiv)>0:
            return int(result)+1
        return int(result)
    else:
        return 0

if __name__ == '__main__':
    X=90
    Y=85
    D=30
    a = solution2(X, Y, D)
    print a