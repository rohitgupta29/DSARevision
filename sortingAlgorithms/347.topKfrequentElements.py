

def topKFrequent(nums, k):

    frequency_map = {}
    for num in nums:
        if num in frequency_map:
            frequency_map[num] += 1
        else:
            frequency_map[num] = 1

    sorted_freq = sorted(frequency_map.items(), key= lambda item: item[1], reverse = True)

    top_k_elements = [item[0] for item in sorted_freq[:k]]

    return top_k_elements


nums = [1, 1, 1, 2, 2, 3]
k = 2

result = topKFrequent(nums,k)
print(result)