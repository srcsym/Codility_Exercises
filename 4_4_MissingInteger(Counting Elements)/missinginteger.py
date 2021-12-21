def solution(A):
    new_list=sorted(list(set(A)))
    s=0

    if new_list[0]==0:
            new_list.remove(0)
    if new_list==[]:
        return 1


    for i in range(1,len(new_list)+1):
            if i!=new_list[i-1]:
                 return i
            else:
                 continue
    return new_list[-1]+1

#print(solution([0,1,3,6,4,1,2]))
#print(solution([0]))
print(solution([6]))
#print(solution([1,2,3]))
# #print(solution([1,2,3,8]))
# print(solution([-1,-3]))