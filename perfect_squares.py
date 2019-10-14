def num_squares(n):
    num = n
    for item in range(n):
        square = item * item
        if square < n:
            num = min(num, num_squares(n - square))
        else:
            break
    print(num)


num_squares(12)
