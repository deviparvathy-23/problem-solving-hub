def dynamicArray(n, queries):
    arr=[]
    for i in range(n):
        arr.append([])
    lastAnswer=0
    a=[]
    for i in queries:
            if i[0]==1:
                idx=(i[1]^lastAnswer)%n
                arr[idx].append(i[2])
            elif i[0]==2:
                idx=(i[1]^lastAnswer)%n
                lastAnswer=arr[idx][i[2]%len(arr[idx])]
                a.append(lastAnswer)
    return a
