# Longest Repeating Character Replacement


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        counts = {}
        max_frequency = 0
        longest_length = 0

        for right, ch in enumerate(s):
            counts[ch] = counts.get(ch, 0) + 1
            max_frequency = max(max_frequency, counts[ch])

            while (right - left + 1) - max_frequency > k:
                counts[s[left]] -= 1
                left += 1

            longest_length = max(longest_length, right - left + 1)

        return longest_length

    def charachterReplacement(self, s: str, k: int) -> int:
        return self.characterReplacement(s, k)