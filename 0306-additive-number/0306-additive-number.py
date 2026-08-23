class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)

        def add(a, b):
            i = len(a) - 1
            j = len(b) - 1
            carry = 0
            result = []

            while i >= 0 or j >= 0 or carry:
                x = int(a[i]) if i >= 0 else 0
                y = int(b[j]) if j >= 0 else 0

                total = x + y + carry
                result.append(str(total % 10))
                carry = total // 10

                i -= 1
                j -= 1

            return ''.join(reversed(result))

        def check(a, b, k, count):
            while k < n:
                c = add(a, b)

                if not num.startswith(c, k):
                    return False

                k += len(c)
                a, b = b, c
                count += 1

            return count >= 3

        for i in range(1, n):
            # Leading zero in first number
            if num[0] == '0' and i > 1:
                break

            a = num[:i]

            for j in range(i + 1, n):
                # Leading zero in second number
                if num[i] == '0' and j - i > 1:
                    break

                b = num[i:j]

                if check(a, b, j, 2):
                    return True

        return False