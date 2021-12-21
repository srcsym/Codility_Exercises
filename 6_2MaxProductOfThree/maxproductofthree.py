def solution(A):
    max=0
    for i in range(0,len(A)-2):
        multi=A[i]*A[i+1]*A[i+2]
        print(multi)
        if multi>max:
            max=multi
    return max

print(solution([-3,1,2,-2,5,6]))
