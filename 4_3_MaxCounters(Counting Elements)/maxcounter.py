def solution(N, A):
    firstList = [0] * N

    if len(A) == 1:
        if A[0]==int(N) +1:
            return firstList
        else:
            firstList[A[0] - 1] += 1
            return firstList

    for i in range(0, len(A)):

        if A[i] == max(A):

            firstList = [max(firstList)] * N

        else:

            firstList[A[i] - 1] += 1

    return firstList


print(solution(5,[3,4,4,6,1,4,4]))