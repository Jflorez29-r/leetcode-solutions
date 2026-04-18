def container_with_most_water(height: list[int]) -> int:
  left = 0
  right = len(height) - 1
  max_area = 0 # Initialize max_area to 0

  while left < right:
    # Area = height * width. Width is the distance between X-coordinates (indices)
    current_area = min(height[left], height[right]) * (right - left)
    max_area = max(max_area, current_area) # Update max_area if the current area is greater

    if height[left] < height[right]:  # Move the pointer with the smaller height
      left += 1 # Move the left pointer to the right
    else:
      right -= 1 # Move the right pointer to the left

  return max_area


if __name__ == "__main__":
  print(container_with_most_water([1, 8, 6, 2, 5, 4, 8, 3, 7]))
