class Solution:
    def frequencySort(self, s: str) -> str:
        #Count the frequency of each character
        char_count = Counter(s)
        
        #Sort characters based on their frequency in descending order
        sorted_chars = sorted(char_count, key=char_count.get, reverse=True)
        result = ''
        for char in sorted_chars:
            result += char * char_count[char]
        return result