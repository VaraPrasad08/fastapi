def restoreGem(r, c):
    dp = []
    for i in range(0, len(r)):
        dp.append([])
        for j in range(0, len(c)):

            m = min(r[i], c[j])
            dp[i].append(m)

            r[i] -= m
            c[j] -= m
 
    return dp
 
def printMatrix(ans, N, M):

    for i in range(0, len(ans)):
        for j in range(0, len(ans[i])):
            print(ans[i][j], end=" ")
 
        print("\n")

rowSum = [5, 7, 10]
colSum = [8, 6, 8]
 
ans = restoreGem(rowSum, colSum)
 
printMatrix(ans, len(rowSum),
            len(colSum))