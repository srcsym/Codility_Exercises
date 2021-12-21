def solution(A):
    counter=0
    for i in range(len(A)):
        if A[i]==0:
            for j in range(i+1,len(A)):
                if A[j]==1:
                    counter+=1
    return counter