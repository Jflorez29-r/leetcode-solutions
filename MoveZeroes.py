def move_zeroes(nums: list[int]) -> None:
    """
    Moves all zeroes to the end of the list while maintaining the relative order
    of non-zero elements using the Two-Pointer swap technique.
    """
    slow = 0 # Pointer to track the position of the next non-zero element
    for fast in range(len(nums)):
        if nums[fast] != 0: # If the current element is non-zero, swap it with the element at the slow pointer
            nums[slow], nums[fast] = nums[fast], nums[slow] # Swap the non-zero element with the element at the slow pointer
            slow += 1 # Move the slow pointer to the next position for the next non-zero element


# Example usage:
nums = [0, 1, 0, 3, 12]
move_zeroes(nums)
print(nums)  # Output: [1, 3, 12, 0, 0]
