This project recreates the Python exercises demonstrated in the recorded class lab. A menu lets users run each exercise individually.
Environment
- Python 3
- Visual Studio Code with the Microsoft Python extension
- No additional Python packages are required.
Exercises
Menu option	Exercise	Description
1	Hello World	Prints a greeting.
2	Fixed rectangle area	Calculates the area using length 40 and width 20.
3	Interactive rectangle area	Calculates area from entered dimensions.
4	Even or odd	Checks whether an integer is even or odd.
5	Maximum of three numbers	Finds the largest entered number.
6	Minimum of three numbers	Finds the smallest entered number.
7	Factorial calculator	Calculates the factorial of a nonnegative integer.
8	Reverse a string	Displays entered text backward.
9	Fibonacci sequence	Displays the requested number of terms, starting with 0 and 1.
0	Exit	Closes the program.


How to Run
Open a terminal in the project folder and run:
python3 main.py
Enter a menu option and follow the prompts. After an exercise finishes, the menu appears again. Enter 0 to exit.
Reverse String Solution
The assignment asks students to solve the reverse-string issue from the recording. This implementation uses Python string slicing:
text = input("Enter a string: ")
reversed_text = text[::-1]
print("Reversed string:", reversed_text)
The slice [::-1] steps backward through the text and creates a reversed string. The original text remains unchanged. No conditional statement is needed.

Example:
Enter a string: Steelers
Reversed string: sreleetS
The transcript alone does not establish the exact cause of the instructor's error. This solution uses valid Python 3 syntax to perform the required reversal.
Calculation and Input Handling
- input() returns text. Numeric exercises convert that text using int() or float() before calculating.
- The even-or-odd checker uses number % 2 == 0 to identify even numbers.
- The factorial calculator starts at 1 and multiplies by each integer through the entered number. This also returns 1 for zero factorial.
- The Fibonacci exercise starts with a, b = 0, 1 and updates the values using a, b = b, a + b.
- Invalid numeric input is caught so the user can choose an exercise again.
Manual Verification Examples
These are expected results to use when checking the program.
Exercise	Input	Expected result
Hello World	None	Hello World
Fixed rectangle	None	800 square inches
Interactive rectangle	30, 34	1020.0
Even or odd	4	Even
Even or odd	3	Odd
Maximum	4, 1, 100	100.0
Minimum	4, 1, 100	1.0
Factorial	5	120
Factorial	0	1
Reverse string	Steelers	sreleetS
Fibonacci	7	0 1 1 2 3 5 8
