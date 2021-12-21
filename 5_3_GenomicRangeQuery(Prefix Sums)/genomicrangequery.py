def solution(S, P, Q):
    nuc_list={'A':1,'C':2,'G':3,'T':4}

    value_list=[]
    for i in range(len(P)):
        if S[P[i]] < S[Q[i]]:
            value_list.append(nuc_list[S[P[i]]])
        else:
            value_list.append(nuc_list[S[Q[i]]])
    return value_list

print(solution('CAGCCTA',[2,5,0],[4,5,6]))
