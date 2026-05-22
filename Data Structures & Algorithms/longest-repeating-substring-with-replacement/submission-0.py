class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        left = 0
        max_f = 0
    
        for right in range(len(s)):

        # Update frequency of current character
            count[s[right]] = count.get(s[right], 0) + 1
        # Track the highest frequency character seen so far in the window
            max_f = max(max_f, count[s[right]])
        
        # If window size - max frequency > k, slide the window
            if (right - left + 1) - max_f > k:
                count[s[left]] -= 1
                left += 1
            
            res = max(res, right - left + 1)
        
        return res