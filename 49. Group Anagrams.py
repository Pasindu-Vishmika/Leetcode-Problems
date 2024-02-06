from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        
        for s in strs:
            signature = ''.join(sorted(s))
            if signature in groups:
                groups[signature].append(s)
            else:
                groups[signature] = [s]
        
        return list(groups.values())