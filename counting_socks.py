# Given an array of integers representing the color of each sock, determine
# how many pairs of socks with matching colors there are.
# Function must return an integer representing the number of matching pairs
# of socks that are available.


def sock_merchant(num, op_array):
    pairs = {}
    count = 0
    for item in op_array:
        if item in pairs:
            pairs[item] += 1
        else:
            pairs[item] = 1
    for item in pairs.items():
        count = count + int(item[1]/2)
    print(count)


if __name__ == '__main__':
    sock_merchant(10, [1, 2, 3, 1, 3, 2, 2, 1, 2, 3])
