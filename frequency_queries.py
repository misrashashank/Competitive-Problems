# Frequency Queries
# You are given q queries. Each query is of the form two integers described below:
# -1 x : Insert x in your data structure.
# -2 y : Delete one occurence of y from your data structure, if present.
# -3 z : Check if any integer is present whose frequency is exactly z.
# If yes, print 1 else 0.

# The queries are given in the form of a 2-D array queries of size q where
# queries[i][0] contains the operation, and queries[i][1] contains the data element.


class Frequency:
    def frequency_query(queries):
        num_dict = {}
        output_arr = []
        for item in queries:
            print(num_dict)
            if item[0] == 1:
                if item[1] in num_dict.keys():
                    num_dict[item[1]] += 1
                else:
                    num_dict[item[1]] = 1
            elif item[0] == 2:
                if item[0] in num_dict.keys():
                    num_dict[item[1]] -= 1
            else:
                if item[1] in num_dict.values():
                    output_arr.append(1)
                else:
                    output_arr.append(0)
        return output_arr


if __name__ == '__main__':
    main_obj = Frequency()
    frequency_query([(1, 1), (2, 3), (3, 2), (1, 2), (1, 1), (1, 1), (2, 1), (3, 2)])
