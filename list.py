import bisect

def lis(arr):
    sub = []
    for x in arr:
        idx = bisect.bisect_left(sub, x)
        if idx == len(sub):
            sub.append(x)
        else:
            sub[idx] = x
    return len(sub)

print(lis([10,9,2,5,3,7,101,18]))  # Output: 4
