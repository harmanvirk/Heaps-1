#TC = O(n logk) | SC = O(k)
import heapq
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        if (nums == None or len(nums) == 0):
            return -1

        topK = []

        for i in range(k):
            heapq.heappush(topK, nums[i])

        for i in range(k, len(nums)):
            smallest = topK[0]
            if (smallest < nums[i]):
                heapq.heappop(topK)
                heapq.heappush(topK, nums[i])

        return topK[0]