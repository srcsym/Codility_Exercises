def solution(A):
    min=10
    index=""
    for i in range(0,len(A)-1):
        for j in range(i+1,len(A)):
            avarage=A[i:(j+1)]/int(j-i+1)

        if avarage<min:
            min=avarage
            index=i
    return index