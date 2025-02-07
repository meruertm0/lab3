class my_string:
    def __init__(self):
        self.string = ""

    def getString(self):
        self.string = input("Enter a string: ")

    def printString(self):
        print(self.string.upper())
p1 = my_string()
p1.getString()
p1.printString()
