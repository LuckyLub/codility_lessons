"""Write a function that, given an array A consisting of N integers fulfilling 
the above conditions, returns the value of the unpaired element."""


def solution(A):
    while True:
        p = A[0]
        B = A[1:]
        if p in B:
            j = B.index(p)
            A.pop(0)
            A.pop(j)
        else:
            return p

if __name__ == "__main__":
    A = [9, 3, 9, 3, 9, 7, 9]
    print(solution(A))