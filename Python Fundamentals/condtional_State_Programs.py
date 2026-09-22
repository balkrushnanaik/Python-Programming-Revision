# Absolutely. Here are **detailed one-line basic problem statements** to practice **Conditional Statements in Python** (`if`, `if-else`, `if-elif-else`, nested `if`, logical operators).

# ## 🟢 Level 1 — Basic `if` Statements

# 1. **Positive Number:** Write a Python program that takes a number from the user and prints `"Positive"` if the number is greater than 0.
number = float(input("Enter a number: "))
if number > 0:
    print("Positive")
# 2. **Age Check:** Write a program that takes a person's age and prints `"Eligible"` if the age is 18 or above.
age = int(input("Enter your age: "))
if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")
# 3. **Temperature Check:** Write a program that takes the current temperature and prints `"Hot"` if the temperature is greater than 30°C.
# 4. **Passing Marks:** Write a program that takes a student's marks and prints `"Pass"` if the marks are 40 or above.
# 5. **Even Number:** Write a program that takes an integer and prints `"Even"` if the number is divisible by 2.
# 6. **Multiple of 5:** Write a program that takes a number and prints `"Multiple of 5"` if it is completely divisible by 5.
# 7. **Large Number:** Write a program that takes two numbers and prints the first number if it is greater than the second number.
# 8. **Discount Eligibility:** Write a program that takes a customer's purchase amount and prints `"Discount Available"` if the amount is ₹5,000 or more.
# 9. **Voting Age:** Write a program that takes a person's age and prints `"Can Vote"` if the age is 18 or above.
# 10. **Password Length:** Write a program that takes a password and prints `"Strong Length"` if its length is at least 8 characters.

# ## 🟡 Level 2 — `if-else`

# 11. **Even or Odd:** Write a program that takes an integer and prints whether the number is `"Even"` or `"Odd"`.
# 12. **Positive or Negative:** Write a program that takes a number and prints `"Positive"` if it is greater than or equal to 0, otherwise prints `"Negative"`.
# 13. **Pass or Fail:** Write a program that takes marks and prints `"Pass"` when marks are 40 or above, otherwise prints `"Fail"`.
# 14. **Eligible for Driving:** Write a program that takes age and prints `"Eligible"` if the age is 18 or above, otherwise prints `"Not Eligible"`.
# 15. **Greater Number:** Write a program that takes two numbers and prints the greater number, or `"Both are equal"` if they have the same value.
# 16. **Divisible by 3:** Write a program that takes a number and prints `"Divisible"` if it is divisible by 3, otherwise prints `"Not Divisible"`.
# 17. **Profit or Loss:** Write a program that takes cost price and selling price and prints `"Profit"` if selling price is greater than cost price, otherwise prints `"Loss"`.
# 18. **Login Check:** Write a program that takes a username and password and prints `"Login Successful"` if both match predefined credentials, otherwise prints `"Invalid Credentials"`.
# 19. **Free Delivery:** Write a program that takes an order amount and prints `"Free Delivery"` if the amount is ₹500 or more, otherwise prints `"Delivery Charges Applicable"`.
# 20. **Number Comparison:** Write a program that takes two numbers and prints `"First is greater"` if the first number is greater, otherwise prints `"Second is greater or equal"`.

# ## 🟠 Level 3 — `if-elif-else`

# 21. **Grade Calculator:** Write a program that takes marks and prints `"A"` for marks 80–100, `"B"` for 60–79, `"C"` for 40–59, and `"Fail"` for below 40.
# 22. **Age Category:** Write a program that takes age and classifies the person as `"Child"` for 0–12, `"Teenager"` for 13–19, `"Adult"` for 20–59, and `"Senior Citizen"` for 60 or above.
# 23. **Number Sign:** Write a program that takes a number and prints `"Positive"`, `"Negative"`, or `"Zero"` based on its value.
# 24. **Largest of Three:** Write a program that takes three numbers and prints which number is the largest.
# 25. **Day of Week:** Write a program that takes a number from 1 to 7 and prints the corresponding day of the week.
# 26. **Month Days:** Write a program that takes a month number and prints the number of days in that month.
# 27. **Temperature Category:** Write a program that takes temperature and prints `"Cold"` below 15°C, `"Normal"` from 15–30°C, and `"Hot"` above 30°C.
# 28. **Electricity Bill:** Write a program that takes electricity units and calculates the bill using different rates for different consumption ranges.
# 29. **BMI Category:** Write a program that takes BMI and prints `"Underweight"`, `"Normal"`, `"Overweight"`, or `"Obese"` according to standard BMI ranges.
# 30. **Simple Calculator:** Write a program that takes two numbers and an operator (`+`, `-`, `*`, `/`) and performs the selected operation.

