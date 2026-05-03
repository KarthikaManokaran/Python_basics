## 1.Print numbers from 1 to 10 using for loop

for i in range(1,11):
    print(i)

## 2.Print even numbers from 1 to 20

for i in range(2,21,2):
    print(i)

#3.Print odd numbers from 1 to 20

for i in range(1,20,2):
     print(i)

#4.Print multiplication table of 5

for i in range(1,11):
    print(i,"*5 =",i*5)

#Find sum of numbers from 1 to 100
total=0
for i in range(1,101):
   total +=i
print("sum:",total)

#Print squares of numbers from 1 to 10

for i in range(1,11):
    print(i*i)

#Print reverse numbers from 10 to 1
for i in range(10,0,-1):
    print(i)

#Count vowels in a string

string = input("enter your string:")
count = 0

for i in string:
    if i.lower() in 'aeiou':
        count += 1
print("Number of vowels:", count)

#Print each character in string "Python"
for i in "python":
    print(i)

#Find factorial of a number using for loop
num = int(input("Enter a number: "))
fact = 1

for i in range(1, num + 1):
    fact *= i

print("Factorial:", fact)
