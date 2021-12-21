def solution(A):
    controlList=list(range(1,len(A)+1))
    print(controlList)
    if controlList==sorted(A):
        return 1
    else:
        return 0

print(solution([4,1,3,2]))
