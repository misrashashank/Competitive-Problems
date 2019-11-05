def minimumAbsDifference(arr):
    arr.sort()
    min_diff = 100000
    pairs = []
    for index in range(len(arr)):
        if index + 1 < len(arr):
            if abs(arr[index] - arr[index+1]) < min_diff:
                pairs.clear()
                pairs.append([arr[index], arr[index+1]])
                min_diff = abs(arr[index] - arr[index+1])
            elif abs(arr[index] - arr[index+1]) == min_diff:
                pairs.append([arr[index], arr[index+1]])
            else:
                pass
    return pairs

pairs = minimumAbsDifference([1,2])
print(pairs)