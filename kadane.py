def max_subarray(arr):
    max_sum = cur_sum = arr[0]
    for x in arr[1:]:
        cur_sum = max(x, cur_sum + x)
        max_sum = max(max_sum, cur_sum)
    return max_sum

print(max_subarray([-2,1,-3,4,-1,2,1,-5,4]))  # Output: 6 (subarray [4, -1, 2, 1])
