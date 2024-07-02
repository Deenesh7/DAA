def dynamic_pricing(T, P, I, E, C):
    n = len(P)
    dp = [[0 for _ in range(n)] for _ in range(T)]
    ps = [[0 for _ in range(n)] for _ in range(T)]

    for t in range(T):
        for i in range(n):
            mp = float('-inf')
            op = 0

            for price in range(C[i] - 10, C[i] + 11):
                if I[i] <= 0:
                    break 

                demand = max(E[i] * (price - C[i]), 0)
                profit = price * demand

                if t > 0:
                    profit += dp[t-1][i]

                if profit > mp:
                    mp = profit
                    op = price

            dp[t][i] = mp
            ps[t][i] = op
            I[i] -= max(E[i] * (op - C[i]), 0)

    return ps, dp[T-1]
T = 4
P = ['P1', 'P2','P3','P4']
I = [100, 100,150,200]
E = [1.2, 1.1,0.8,0.9]
C = [50, 60,70,80]
opt, finprofit = dynamic_pricing(T, P, I, E, C)
print("Optimal Prices (Dynamic): ", opt)
print("Final Profits (Dynamic): ", finprofit)
