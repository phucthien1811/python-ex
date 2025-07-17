def max_average(nums, k):
    s = sum(nums[:k])
    max_avg = s / k
    for i in range(k, len(nums)):
        s += nums[i] - nums[i-k]
        max_avg = max(max_avg, s / k)
    return max_avg

print(max_average([1,12,-5,-6,50,3], 4))  # Output: 12.75
