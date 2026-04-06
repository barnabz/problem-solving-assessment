def solve():
    import sys
    input = sys.stdin.readline

    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    costs = []
    for x in a:
        costs.append((k - x % k) % k)

    costs.sort()
    print(costs[0] + costs[1])


if __name__ == "__main__":
    solve()
