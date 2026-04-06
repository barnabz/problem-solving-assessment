# Incorrect: assumes only one element needs to be divisible

def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    min_cost = float('inf')

    for x in a:
        cost = (k - x % k) % k
        min_cost = min(min_cost, cost)

    print(min_cost)

if __name__ == "__main__":
    solve()
