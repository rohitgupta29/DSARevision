from typing import List
from collections import Counter
from heapq import heappush, heappop

def topKFrequent(nums: List[int], k: int) -> List[int]:

    num_freq = Counter(nums)

    min_heap = []
    for num, freq in num_freq.items():
        heappush(min_heap, (freq,num))
        print(min_heap)
        if len(min_heap) > k:
            heappop(min_heap)

        print("minheap pop: ", min_heap)
        top_k_frequent = [pair[1] for pair in min_heap]

    return top_k_frequent


    # freq_table = Counter(nums)
    # print(freq_table)
    # heap = []
    # for i in freq_table.keys():
    #     # print(i)
    #     heappush(heap, (-freq_table[i], i))
    # print("heap: ",heap)
    # ans = []
    # while k > 0:
    #     k -=1
    #     # print(heappop(heap)[0])
    #     a = heappop(heap)
    #     print(a)
    #     ans.append(a[1])
    # return ans



print(topKFrequent(nums= [1,1,1,2,2,3] , k=2))