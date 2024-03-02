class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        x=[i*i for i in nums]
        x.sort()
        return x
        