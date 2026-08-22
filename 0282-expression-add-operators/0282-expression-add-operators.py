from typing import List

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        result = []

        def backtrack(index, expression, value, prev):
            # All digits used
            if index == len(num):
                if value == target:
                    result.append(expression)
                return

            for end in range(index, len(num)):
                # Don't allow numbers with leading zeros
                if end > index and num[index] == '0':
                    break

                current = num[index:end + 1]
                current_value = int(current)

                # First number
                if index == 0:
                    backtrack(
                        end + 1,
                        current,
                        current_value,
                        current_value
                    )
                else:
                    # Addition
                    backtrack(
                        end + 1,
                        expression + "+" + current,
                        value + current_value,
                        current_value
                    )

                    # Subtraction
                    backtrack(
                        end + 1,
                        expression + "-" + current,
                        value - current_value,
                        -current_value
                    )

                    # Multiplication
                    # Undo the previous operand and multiply it
                    # by the current number.
                    backtrack(
                        end + 1,
                        expression + "*" + current,
                        value - prev + prev * current_value,
                        prev * current_value
                    )

        backtrack(0, "", 0, 0)
        return result