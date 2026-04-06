# Incorrect: brute force GCD logic (inefficient and wrong approach)

import math

def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    ans = float('inf')

    for i in range(n):
        for j in range(i+1, n):
            g = math.gcd(a[i], a[j])
            if g % k == 0:
                ans = 0
            else:
                cost1 = (k - a[i] % k) % k
                cost2 = (k - a[j] % k) % k
                ans = min(ans, cost1 + cost2)

    print(ans)

if __name__ == "__main__":
    solve()
