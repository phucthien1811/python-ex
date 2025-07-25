def has_pair_with_sum(arr, k):
    left, right = 0, len(arr)-1
    while left < right:
        s = arr[left] + arr[right]
        if s == k:
            return True
        elif s < k:
            left += 1
        else:
            right -= 1
    return False

print(has_pair_with_sum([1, 2, 3, 9], 8))  # False
print(has_pair_with_sum([1, 2, 4, 4], 8))  # True
