class RomanNumeral:
    def __init__(self, value):
        self.value = value

    def to_roman(self):
        roman_numerals = {1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC", 50: "L", 40: "XL", 10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"}
        result = ""
        for numeral, symbol in roman_numerals.items():
            while self.value >= numeral:
                result += symbol
                self.value -= numeral
        return result

    def __str__(self):
        return self.to_roman()

value = int(input("Enter an integer: "))
roman_numeral = RomanNumeral(value)
print(roman_numeral)
