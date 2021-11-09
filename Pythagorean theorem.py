# Find hypotenuse using Pythagorean theorem
while True:

    class Triangle:

        def __init__(self, length, base):
            self.length = length
            self.base = base

        def hypotenuse(self):
            print(f"\nLength of right triangle is {self.length}.")
            print(f"Base of right triangle is {self.base}.")
            print(f"So Hypotenuse of right triangle is {int((self.length ** 2 + self.base ** 2) ** 0.5)}.\n")

    length = int(input("Enter length of right triangle : "))
    base = int(input("Enter base of right triangle : "))

    hypo = Triangle(length, base)
    hypo.hypotenuse()

    find_again = input("Want to find again (y / n): ")
    if find_again.lower() != "y":
        print("------ End!!! ------")
        break
