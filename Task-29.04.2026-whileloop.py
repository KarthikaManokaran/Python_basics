#While loop:
#1.Print numbers from 1 to 10 using while loop

num = 1
while num <=10:
    print(num)
    num += 1
print("-------------------------------------------------------")
##2.Print even numbers from 1 to 50

num = 2
while num<=50:
    print(num)
    num += 2

print("-------------------------------------------------------")
##3.Print odd numbers from 1 to 50

num = 1
while num<=49:
    print(num)
    num += 2

print("-------------------------------------------------------")
##4.Print reverse numbers from 20 to 1

num =20
while num>=1:
    print(num)
    num -= 1
    
print("-------------------------------------------------------")

##5.Find sum of first 10 natural numbers
num=1
total=0
while num <= 10:
    total += num
    num += 1
print(total)

print("-------------------------------------------------------")

##6.Find factorial using while loop

num = int(input("Enter a number(fact):"))
fact = 1
i =1
while i<=num:
    fact *= i
    i += 1
print(fact)
print("---------------------------------------------------------")

## 7.Count digits in a number
num = int(input("Enter a number: "))

count = 0

while num != 0:
    num //= 10
    count += 1

print("Number of digits:", count)

print("------------------------------------------------------------")

## 8.Reverse a number
num = int(input("Enter a number: "))

rev = 0

while num != 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10

print("Reversed number:", rev)
print("-----------------------------------------------------------")
##9.Check palindrome number
num = int(input("Enter a number: "))

original = num
rev = 0

while num != 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10

if original == rev:
    print("Palindrome")
else:
    print("Not Palindrome")
print("------------------------------------------------------------")
##10.Keep asking password until correct password entered

##correct_password = "admin123"

password = ""

while password != correct_password:
    password = input("Enter password: ")

print("Access Granted")
    
