# Python Exercise Lab
# Chris Fields


def hello_world():
    print("Hello World")


def fixed_rectangle_area():
    length = 40
    width = 20
    area = length * width
    print("The area of the rectangle is:", area, "square inches")


def rectangle_area():
    length = float(input("Enter the rectangle's length: "))
    width = float(input("Enter the rectangle's width: "))

    if length <= 0 or width <= 0:
        print("Length and width must be greater than zero.")
        return

    area = length * width
    print("The area of the rectangle is:", area)


def even_or_odd():
    number = int(input("Enter an integer: "))

    if number % 2 == 0:
        print(number, "is even")
    else:
        print(number, "is odd")


def maximum_of_three():
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))
    number3 = float(input("Enter the third number: "))

    max_value = max(number1, number2, number3)
    print("The maximum number is:", max_value)


def minimum_of_three():
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))
    number3 = float(input("Enter the third number: "))

    min_value = min(number1, number2, number3)
    print("The minimum number is:", min_value)


def factorial_calculator():
    number = int(input("Enter a nonnegative integer: "))

    if number < 0:
        print("Factorial requires a nonnegative integer.")
        return

    factorial = 1

    for i in range(1, number + 1):
        factorial *= i

    print("The factorial of", number, "is:", factorial)


def reverse_string():
    text = input("Enter a string: ")
    reversed_text = text[::-1]

    print("Reversed string:", reversed_text)


def fibonacci_sequence():
    terms = int(input("Enter the number of Fibonacci terms: "))

    if terms <= 0:
        print("Enter a number greater than zero.")
        return

    a, b = 0, 1

    print("Fibonacci sequence:")

    for _ in range(terms):
        print(a, end=" ")
        a, b = b, a + b

    print()


def main():
    exercises = {
        "1": hello_world,
        "2": fixed_rectangle_area,
        "3": rectangle_area,
        "4": even_or_odd,
        "5": maximum_of_three,
        "6": minimum_of_three,
        "7": factorial_calculator,
        "8": reverse_string,
        "9": fibonacci_sequence,
    }

    while True:
        print("\nPython Exercise Lab")
        print("1. Hello World")
        print("2. Rectangle area with fixed values")
        print("3. Rectangle area with user input")
        print("4. Even or odd")
        print("5. Maximum of three numbers")
        print("6. Minimum of three numbers")
        print("7. Factorial calculator")
        print("8. Reverse a string")
        print("9. Fibonacci sequence")
        print("0. Exit")

        choice = input("Choose an exercise: ").strip()

        if choice == "0":
            print("Goodbye!")
            break

        exercise = exercises.get(choice)

        if exercise is None:
            print("Please choose a number from 0 through 9.")
            continue

        try:
            exercise()
        except ValueError:
            print("Invalid number. Choose the exercise again and enter a numeric value.")


if __name__ == "__main__":
    main()