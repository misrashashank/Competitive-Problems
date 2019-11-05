# Checking Paranthesis correctness using Stack Data Structure
# implemented using List Data Structure


class CheckBalancedParanthesis:
    def __init__(self):
        self.op_array = []

    def push(self, item):
        self.op_array.append(item)

    def pop(self):
        self.op_array.pop()

    def is_empty(self):
        return self.op_array == []

    def checker(self, seq):
        obj = CheckBalancedParanthesis()
        result = True
        for item in seq:
            if item == '(':
                obj.push(item)
            elif item == ')':
                if not obj.is_empty():
                    obj.pop()
                else:
                    result = False
                    break
        if not obj.is_empty():
            result = False
        return result


if __name__ == '__main__':
    main_obj = CheckBalancedParanthesis()
    # print(main_obj.checker('(()()(()'))
