def find_min_max(arr, left, right):
    if left == right:
        return arr[left], arr[left]

    if right == left + 1:
        if arr[left] < arr[right]:
            return arr[left], arr[right]
        else:
            return arr[right], arr[left]

    # Середина
    mid = (left + right) // 2

    # Рекурсивний пошук для лівої та правої частини
    left_min, left_max = find_min_max(arr, left, mid)
    right_min, right_max = find_min_max(arr, mid + 1, right)

    # Об’єднання результатів
    overall_min = min(left_min, right_min)
    overall_max = max(left_max, right_max)

    return overall_min, overall_max

numbers = [3, 5, 1, 8, 2, 9, -4, 7]

minimum, maximum = find_min_max(numbers, 0, len(numbers) - 1)

print("Мінімум:", minimum)
print("Максимум:", maximum)
