import random

def generate():
    n = random.randint(2, 10)
    k = random.randint(1, 10)
    arr = [random.randint(1, 20) for _ in range(n)]

    print(n, k)
    print(*arr)

if __name__ == "__main__":
    generate()
