class Solution(object):
    def multiply(self, num1, num2):
        total = 0
        num1 = num1[::-1]
        num2 = num2[::-1]

        for i in range(len(num1)):
            temp_num1 = int(num1[i])
            for j in range(len(num2)):
                temp_num2 = int(num2[j])
                total += temp_num1 * temp_num2 * 10 ** (i+j)
        return str(total)

num1 = "123"
num2 = "456"
sol = Solution()
result = sol.multiply(num1, num2)
print(result)