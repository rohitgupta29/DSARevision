


def count_subarrays_with_target_sum(arr, tar):
    # Dictionary to store the frequency of prefix sums.
    # We start by initializing it with {0: 1} because a prefix sum of 0
    # means there's one way to get a subarray starting from the beginning that equals the target.
    prefix_sum_count = {0: 1}

    # Variable to keep track of the current prefix sum as we iterate through the array.
    current_sum = 0

    # Variable to count the number of subarrays that sum to the target value.
    subarray_count = 0

    # Loop through each element in the array.
    for num in arr:
        current_sum += num  # Update the prefix sum with the current element.

        # Check if (current_sum - tar) exists in the hash map.
        # If it does, it means there is a subarray that sums to 'tar'.
        # Add the frequency of that prefix sum to the subarray count.
        if (current_sum - tar) in prefix_sum_count:
            subarray_count += prefix_sum_count[current_sum - tar]

        # Update the frequency of the current prefix sum in the hash map.
        # If the prefix sum is already in the map, increment its count.
        # Otherwise, add it to the map with a count of 1.
        if current_sum in prefix_sum_count:
            prefix_sum_count[current_sum] += 1
        else:
            prefix_sum_count[current_sum] = 1

    # Return the total count of subarrays that sum to the target.
    return subarray_count


arr = [1, 2, 3, -2, 5]
tar = 5
result = count_subarrays_with_target_sum(arr, tar)
print(result)  # Output should be 2