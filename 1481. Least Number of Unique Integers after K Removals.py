class Solution:
    def findLeastNumOfUniqueInts(self, arr, k):
        counter = {}
        for num in arr:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1
        
        values = list(counter.values())
        values.sort()
        
        cnt = 0
        for i in range(len(values)):
            if k > values[i]:
                k -= values[i]
                values[i] = 0
            else:
                values[i] -= k
                k = 0
            
            if values[i] != 0:
                cnt += 1
        
        return cnt
