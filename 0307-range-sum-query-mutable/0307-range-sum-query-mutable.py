class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.nums = nums[:]
        self.tree = [0] * (self.n + 1)

        for i in range(self.n):
            self._add(i + 1, nums[i])

    def _add(self, index: int, value: int) -> None:
        while index <= self.n:
            self.tree[index] += value
            index += index & -index

    def _sum(self, index: int) -> int:
        total = 0

        while index > 0:
            total += self.tree[index]
            index -= index & -index

        return total

    def update(self, index: int, val: int) -> None:
        diff = val - self.nums[index]
        self.nums[index] = val

        self._add(index + 1, diff)

    def sumRange(self, left: int, right: int) -> int:
        return self._sum(right + 1) - self._sum(left)