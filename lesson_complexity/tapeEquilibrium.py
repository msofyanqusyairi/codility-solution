# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    # write your code in Python 2.7
    minResult = A[0]
    if (len(A)>=2 and len(A)<=100000):
        for i,v in enumerate(A):
            P = i+1
            if (P < len(A)):
                # print "-"
                # print sum(A[0:P])
                # print sum(A[P:len(A)])
                diff = abs(sum(A[:P]) - sum(A[P:len(A)]))
                if (diff < minResult):
                    minResult = diff

    return minResult

def solution2(A):
    # write your code in Python 2.7
    minResult = None
    temp = 0
    temp2 = sum(A)
    if (len(A)>=2 and len(A)<=100000):
        for i in xrange(1, len(A)):
            temp += A[i-1]
            temp2 -= A[i-1]
            diff = abs(temp - temp2)
            if (minResult is None):
                minResult = diff
            else:
                minResult = min(diff, minResult)

    return minResult

if __name__ == '__main__':
    A = [3,1,2,4,3]
    print solution2(A)