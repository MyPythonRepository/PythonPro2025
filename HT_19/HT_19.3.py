def max_lake_depth(heights):
    n = len(heights)
    if n < 3:
        return 0

    left = 0
    right = n - 1
    left_max = heights[left]
    right_max = heights[right]
    max_depth = 0

    while left < right:
        if heights[left] < heights[right]:
            left += 1
            left_max = max(left_max, heights[left])
            max_depth = max(max_depth, left_max - heights[left])
        else:
            right -= 1
            right_max = max(right_max, heights[right])
            max_depth = max(max_depth, right_max - heights[right])

    return max_depth


heights = [1, 2, 5, 6, 1, 2, 2, 3, 0, 1, 5, 6, 7, 5, 5, 7, 8, 8, 2]
print(max_lake_depth(heights))
