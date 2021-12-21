def solution(A, B, K):
    s=0
    for i in range(A,B+1):
        if i%K==0:
            s+=1
    return s