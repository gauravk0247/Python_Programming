# Q.2 Write a class calculator capable of finding square, cube, squareroot of a number.
class calculator:
    def __init__(self, num):
        self.number = num

    def square(self):
        print(f"The value of {self.number} square is {self.number **2}")

    def squareroot(self):
        print(f"The value of {self.number} square root is {self.number **0.5}")

    def cube(self):
        print(f"The value of {self.number} cube is {self.number **3}")

a = calculator(int(input("Enter a Number: ")))
a.square()
a.squareroot()
a.cube()