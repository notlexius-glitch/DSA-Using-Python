class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        ones = [
            "", "One", "Two", "Three", "Four",
            "Five", "Six", "Seven", "Eight", "Nine",
            "Ten", "Eleven", "Twelve", "Thirteen",
            "Fourteen", "Fifteen", "Sixteen",
            "Seventeen", "Eighteen", "Nineteen"
        ]

        tens = [
            "", "", "Twenty", "Thirty", "Forty",
            "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"
        ]

        def convert(n):
            if n < 20:
                return ones[n]

            if n < 100:
                return tens[n // 10] + (
                    " " + ones[n % 10] if n % 10 else ""
                )

            return (
                ones[n // 100] + " Hundred" +
                (" " + convert(n % 100) if n % 100 else "")
            )

        result = []

        billions = num // 1_000_000_000
        millions = (num // 1_000_000) % 1000
        thousands = (num // 1000) % 1000
        remainder = num % 1000

        if billions:
            result.append(convert(billions) + " Billion")

        if millions:
            result.append(convert(millions) + " Million")

        if thousands:
            result.append(convert(thousands) + " Thousand")

        if remainder:
            result.append(convert(remainder))

        return " ".join(result)
        #praval