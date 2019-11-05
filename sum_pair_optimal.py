import sys

class Optimal:
    def optimal_sum_pair(self, a, b, target):
        diff = sys.maxsize
        output = []
        for first in a:
            if first[1] < target:
                for second in b:
                    if second[1] < target:
                        middle_sum = first[1] + second[1]
                        if middle_sum < target + 1 and target - middle_sum < diff:
                            diff = abs(target - middle_sum)
                            output.clear()
                            output.append([first[0], second[0]])
                        elif middle_sum < target + 1 and target - middle_sum == diff:
                            output.append([first[0], second[0]])
                        else:
                            pass
        return output


if __name__ == "__main__":
    a = [[1, 3], [2, 5], [3, 7], [4, 10]]
    b = [[1, 2], [2, 3], [3, 4], [4, 5]]
    target = 10
    # a = [[1, 8], [2, 7], [3, 14]]
    # b = [[1, 5], [2, 10], [3, 14]]
    # target = 20
    # a = [[1, 8], [2, 15], [3, 9]]
    # b = [[1, 8], [2, 11], [3, 12]]
    # target = 20
    obj = Optimal()
    output = obj.optimal_sum_pair(a, b, target)
    print(output)