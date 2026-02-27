def find_max_consecutive_ones(nums: list[int]) -> int:
    max_count = 0
    current = 0
    for v in nums:
        if v == 1:
            current += 1
            if current > max_count:
                max_count = current
        else:
            current = 0
    return max_count


# Prueba
nums = [1, 1, 0, 1, 1, 1]
print(find_max_consecutive_ones(nums))  # 3
