def pas(n):
    """
    it draws the pascal triangle
    :param n: how many levels
    :return: the lists
    """
    a = []
    b = []

    #The first item of each n
    a[0] = 1

    if n > 0:
        b = pas(n-1)
        for i in range(n):
            a[i] = b[i] + b[i-1]

    return a, b

print(pas(5))
