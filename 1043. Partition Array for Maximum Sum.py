
class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        newarr = [0] * n 
        
        for i in range(n):
            current_max = arr[i]
            for j in range(1, min(k, i + 1) + 1):
                current_max = max(current_max, arr[i - j + 1])
                previous_sum = 0 if i - j < 0 else newarr[i - j]
                newarr[i] = max(newarr[i], previous_sum + current_max * j)

        return newarr[-1]
