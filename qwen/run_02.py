# Incorrect: only considers adjacent pairs

def solve():
    import math

    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    ans = float('inf')

    for i in range(n - 1):
        cost1 = (k - a[i] % k) % k
        cost2 = (k - a[i+1] % k) % k
        ans = min(ans, cost1 + cost2)

    print(ans)

if __name__ == "__main__":
    solve()
