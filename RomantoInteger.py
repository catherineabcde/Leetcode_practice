# class Solution:
#     def romanToInt(self, s: str) -> int:
#         split_s = []
#         for e in s:
#             split_s.append(e)

#         n = len(split_s)
#         L = []
#         for i in range(n):
#             word = split_s[i]
#             match word:
#                 case 'I':
#                     L.append(1)
#                 case 'V':
#                     L.append(5)
#                 case 'X':
#                     L.append(10)
#                 case 'L':
#                     L.append(50)
#                 case 'C':
#                     L.append(100)
#                 case 'D':
#                     L.append(500)
#                 case 'M':
#                     L.append(1000)

#         S, i, a = 0, 0, 0
#         while i < n:
#             a = i + 1
#             if a < n:
#                 if L[i] < L[a]:
#                     S += L[a] - L[i]
#                     i += 2
#                 else:
#                     S += L[i]
#                     i += 1
#             else:
#                 S += L[i]
#                 i += 1
#         return S

class Solution:
    def romanToInt(self, s:str) -> int:
        roman_map = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        total = 0
        n = len(s)
        for i in range(n):
            value = roman_map[s[i]]
            if i + 1 < n and value < roman_map[s[i+1]]:
                total -= value
            else:
                total += value
        return value
