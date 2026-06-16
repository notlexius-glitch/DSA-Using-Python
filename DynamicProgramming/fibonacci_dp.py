n = 10

dp = [0, 1]

for i in range(2, n):
    dp.append(dp[i-1] + dp[i-2])

print(dp)