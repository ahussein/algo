def power_(x, n):
    if n == 0:
        return 1
    if n == 1:
        return x
    partial = power_(n, x // 2)
    result = partial * partial
    if n % 2 == 1:
        return result * x
    else:
        return result


if __name__ == "__main__":
    x, n = [int(item) for item in input().strip().split(' ')]
    print(power_(x, n))
