class RomanNum:
    def __init__(self, num):
        self.num = num
        self.val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]
        self.syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]

    def int_to_roman(self):
        roman_num = ''
        i = 0
        num = self.num  # Avoid modifying the original number
        while num > 0:
            for _ in range(num // self.val[i]):
                roman_num += self.syb[i]
                num -= self.val[i]
            i += 1
        return roman_num

    def __str__(self):
        return self.int_to_roman()


# Now when you print the object, it will show the Roman numeral
# print(RomanNum(15))  # Output will be "I"
