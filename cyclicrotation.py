"""Write a function that, given an array A consisting of N integers and an integer K, 
returns the array A rotated K times."""

def solution(A,K):
    la = len(A)

    if K >= la:
        K = K % la
    if K == 0:
        return A
    head = A[la-K:]
    tail = A[:la-K]
    head.extend(tail)
    return head

if __name__ == "__main__":
    A = [3, 8, 9, 7, 6]
    K = 3
    print(solution(A,K))