class Solution:
    def frequencySort(self, s: str) -> str:
        # Counter - dict with character (key) and frequency (value)
        
        # most_common() sort by frequency in descending order
        counter = Counter(s).most_common()
        
        # String multiplication
        answers = [k*v for k, v in counter]
        
        return "".join(answers)
