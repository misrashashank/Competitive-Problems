# def ugly_number(n, a, b, c):
#     count = 1
#     for i in range(1, n**2):
#         if (i % a == 0) or (i % b == 0) or (i % c == 0):
#             if count == n:
#                 return i
#             count += 1


def ugly_number(n, a, b, c):
    possible = []
    l = [a, b, c]
    l.sort()
    for i in range(1, n+1):
        possible.append(l[0] * i)
    last_element = possible[-1]
    for i in range(1, n+1):
        if (i*l[1]) < last_element:
            possible.append(i*l[1])
        else:
            break
    for i in range(1, n+1):
        if (i*l[2]) < last_element:
            possible.append(i*l[2])
        else:
            break
    return(list(set(possible))[n-1])


n = 5
a = 2
b = 11
c = 13
result = ugly_number(n, a, b, c)
print(result)