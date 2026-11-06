for i in range(1, 11):
    print(i)
    
for i in range(1,6):
    print("I am learning python")
    
for i in range(1,4):
    print(i*2)
    
for i in range(1,11,2):
    print(i)
    
for i in range(2,21,2):
    print(i)
    
i=1
while i<=10:
    print(i)
    i=i+1
    
i=2
while i<=20:
    print(i)
    i=i+2
    
i=1
total=0
while i<=10:
    total=total+i
    i=i+1
print("Total: ", total)

for i in range(1,11):
    if i==5:
        break
    print(i)
    
i=1
while i<=10:
    if i==6:
        break
    print(i)
    i=i+1
    
for i in range(1,11):
    if i%2==0:
        print("First even number: ", i)
        break
    
for i in range(1,11):
    if i==8:
        print("Number found!", i)
        break
    
for i in range(1,11):
    if i==5:
        continue
    print(i)
    
for i in range(1,16):
    if i%3==0:
        continue
    print(i)
    
for i in range(1,6):
    print(i)
    if i==3:
        break
    
for i in range(1,4):
    for j in range(1,3):
        print(i,j)
        
for i in range(1,5):
    for j in range(i):
            print("*", end="")
    print()
    
for i in range(1,4):
    for j in range(1,5):
        print("*", end="")
    print()

for i in range(1,21):
    if i%2!=0:
        continue
    print(i)
    

total=0
for i in range(1,11):
    total=total+i
print("Total: ", total)

fact=1
for i in range(1,6):
    fact=fact*i
print("Factorial: ", fact)

for i in range(1,11):
    result=5*i
    print("5*",i,"=", result)