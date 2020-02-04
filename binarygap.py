"""Write a function that, given a positive integer N, returns the length of its longest binary gap. 
The function should return 0 if N doesn't contain a binary gap. For example, given N = 1041 the 
function should return 5, because N has binary representation 10000010001 and so its longest binary 
gap is of length 5. Given N = 32 the function should return 0, because N has binary representation 
'100000' and thus no binary gaps."""

def solution(N):
   n = bin(N)
   ns = str(n)
   x = 0
   res = 0
   while True:
       i = ns.find("1")
       if i > 0 or x > 0:
           prev = x
           x += i
           dif = x - prev
           if prev != 0 and dif > 0 and dif > res:
               res = dif

           ns = ns[i+1:]
       else:
           break
   return res


if __name__ == "__main__":
    print(solution(51712))
