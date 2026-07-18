class Solution(object):
    def isMatch(self, s, p):
        i, j = 0, 0
        star, match = -1, 0
        while i < len(s):
            if j < len(p) and (p[j] == '?' or s[i] == p[j]):
                i += 1
                j += 1
            elif j < len(p) and p[j] == '*':
                star = j
                match = i
                j += 1
            elif star != -1:
                j = star + 1
                i = match + 1
                match += 1
            else:
                return False

        while j < len(p) and p[j] == '*':
            j += 1
        
        return j == len(p)
            
s = "aa"
p = "a"
sol = Solution()
result = sol.isMatch(s, p)
print(result)