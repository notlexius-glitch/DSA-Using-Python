class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        ugly = [1] * n
        pointers = [0] * len(primes)

        for i in range(1, n):
            # Find the smallest next candidate
            next_num = min(
                primes[j] * ugly[pointers[j]]
                for j in range(len(primes))
            )

            ugly[i] = next_num

            # Move every pointer that produced next_num
            for j in range(len(primes)):
                if primes[j] * ugly[pointers[j]] == next_num:
                    pointers[j] += 1

        return ugly[n - 1]