# ## 🔵 Level 4 — Logical Operators

# 31. **Voting Eligibility:** Write a program that checks whether a person is at least 18 years old and has Indian citizenship before displaying `"Eligible to Vote"`.
# 32. **Scholarship Eligibility:** Write a program that checks whether a student's marks are at least 75 and family income is below ₹3,00,000 to determine scholarship eligibility.
# 33. **Login Validation:** Write a program that checks whether both username and password are correct before allowing the user to log in.
# 34. **Driving License:** Write a program that checks whether a person's age is at least 18 and they have passed the driving test.
# 35. **College Admission:** Write a program that checks whether a student's percentage is at least 60 and entrance exam score is at least 50.
# 36. **Discount Eligibility:** Write a program that gives a discount if the customer is a member **or** has purchased goods worth more than ₹10,000.
# 37. **Exam Eligibility:** Write a program that checks whether a student's attendance is at least 75% and internal marks are at least 40.
# 38. **Job Eligibility:** Write a program that checks whether a candidate has a degree and at least two years of relevant experience.
# 39. **ATM Withdrawal:** Write a program that allows withdrawal only when the requested amount is within the account balance and is a multiple of ₹100.
# 40. **Password Validation:** Write a program that checks whether a password has at least 8 characters and contains a digit.

# ## 🔴 Level 5 — Nested Conditional Statements

# 41. **ATM Transaction:** Write a program that first checks whether the PIN is correct and, if correct, checks whether the requested withdrawal amount is available in the account.
# 42. **College Admission:** Write a program that first checks whether the student's percentage meets the minimum requirement and then checks their entrance exam score.
# 43. **Shopping Discount:** Write a program that first checks whether the purchase amount is above ₹5,000 and then determines the discount based on whether the customer is a member.
# 44. **Employee Bonus:** Write a program that first checks whether an employee has completed one year and then checks their performance rating to determine the bonus.
# 45. **Bank Loan:** Write a program that first checks the applicant's age and then checks their salary and credit score before approving the loan.
# 46. **Movie Ticket:** Write a program that checks the person's age and then determines the ticket price based on whether they are a child, adult, or senior citizen.
# 47. **Online Exam:** Write a program that first checks the student's login credentials and then checks whether they are eligible to start the examination.
# 48. **E-commerce Order:** Write a program that checks whether the product is available in stock and, if available, checks whether the customer's payment amount is sufficient.
# 49. **Job Application:** Write a program that first checks whether the candidate has the required degree and then checks their programming experience.
# 50. **Restaurant Bill:** Write a program that checks whether the customer is a member and, if they are, applies a membership discount based on the total bill.

# ### 🟣 Level 6 — Real-World Beginner Problems

# 51. **ATM Balance:** Write a program that accepts account balance and withdrawal amount and displays whether the transaction can be completed.
# 52. **Mobile Recharge:** Write a program that takes a recharge amount and displays the corresponding plan benefits based on different recharge ranges.
# 53. **Uber Fare:** Write a program that takes distance travelled and calculates the fare using different rates for different distance ranges.
# 54. **Employee Salary:** Write a program that takes basic salary and calculates the bonus percentage based on the employee's salary range.
# 55. **Student Scholarship:** Write a program that takes marks and family income and determines whether the student qualifies for a scholarship.
# 56. **Electricity Consumption:** Write a program that takes units consumed and calculates the electricity bill using different slabs.
# 57. **Shopping Cart:** Write a program that takes total purchase amount and applies different discount percentages based on the purchase value.
# 58. **Hotel Room Booking:** Write a program that takes the number of nights and room type and calculates the total booking cost.
# 59. **Library Fine:** Write a program that takes the number of late days and calculates the library fine according to different late-day ranges.
# 60. **Employee Attendance:** Write a program that takes total working days and days present and determines whether the employee has sufficient attendance.

# ### 🎯 Recommended Practice Order

# For learning conditional statements from **zero to interview level**, solve them in this order:

# **1–10 → Basic `if`**
# **11–20 → `if-else`**
# **21–30 → `if-elif-else`**
# **31–40 → `and`, `or`, `not`**
# **41–50 → Nested `if`**
# **51–60 → Real-world problems**

# If you want to practice properly, **try solving these without using loops, functions, lists, or exception handling initially**—focus only on `if`, `elif`, `else`, comparison operators, and logical operators.
