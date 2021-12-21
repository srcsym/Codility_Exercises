def solution(X, A):

    list_new=[]
    for item in A:
        if item not in list_new:
            list_new.append(item)
    
    if len(list_new)==X:
        index_last=A.index(list_new[-1])
        return index_last
    else:
        return -1

print(solution(5,[1,3,1,4,2,3,5,4]))