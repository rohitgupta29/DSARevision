def sortColors(nums):
    # Initialize pointers for the current position, the next position for 0s, and the next position for 2s
    low = 0          # Pointer for the next position of 0
    mid = 0          # Pointer for the current element being evaluated
    high = len(nums) - 1  # Pointer for the next position of 2

    # Iterate through the array until mid exceeds high
    while mid <= high:
        if nums[mid] == 0:
            # If the current element is 0, swap it with the element at low pointer
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1   # Move low pointer to the right
            mid += 1   # Move mid pointer to the right
        elif nums[mid] == 1:
            # If the current element is 1, just move mid pointer to the right
            mid += 1
        else:  # nums[mid] == 2
            # If the current element is 2, swap it with the element at high pointer
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1  # Move high pointer to the left

# Example input array with colors represented as integers (0s, 1s, and 2s)
arr = [2, 0, 2, 1, 1, 0]

# Call the sortColors function to sort the array in place
sortColors(arr)

# Print the sorted result
print(arr)