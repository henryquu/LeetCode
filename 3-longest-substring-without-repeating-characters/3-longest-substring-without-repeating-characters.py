class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        longest = 0

        slow = 0

        for ind, char in enumerate(s):
            if char not in seen or seen[char] < slow:
                longest = max(longest, ind - slow + 1)
            else:
                slow = seen[char] + 1
            seen[char] = ind

        return longest