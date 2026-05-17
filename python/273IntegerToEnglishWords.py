class Solution:
    ZERO = "Zero"
    ONES = [
        "", "One", "Two", "Three", "Four", "Five",
        "Six", "Seven", "Eight", "Nine"
    ]

    TEENS = [
        "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen",
        "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"
    ]

    TENS = [
        "", "", "Twenty", "Thirty", "Forty",
        "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"
    ]

    Hundred = "Hundred"

    THOUSANDS = [
        "", "Thousand", "Million", "Billion", "Trillion",
        "Quadrillion", "Quintillion", "Sextillion",
        "Septillion", "Octillion", "Nonillion", "Decillion"
    ]

    def numberToWords(self, num: int) -> str:
        if num == 0:
            return self.ZERO

        res = []
        for i, chunk in enumerate(self.splitByThousands(num)):
            if chunk:
                chunk_words = []
                chunk_words.append(self.threeDigitsToWords(chunk))

                if i > 0:
                    chunk_words.append(self.THOUSANDS[i])
                
                res.append(" ".join(chunk_words))

        return " ".join(reversed(res))

    def splitByThousands(self, num: int):
        chunks = []
        while num > 0:
            num, rem = divmod(num, 1000)
            chunks.append(rem)
        return chunks

    def threeDigitsToWords(self, n: int) -> str:
        words = []
        hundreds, rem = divmod(n, 100)
        if hundreds:
            words.append(self.ONES[hundreds])
            words.append(self.Hundred)
        
        if rem:
            if rem < 10:
                words.append(self.ONES[rem])
            elif rem < 20:
                words.append(self.TEENS[rem - 10])
            else:
                tens, ones = divmod(rem, 10)
                words.append(self.TENS[tens])
                if ones:
                    words.append(self.ONES[ones])
        return " ".join(words)
