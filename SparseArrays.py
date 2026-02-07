def matchingStrings(stringList, queries):
    a=[]
    for i in queries:
        a.append(0)
    for i in range(len(queries)):
        for j in stringList:
            if queries[i]==j:
                a[i]+=1
    return a
