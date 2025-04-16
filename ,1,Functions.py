# Well wishes:
def well_wishes():
    print("Hello")
    print("How are you doing?")


well_wishes()

# Circumfrence of a circle:
r = float(input("Enter your radius: "))

# definition of function:
def circle_circumfrence(r):
    return 2*3.14*r

# Printing the value:
print(circle_circumfrence(r))


# Wether Condition:
# define wether conditon:
def wether_condition():
    print("Wether is pleasent in", spring)
    print("Wether is the same in", autum)

# Variables:
spring = "summmer"
autum = "winter"

wether_condition()

# Calculator:

# Defining functions:
def add(p , q):
    return p + q
def sub(p , q):
    return p - q
def mul(p , q):
    return p * q
def div(p , q):
    return p / q

# Asking user their choice
print("Please select your option: ")
print("a. Add")
print("b. Subtract")
print("c. Multiply")
print("d. Division")

num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))
choice = input("Enter your choice (a, b, c, d): ").lower()


if choice == "a":
    total =  add(num1, num2)
    print(f"You're total after the calculations is {total:.2f}")
elif choice == "b":
    total = sub(num1, num2)
    print(f"You're total after the calculations is {total :.2f}")
elif choice == "c":
    total = mul(num1, num2)
    print(f"You're total after the calculations is {total :.2f}")
elif choice == "d":
    total =  div(num1, num2)
    print(f"You're total after the calculations is {total :.2f}")

else:
    print("Invalid operation!")
