

def findRightInterval(intervals):

    result = [-1] * len(intervals)

    indexed_intervals = [(start,end,i) for i, (start,end) in enumerate(intervals)]

    indexed_intervals.sort(key=lambda x: x[0])

    for start, end, original_index in indexed_intervals:
        low,high = 0, len(indexed_intervals)

        while low < high:
            mid = (low + high) // 2
            if indexed_intervals[mid][0] >= end:
                high = mid
            else:
                low = mid + 1
        if low < len(indexed_intervals):
            result[original_index] = indexed_intervals[low][2]
        return result

# Example input: list of intervals
intervals = [[1, 2], [2, 3], [0, 1]]

# Call the findRightInterval function and store the result
result = findRightInterval(intervals)

# Print the indices of the right intervals
print(result)