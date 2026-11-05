age= 21
if age>= 18:
    print("You are eligible to vote")
    
    age= 16
    if age>= 18:
        print("Eligible to vote")
    else:
        print("Not eligible to vote")
        
marks= 85
if marks>= 90:
    print("Grade A")
elif marks>= 75:
    print("Grade B")
elif marks>= 50:
    print("Grade C")
else:
    print("Fail")
    
age= 21
has_id= True
if age>= 18 and has_id:
    print("Entry allowed")
else:
    print("Entry denied")
    
age= 21
marks= 85

if age >= 18:
    if marks >= 50:
        print("Eligible")
        
age= 16
marks= 90

if age >= 18:
    if marks >= 50:
        print("Eligible")
        
num= int(input("Enter a number: "))
if num> 0:
    print("Positive number")
elif num< 0:
    print("Negative number")
else:
    print("Zero")
    
num= int(input("Enter a number: "))
if num%2== 0:
    print("Even number")
else:
    print("Odd number")
    
age= int(input("Enter the user age: "))
if age>= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")
    
num1= int(input("Enter first number: "))
num2= int(input("Enter second number: "))
num3= int(input("Enter third number: "))
if num1>=num2 and num1>=num3:
    print("Largest number is ",num1)
elif num2>=num1 and num2>=num3:
    print("Largest number is ",num2)
else:
    print("Largest number is ",num3)
    
marks= int(input("Enter the student marks: "))
if marks < 0 or marks > 100:
    print("Invalid marks")
elif marks>= 90:
    print("Grade A")
elif marks>= 75:
    print("Grade B")
elif marks>= 50:
        print("Grade c")
else:
    print("Fail")
    
age= int(input("Enter your age: "))
if age>= 18:
    print("Eligible")
else:
    print("Not eligible")