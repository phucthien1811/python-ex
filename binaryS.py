def binary_search(arr, x):
    left, right = 0, len(arr)-1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return mid  # Tìm thấy
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1  # Không tìm thấy

arr = [1, 3, 5, 7, 9, 11]
print(binary_search(arr, 7))  # Kết quả: 3
