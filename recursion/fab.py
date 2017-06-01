def fab(n):
    """
    Return pair of Fabonacci numbers , F(n) and F(n-1)
    """
    if n <= 1:
        return (n, 0)
    else:
        (a, b) = fab(n-1)
        return (a + b, a)


if __name__ == '__main__':
    n = int(input())
    print(fab(n))
