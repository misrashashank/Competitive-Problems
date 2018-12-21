# Couting Triplets
# You are given an array and you need to find number of tripets of indices
# (i, j, k) such that the elements at those indices are in
# geometric progression for a given common ratio r and i < j < k.
# The countTriplets function should return the number of triplets forming
# a geometric progression for a given r as an integer.


class Triplets:
    def count_triplets(arr, r):
        arr_dict = {}
        count = 0
        for item in arr:
            if item in arr_dict.keys():
                arr_dict[item] += 1
            else:
                arr_dict[item] = 1
        for key in arr_dict.keys():
            if key*r and key*r*r in arr_dict.keys():
                count = count + (arr_dict[key] * arr_dict[key*r] * arr_dict[key*r*r])
        print(count)


if __name__ == '__main__':
    main_obj = Triplets()
    count_triplets([1, 2, 2, 4], 2)
