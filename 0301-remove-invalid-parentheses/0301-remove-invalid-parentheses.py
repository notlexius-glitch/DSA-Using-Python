class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def is_valid(s):
            count = 0

            for ch in s:
                if ch == '(':
                    count += 1
                elif ch == ')':
                    count -= 1

                    if count < 0:
                        return False

            return count == 0

        result = []
        queue = {s}
        found = False

        while queue:
            valid = []

            for current in queue:
                if is_valid(current):
                    valid.append(current)

            if valid:
                return valid

            next_level = set()

            for current in queue:
                for i in range(len(current)):
                    if current[i] in "()":
                        next_level.add(current[:i] + current[i + 1:])

            queue = next_level

        return []