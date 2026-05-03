num = input("Enter a number:")
 
if not num.isalpha():
     num = int(num) 
     if type(num) == int or type(num) == float:    
         if num%2==0:
             print("Even")
         elif num%2!=0:
            print("odd")
else:
        print("end")

##---------------------------------------------------------------------------------

### Task:
        ##Write a Python program that:
	##1. Takes five input marks from the user.
	##32. Calculates the total of the marks.
	##3. Computes the average of the marks.
	##4. Assigns a grade based on the average using the following criteria:
		#• 90 and above: A+
		#• 80 to 89: A
		#• 70 to 79: B
		#• 60 to 69: C
		#• 50 to 59: D
		#• Below 50: F
	##5. Displays the total marks, average marks (formatted to two decimal places),
	  ## and the assigned grade.
##Ans:
subjects = ["Tamil", "English", "Maths", "Science", "Social"]

marks = []

for subject in subjects:
    mark = int(input(f"Enter mark of {subject}: "))
    marks.append(mark)

total = sum(marks)
average = total / 5


if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"


print("\n--- Result ---")
print("Total Marks:", total)
print("Average Marks: {:.2f}".format(average))
print("Grade:", grade)


#2.Write a Python program that calculates the fine for overdue library books based
  #on the following conditions:
	#•	0 to 10 days → Fine is ₹1
	#•	11 to 20 days → Fine is ₹5
	#•	21 to 30 days → Fine is ₹10
	#•	More than 30 days → Print "fine not define for this range"


days = int(input("Enter number of overdue days: "))

if 0 <= days <= 10:
    fine = 1
    print("Fine is ₹", fine)
elif 11 <= days <= 20:
    fine = 5
    print("Fine is ₹", fine)
elif 21 <= days <= 30:
    fine = 10
    print("Fine is ₹", fine)
elif days > 30:
    print("Fine not define for this range")
else:
    print("Invalid input")

#3.Check Even or Odd
	#•	#Write a Python program to check if a given number is even or odd using an 
		#if statement.
num=int(input("Enter the number:"))
print("Even" if num%2==0 else "odd")

#4.Check Voting Eligibility
	#•	Ask the user for their age and check if they are eligible to 
		#vote (18 or older).
age=int(input("Enter your Age:"))
print("you are elligible to vote" if age>=18 else "You are waiting to complete your age is 18")

#5.Find the Largest Number
	#•	Take three numbers as input and print the largest one using if conditions.


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

print("Largest number is:", largest)

#6.Check Leap Year
	#•	Write a program to check if a given year is a leap year or not.

year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")

#7.Check for Vowel or Consonant
	#•	Take a character as input and check if it’s a vowel (a, e, i, o, u) or a consonant.
		 
letter = input("Enter a character: ").lower()

if len(letter) == 1 and letter.isalpha():
    if letter in ['a', 'e', 'i', 'o', 'u']:
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Invalid input")

#8.Check Positive, Negative, or Zero • Take a number as input and determine if it’s positive, negative, or zero.

num = float(input("Enter a number: "))

if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")

#9.Divisibility Test
	#•	Write a program that checks if a number is divisible by both 5 and 7.

num = int(input("Enter a number: "))

if num % 5 == 0 and num % 7 == 0:
    print("The number is divisible by both 5 and 7")
else:
    print("The number is NOT divisible by both 5 and 7")
