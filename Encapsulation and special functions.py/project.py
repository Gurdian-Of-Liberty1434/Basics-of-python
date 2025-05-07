class reverse:
    def __init__(self):
        self.text = input("Enter a word: ")

    def reverse(self):
        reversed_text = ""
        for char in self.text:
            reversed_text = char + reversed_text
        return reversed_text

    def print_result(self):
        print("The original string is", self.text)
        print("The reverse string is", self.reverse())
        
reverser = reverse()
reverser.print_result()