##count vowels in a string input: programming,output 3
total=0
for i in "programming":
    if i in "aeiou":
        total+=1
print(total)

## 2.Sum of Numbers from 1 to N,Input: 5,Output: 15  (1+2+3+4+5)

total=0
for i in range(1,6):
    total+=i
print(total)

##3.Fibonacci Series (Using for loop),Input: 7,Output: 0 1 1 2 3 5 8
start=0
nextnum=1
for i in range(7):
    print(start, end="  ")
    count =start+nextnum
    start=nextnum
    nextnum=count
    
##4.Count Even and Odd Numbers,Input:[10, 3, 5, 8, 6, 11],Output:Even: 3,Odd: 3

even=0
odd=0
for i in [10,3,5,8,6,11]:
    if i%2==0:
        even+=1
    else:
        odd+=1
print()
print("Even:",even,"odd:",odd)

##5.Remove Duplicates from List (Without set),Input:[1,2,2,3,4,4,5],Output:[1,2,3,4,5]
duplicate = []
for i in [1,2,2,3,4,4,5]:
    if i not in duplicate:
        duplicate.append(i)

print(duplicate)
