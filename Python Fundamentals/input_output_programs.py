# Absolutely. Since you're revising **Python basics**, here are practice problems focused specifically on **Input and Output**—starting from very easy and gradually increasing difficulty.
#
# ## 🟢 Level 1 — Basic Input & Output
#
# 1. **Print Your Introduction**
#    Take your name, age, and city as input and print them in a meaningful sentence.
#    **Example:**
#    Input: `Rahul`, `21`, `Pune`
#    Output: `My name is Rahul. I am 21 years old and I live in Pune.`
name = input("Enter your name")
age = input("Enter your age")
city = input("Enter your city")

print(f"My name is {name}. I am {age} years old and I live in {city}.")
# 2. **Add Two Numbers**
#    Take two integers as input and print their sum.
num1 = int(input("Enter first number"))
num2 = int(input("Enter second number"))

sum = num1 + num2
print(f"Sum of {num1} and {num2} is {sum}")
# 3. **Basic Calculator**
#    Take two numbers and print their:
#
#    * Addition
#    * Subtraction
#    * Multiplication
#    * Division
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

addition = n1 + n2
print(addition)

subtraction = n1 - n2
print(subtraction)
# 4. **Square of a Number**
#    Take a number as input and print its square.
number1 = int(input("Enter any number: "))
print(f"Square is : {number1 * number1}")
# 5. **Cube of a Number**
#    Take a number as input and print its cube.
number1 = int(input("Enter any number: "))
print(f"Square is : {number1 ** 3}")
# 6. **Greeting Program**
#    Take the user's name as input and print:
#    `Hello, <name>! Welcome to Python.`
name = input("Enter your name")
print(f"Hello, {name}! Welcome to Python.")
# 7. **Age Next Year**
#    Take the user's current age and print their age next year.
age = int(input("Enter your age"))

next_year_age = age + 1
print(f"Next Year age: {next_year_age}")
# 8. **Full Name**
#    Take first name and last name separately and print the full name.
first_name = input("Enter your first name : ")
last_name = input("Enter you last name: ")

full_name = first_name +''+ last_name
print(full_name)
# ## 🟡 Level 2 — Numbers & Calculations
#
# 9. **Area of Rectangle**
#    Take length and breadth as input and calculate the area.
#
# 10. **Perimeter of Rectangle**
#     Take length and breadth and calculate the perimeter.
#
# 11. **Area of Circle**
#     Take radius as input and calculate the area of a circle.
#     Use `π = 3.14`.
#
# 12. **Temperature Conversion**
#     Take temperature in Celsius and convert it to Fahrenheit.
#     Formula:
#     `F = (C × 9/5) + 32`
#
# 13. **Minutes to Seconds**
#     Take minutes as input and convert them into seconds.
#
# 14. **Hours to Minutes**
#     Take hours as input and convert them into minutes.
#
# 15. **Simple Interest**
#     Take:
#
#     * Principal
#     * Rate
#     * Time
#
#     Calculate simple interest.
#     Formula: `SI = (P × R × T) / 100`
#
# 16. **Average of Three Numbers**
#     Take three numbers and print their average.
#
# 17. **Total and Percentage**
#     Take marks of 5 subjects and calculate:
#
#     * Total marks
#     * Percentage
#
# 18. **Bill Calculator**
#     Take the price and quantity of a product and calculate the total bill.
#
# ---
#
# ## 🟠 Level 3 — Multiple Inputs
#
# 19. **Student Details**
#     Take the following as input:
#
#     * Name
#     * Roll number
#     * Age
#     * Marks
#
#     Display all details neatly.
#
# 20. **Employee Salary**
#     Take basic salary, HRA, and bonus as input. Calculate the total salary.
#
# 21. **Shopping Bill**
#     Take the prices of 3 products and calculate:
#
#     * Total amount
#     * Average price
#
# 22. **Travel Distance**
#     Take speed and time as input and calculate distance.
#     Formula: `Distance = Speed × Time`
#
# 23. **BMI Calculator**
#     Take weight in kg and height in meters. Calculate BMI.
#     Formula: `BMI = weight / height²`
#
# 24. **Swap Two Numbers**
#     Take two numbers as input and swap their values.
#
# 25. **Time Conversion**
#     Take a number of seconds and convert it into:
#
#     * Hours
#     * Minutes
#     * Seconds
#
# ---
#
# ## 🔴 Level 4 — Challenge Problems
#
# 26. **Restaurant Bill**
#     Take the prices of 3 dishes, calculate the subtotal, add 5% GST, and display the final bill.
#
# 27. **Salary Calculation**
#     Take basic salary as input. Calculate:
#
#     * HRA = 20% of basic salary
#     * DA = 10% of basic salary
#     * Gross salary = Basic + HRA + DA
#
# 28. **Marks Report**
#     Take marks of 5 subjects and display a formatted report:
#
# ```text
# ----- Student Report -----
# Name: Rahul
# Maths: 85
# Science: 78
# English: 90
# History: 82
# Computer: 95
# Total: 430
# Percentage: 86%
# ```
#
# 29. **Currency Conversion**
#     Take an amount in Indian Rupees and convert it into another currency using a conversion rate provided by the user.
#
# 30. **Bill Splitter**
#     Take:
#
#     * Total restaurant bill
#     * Number of people
#     * Tip percentage
#
#     Calculate how much each person should pay.
#
# ---
#
# ### 🎯 Recommended revision order
#
# Don't solve all 30 randomly. For a **Python basics revision**, I'd suggest:
#
# **First:** 1 → 8
# **Then:** 9 → 18
# **Then:** 19 → 25
# **Finally:** 26 → 30
#
# Try solving them **without looking at solutions**. The main concepts you should practice here are:
#
# ```python
# input()
# print()
# int()
# float()
# str()
# ```
#
# and **type conversion**, especially:
#
# ```python
# age = int(input("Enter your age: "))
# price = float(input("Enter price: "))
# name = input("Enter your name: ")
# ```
#
# If you want, I can also give you **20 Input/Output problems in an interview/practical-exam style, without solutions**, so you can solve them yourself.
