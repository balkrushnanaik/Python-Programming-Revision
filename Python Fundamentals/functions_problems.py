# Absolutely. Here are **detailed one-line problem statements for practicing Python Functions**, arranged from **beginner → intermediate → advanced**, so you can solve them one by one.

# ## 🟢 Level 1 — Basic Functions

# 1. **Create a function `greet_user()` that accepts a user's name as an argument and prints a personalized greeting message such as `"Hello, Balkrushna! Welcome to Python."`**
name = input("Enter your name: ")
def greet_user(name):
    return f"Hello, {name}! Welcome to Python."
greeting_message = greet_user(name)
print(greeting_message)
# 2. **Create a function `add_numbers()` that accepts two numbers and returns their sum without printing the result inside the function.**
num1 = 10
num2 = 20
def add_numbers(num1, num2):
    return num1 + num2
addition_result = add_numbers(num1, num2)
print(f"The sum of {num1} and {num2} is: {addition_result}")

# 3. **Create a function `calculate_difference()` that accepts two numbers and returns the difference between the first and second number.**
def calculate_difference(num1, num2):
    return num1 - num2
difference_result = calculate_difference(num1, num2)
print(f"The difference between {num1} and {num2} is: {difference_result}")
# 4. **Create a function `multiply_numbers()` that accepts two numbers and returns their multiplication result.**
def multiply_numbers(num1, num2):
    return num1 * num2
multiplication_result = multiply_numbers(num1, num2)
print(f"The multiplication of {num1} and {num2} is: {multiplication_result}")
# 5. **Create a function `divide_numbers()` that accepts two numbers and returns their division result while safely handling division by zero.**
def divide_numbers(num1, num2):
    if num2 == 0:
        return "Error: Division by zero is not allowed."
    return num1 / num2  
devision_result = divide_numbers(num1, num2)
print(f"The division of {num1} by {num2} is: {devision_result}")
# 6. **Create a function `square_number()` that accepts a number and returns its square using an arithmetic operation.**
def square_number(num):
    return num ** 2
square_result = square_number(num1)
print(f"The square of {num1} is: {square_result}")
# 7. **Create a function `cube_number()` that accepts a number and returns its cube.**
def cube_number(num):
    return num ** 3
cube_result = cube_number(num1)
print(f"The cube of {num1} is: {cube_result}")
# 8. **Create a function `is_even()` that accepts an integer and returns `True` if the number is even and `False` otherwise.**
# 9. **Create a function `is_positive()` that accepts a number and determines whether the number is positive, negative, or zero.**
# 10. **Create a function `find_max()` that accepts two numbers and returns the larger number without using Python's built-in `max()` function.**

# ## 🟢 Level 2 — Functions with Conditions

# 11. **Create a function `check_eligibility()` that accepts a person's age and returns whether the person is eligible to vote based on the legal voting age of 18.**
# 12. **Create a function `check_number()` that accepts an integer and returns `"Positive"`, `"Negative"`, or `"Zero"` depending on its value.**
# 13. **Create a function `find_largest()` that accepts three numbers and returns the largest number without using the built-in `max()` function.**
# 14. **Create a function `check_divisibility()` that accepts two integers and returns whether the first number is completely divisible by the second number.**
# 15. **Create a function `calculate_grade()` that accepts a student's marks and returns a grade based on predefined marks ranges such as A, B, C, D, and F.**
# 16. **Create a function `calculate_discount()` that accepts a product price and discount percentage and returns the final price after applying the discount.**
# 17. **Create a function `calculate_tax()` that accepts an income amount and calculates the tax according to different income slabs.**
# 18. **Create a function `is_leap_year()` that accepts a year and returns whether the given year is a leap year according to the standard leap-year rules.**
# 19. **Create a function `check_password()` that accepts a password and returns whether it satisfies minimum requirements such as length and the presence of numbers.**
# 20. **Create a function `calculate_bill()` that accepts the total purchase amount and applies different discount percentages based on the purchase range before returning the final payable amount.**

# ## 🟡 Level 3 — Functions with Strings

