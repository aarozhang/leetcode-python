class Solution:

    # O(n) time, space
    def addStrings(self, num1: str, num2: str) -> str:
        res = []
        carry = 0

        p1 = len(num1) - 1
        p2 = len(num2) - 1

        while p1 >= 0 or p2 >= 0:
            n1, n2 = 0, 0

            # if p1 or p2 is not at end of number, store its value
            if (p1 >= 0):
                n1 = ord(num1[p1]) - ord('0')

            if (p2 >= 0):
                n2 = ord(num2[p2]) - ord('0')

            i = max(p1, p2)

            sum = n1 + n2 + carry
            val = sum % 10  # this is ones digit
            carry = sum // 10  # floor will provide either 0 or 1

            res.append(val)

            p1 -= 1
            p2 -= 1

        # edge case. add final carry if exists
        if carry:
            res.append(carry)

        return ''.join(str(x) for x in res[::-1])


sol = Solution()
print(sol.addStrings("11", "123"))