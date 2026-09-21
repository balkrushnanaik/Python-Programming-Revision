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
l = int(input("Enter length of rectangle: "))
b = int(input("Enter breadth of rectangle: "))
area = l * b
print(f"Area of rectangle is: {area}")
# 10. **Perimeter of Rectangle**
#     Take length and breadth and calculate the perimeter.
l = int(input("Enter length of rectangle: "))
b = int(input("Enter breadth of rectangle: "))
perimeter = 2 * (l + b)
print(f"Perimeter of rectangle is: {perimeter}")
# 11. **Area of Circle**
#     Take radius as input and calculate the area of a circle.
#     Use `π = 3.14`.
r = float(input("Enter radius of circle: "))
area = 3.14 * r * r
print(f"Area of circle is: {area}")
# 12. **Temperature Conversion**
#     Take temperature in Celsius and convert it to Fahrenheit.
#     Formula:
#     `F = (C × 9/5) + 32`
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32   
print(f"Temperature in Fahrenheit is: {fahrenheit}")
# 13. **Minutes to Seconds**
#     Take minutes as input and convert them into seconds.
minutes = int(input("Enter minutes: "))
seconds = minutes * 60  
print(f"{minutes} minutes is equal to {seconds} seconds.")
# 14. **Hours to Minutes**
#     Take hours as input and convert them into minutes.
hours = int(input("Enter hours: "))
minutes = hours * 60
print(f"{hours} hours is equal to {minutes} minutes.")

minutes = int(input("Enter minutes: "))
hours = minutes / 60
print(f"{minutes} minutes is equal to {hours} hours.")
# 15. **Simple Interest**
#     Take:
#
#     * Principal
#     * Rate
#     * Time
#     Calculate simple interest.
#     Formula: `SI = (P × R × T) / 100`
p = float(input("Enter principal amount: "))
r = float(input("Enter rate of interest: "))
t = float(input("Enter time in years: "))
si = (p * r * t) / 100
print(f"Simple Interest is: {si}")
# 16. **Average of Three Numbers**
#     Take three numbers and print their average.
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))    
num3 = float(input("Enter third number: "))
average = (num1 + num2 + num3) / 3
print(f"Average of {num1}, {num2}, and {num3} is: {average}")
# 17. **Total and Percentage**
#     Take marks of 5 subjects and calculate:
#
#     * Total marks
#     * Percentage
maths = float(input("Enter marks in Maths: "))
science = float(input("Enter marks in Science: "))
english = float(input("Enter marks in English: "))
total_marks = maths + science + english 
percentage = (total_marks / 300) * 100
print(f"Total Marks: {total_marks}")
print(f"Percentage: {percentage}%")
# 18. **Bill Calculator**
#     Take the price and quantity of a product and calculate the total bill.
#
price = float(input("Enter price of product: "))
quantity = int(input("Enter quantity of product: "))
total_bill = price * quantity
print(f"Total bill for {quantity} products at {price} each is: {total_bill}")
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
#     Display all details neatly.
name, roll_number, age, marks = input("Enter name, roll number, age, and marks separated by commas: ").split(',')
print(f"Name: {name}")
print(f"Roll Number: {roll_number}")    
print(f"Age: {age}")
print(f"Marks: {marks}")
# 20. **Employee Salary**
#     Take basic salary, HRA, and bonus as input. Calculate the total salary.
basic_salary = float(input("Enter basic salary: "))
hra = float(input("Enter HRA: "))   
bonus = float(input("Enter bonus: "))
total_salary = basic_salary + hra + bonus
print(f"Total Salary is: {total_salary}")
# 21. **Shopping Bill**
#     Take the prices of 3 products and calculate:
#
#     * Total amount
#     * Average price
prod1 = float(input("Enter price of product 1: "))
prod2 = float(input("Enter price of product 2: "))
prod3 = float(input("Enter price of product 3: "))
total_amount = prod1 + prod2 + prod3
average_price = total_amount / 3
print(f"Total Amount: {total_amount}")
print(f"Average Price: {average_price}")
# 22. **Travel Distance**
#     Take speed and time as input and calculate distance.
#     Formula: `Distance = Speed × Time`
speed = float(input("Enter speed in km/h: "))
time = float(input("Enter time in hours: "))
distance = speed * time
print(f"Distance traveled is: {distance} km")
# 23. **BMI Calculator**
#     Take weight in kg and height in meters. Calculate BMI.
#     Formula: `BMI = weight / height²`
weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meters: "))
bmi = weight / (height ** 2)
print(f"Your BMI is: {bmi}")    
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
