def range_sum(arr, l, r):
    prefix = [0]*(len(arr)+1)
    for i in range(len(arr)):
        prefix[i+1] = prefix[i] + arr[i]
    return prefix[r+1] - prefix[l]

arr = [1, 2, 3, 4, 5]
print(range_sum(arr, 1, 3))  # Output: 2+3+4 = 9
