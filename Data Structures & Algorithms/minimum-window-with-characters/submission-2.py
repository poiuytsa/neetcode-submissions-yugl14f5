class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        tFreq = [0] * 128
        window = [0] * 128

        for c in t:
            tFreq[ord(c)] += 1

        have = 0
        need = len(t)

        l = 0
        res = ""
        minLen = float('inf')

        for r in range(len(s)):
            c = s[r]
            window[ord(c)] += 1

            if window[ord(c)] <= tFreq[ord(c)]:
                have += 1

            while have == need:
                if (r - l + 1) < minLen:
                    minLen = r - l + 1
                    res = s[l:r+1]

                window[ord(s[l])] -= 1

                if window[ord(s[l])] < tFreq[ord(s[l])]:
                    have -= 1

                l += 1

        return res