# 21. **Create a function `count_characters()` that accepts a string and returns the total number of characters without using the built-in `len()` function.**
# 22. **Create a function `count_vowels()` that accepts a string and returns the total number of vowels present in the string.**
# 23. **Create a function `reverse_string()` that accepts a string and returns the string in reverse order without using the built-in `reversed()` function.**
# 24. **Create a function `is_palindrome()` that accepts a string and determines whether it reads the same forward and backward.**
# 25. **Create a function `count_words()` that accepts a sentence and returns the number of words contained in the sentence.**
# 26. **Create a function `capitalize_words()` that accepts a sentence and returns a new sentence where the first letter of every word is capitalized.**
# 27. **Create a function `remove_spaces()` that accepts a string and returns the same string after removing all spaces.**
# 28. **Create a function `count_character_frequency()` that accepts a string and a character and returns how many times that character appears in the string.**
# 29. **Create a function `find_longest_word()` that accepts a sentence and returns the longest word without using a library designed specifically for finding the longest element.**
# 30. **Create a function `check_anagram()` that accepts two strings and determines whether they contain the same characters with the same frequency.**

# ## 🟡 Level 4 — Functions with Lists

# 31. **Create a function `find_list_sum()` that accepts a list of numbers and returns the total sum without using Python's built-in `sum()` function.**
# 32. **Create a function `find_list_average()` that accepts a list of numbers and returns their average using a separate function to calculate the total.**
# 33. **Create a function `find_largest_in_list()` that accepts a list of numbers and returns the largest value without using `max()`.**
# 34. **Create a function `find_smallest_in_list()` that accepts a list of numbers and returns the smallest value without using `min()`.**
# 35. **Create a function `count_even_numbers()` that accepts a list of integers and returns how many values in the list are even.**
# 36. **Create a function `filter_positive_numbers()` that accepts a list of numbers and returns a new list containing only positive numbers.**
# 37. **Create a function `remove_duplicates()` that accepts a list and returns a new list containing each element only once while preserving its original order.**
# 38. **Create a function `second_largest()` that accepts a list of numbers and returns the second-largest unique number in the list.**
# 39. **Create a function `sort_numbers()` that accepts a list of numbers and returns the numbers in ascending order without using the built-in `sort()` or `sorted()` functions.**
# 40. **Create a function `find_common_elements()` that accepts two lists and returns the elements that occur in both lists without returning duplicates.**

# ## 🟡 Level 5 — Functions with Dictionaries

# 41. **Create a function `student_average()` that accepts a dictionary containing subject names and marks and returns the student's average marks.**
# 42. **Create a function `highest_scorer()` that accepts a dictionary containing student names and marks and returns the name of the student with the highest marks.**
# 43. **Create a function `count_frequency()` that accepts a list of values and returns a dictionary containing the frequency of each value.**
# 44. **Create a function `find_expensive_products()` that accepts a dictionary of product names and prices and returns products whose prices exceed a specified amount.**
# 45. **Create a function `calculate_inventory_value()` that accepts a dictionary containing product names, quantities, and prices and returns the total inventory value.**
# 46. **Create a function `merge_dictionaries()` that accepts two dictionaries and returns a single dictionary containing all key-value pairs from both dictionaries.**
# 47. **Create a function `find_department_salary()` that accepts employee records and returns the average salary for a specified department.**
# 48. **Create a function `highest_salary_employee()` that accepts employee information and returns the employee record having the highest salary.**
# 49. **Create a function `group_students_by_grade()` that accepts student marks and returns a dictionary grouping students according to their grades.**
# 50. **Create a function `calculate_sales_by_product()` that accepts sales records and returns a dictionary containing the total sales amount for each product.**

# ## 🟠 Level 6 — Default Arguments & Keyword Arguments

# 51. **Create a function `calculate_simple_interest()` that accepts principal, rate, and time as arguments, with a default interest rate that is used when the caller does not provide one.**
# 52. **Create a function `create_profile()` that accepts a user's name, age, city, and profession using default values for optional information.**
# 53. **Create a function `calculate_salary()` that accepts basic salary and optional bonus and allowance values with appropriate default values.**
# 54. **Create a function `generate_invoice()` that accepts customer name, product name, quantity, and price while allowing the caller to provide arguments using either positional or keyword syntax.**
# 55. **Create a function `book_ticket()` that accepts passenger name, destination, seat type, and number of tickets with default values for seat type and ticket quantity.**

# ## 🟠 Level 7 — `*args` and `**kwargs`

# 56. **Create a function `calculate_total()` that accepts any number of numeric arguments using `*args` and returns their total.**
# 57. **Create a function `find_average()` that accepts any number of numbers using `*args` and returns their average.**
# 58. **Create a function `find_maximum()` that accepts any number of numeric arguments using `*args` and returns the largest value without using `max()`.**
# 59. **Create a function `create_student_record()` that accepts a student's name as a required argument and any number of additional details using `**kwargs`, then returns them as a dictionary.**
# 60. **Create a function `display_employee_details()` that accepts any number of keyword arguments using `**kwargs` and displays each employee attribute in a readable format.**
# 61. **Create a function `calculate_expenses()` that accepts multiple expense amounts using `*args` and optional category information using `**kwargs` and returns the required expense summary.**
# 62. **Create a function `combine_data()` that accepts positional values using `*args` and named values using `**kwargs` and returns a structured dictionary containing both types of information.**

