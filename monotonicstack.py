def next_smaller_right(arr):
    res = [-1]*len(arr)
    stack = []
    for i in range(len(arr)):
        while stack and arr[stack[-1]] > arr[i]:
            res[stack.pop()] = i
        stack.append(i)
    return res

print(next_smaller_right([2, 1, 4, 3]))  # Output: [1, -1, 3, -1]