# ## 🔴 Level 8 — Real-World Data Analytics Functions

# 63. **Create a function `calculate_sales_total()` that accepts a list of sales transactions and returns the total sales amount after ignoring invalid or negative transaction values.**
# 64. **Create a function `calculate_monthly_sales()` that accepts sales records containing dates and amounts and returns total sales grouped by month.**
# 65. **Create a function `calculate_employee_average_salary()` that accepts employee records and returns the average salary of all employees after handling missing salary values.**
# 66. **Create a function `find_top_products()` that accepts product sales data and returns the top N products based on total revenue.**
# 67. **Create a function `calculate_conversion_rate()` that accepts the number of visitors and customers and returns the customer conversion percentage while preventing division-by-zero errors.**
# 68. **Create a function `calculate_customer_lifetime_value()` that accepts average purchase value, purchase frequency, and customer lifespan and returns the estimated customer lifetime value.**
# 69. **Create a function `calculate_profit_margin()` that accepts revenue and cost values and returns the profit margin percentage after validating the input values.**
# 70. **Create a function `clean_sales_data()` that accepts a list of sales records and returns cleaned records after removing missing, invalid, or negative sales values.**
# 71. **Create a function `find_best_salesperson()` that accepts employee sales records and returns the salesperson with the highest total sales.**
# 72. **Create a function `calculate_product_performance()` that accepts product sales data and returns each product's total quantity sold, revenue, and average selling price.**

# ## 🔴 Level 9 — Multiple Functions Working Together

# 73. **Create separate functions to calculate total marks, percentage, grade, and pass/fail status for a student, and create a main function that calls all four functions to generate the final result.**
# 74. **Create separate functions for calculating subtotal, discount, tax, and final bill amount, and combine them into an invoice-generation function.**
# 75. **Create separate functions to validate user input, calculate account balance, and generate a transaction summary for a simple banking application.**
# 76. **Create separate functions to calculate product revenue, total revenue, average revenue, and highest-selling product from a sales dataset.**
# 77. **Create separate functions to clean employee data, calculate salary statistics, and identify the highest-paid employee from employee records.**
# 78. **Create separate functions for adding, updating, deleting, and searching student records and combine them into a simple student-management system.**
# 79. **Create separate functions for calculating batting average, strike rate, total runs, and highest score and use them to generate a cricket player's performance report.**
# 80. **Create separate functions for calculating order subtotal, discount, GST, shipping charges, and final payable amount and combine them into an e-commerce checkout system.**

# ## 🔥 Level 10 — Advanced Function Challenges

# 81. **Create a function that accepts another function as an argument and applies that function to every element of a given list.**
# 82. **Create a function that returns another function capable of calculating the power of numbers using a predefined exponent.**
# 83. **Create a recursive function that calculates the factorial of a given positive integer without using loops.**
# 84. **Create a recursive function that calculates the nth Fibonacci number without using loops.**
# 85. **Create a recursive function that calculates the sum of all numbers from 1 to N.**
# 86. **Create a function decorator that measures and prints the execution time of another function.**
# 87. **Create a decorator that checks whether the user has permission to execute a particular function before allowing it to run.**
# 88. **Create a function that accepts another function and a list of values and returns a new list containing the transformed values.**
# 89. **Create a function that uses a lambda expression to filter a list and return only values satisfying a specified condition.**
# 90. **Create a function that uses `map()`, `filter()`, and `reduce()` to process a list of sales values and calculate meaningful business statistics.**

# ### 📊 Best order for Data Analytics practice

# Since you're learning **Python for Data Analytics**, I recommend solving them in this order:

# **1–20 → Basic function logic**  
# **21–40 → Strings & Lists**  
# **41–50 → Dictionaries**  
# **51–62 → Function arguments**  
# **63–72 → Data Analytics problems** ⭐  
# **73–80 → Real-world mini projects** ⭐  
# **81–90 → Advanced Python functions**

# A particularly important set for you is **63–80**, because these problems start connecting Python functions with the type of **sales, employee, customer, and business datasets** you'll encounter in Data Analyst interviews.