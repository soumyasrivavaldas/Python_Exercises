#1.Write a program to find sum of number.

num1= int(input("Enter the value of num1:-"))
num2=int(input("Enter the value of num2:-"))
num=num1+num2
print(num)

'''output:
     Enter the value of num1:-25
     Enter the value of num2:-21
     46'''
#------------------------------------------------------------------------------------------------------
#2.WAP to find the number is strong number or not

sum=0    
num=int(input("Enter a number:"))   
temp=num 
while(num):    
    i=1  
    fact=1  
    rem=num%10  
    while(i<=rem):  
        fact=fact*i    
        i=i+1  
    sum=sum+fact  
    num=num//10  
if(sum==temp):  
    print(temp,"is a strong number")  
else:  
    print(temp,"is not a strong number")
    
'''output:
    Enter a number:145
    145 is a strong number
    Enter a number:153
    153 is not a strong number'''
#-------------------------------------------------------------------------------------------------------     
#3.Python Program to Find the Square Root

num=int(input("Enter the value of n:"))
if(num<0):
    print("Enter the positive value")
else:
    squareroot=num**0.5
    print(sqrt)
    
'''output:
    Enter the value of n:4
    2.0'''
#---------------------------------------------------------------------------------------------------------
#4.Python Program to Calculate the Area of a Triangle

height=int(input("Enter the value of height:-"))
base=int(input("Enter the value of base:-"))
area=height*base//2
print(area,"is a area of triangle")

'''output:
        Enter the value of height:-5
        Enter the value of base:-4
        10 is a area of triangle '''
#---------------------------------------------------------------------------------------------------------
#5.Python Program to Solve Quadratic Equation
        
a=int(input("Enter the value of a:"))   
b=int(input("Enter the value of b:"))       
c=int(input("Enter the value of c:"))
d=b**2-4*a*c
if(d<0):
    d=-d                     #or  
    numerater=-b-d**0.5            #numerater=-b+d**0.5
    denominater=2*a                #denominater=2*a
    Total=numerater/denominater    #Total=numerater/denominater
    print(Total)                   #print(Total) 
else:                 
    numerater=-b-d**0.5            #numerater=-b+d**0.5                
    denominater=2*a                #denominater=2*a
    Total=numerater/denominater    #Total=numerater/denominater
    print(Total)                   #print(Total)
    
'''output:
    Enter the value of a:1
    Enter the value of b:2
    Enter the value of c:-15
    -5.0  ''' 
    
#--------------------------------------------------------------------------------------------------------    
#6.Python Program to Swap Two Variables
    
num1=int(input("Enter the value of num1:-"))
num2=int(input("Enter the value of num2:-"))
print("before swaping of num1:",num1)
print("before swaping of num2:",num2)
temp=num1
num1=num2
num2=temp
print("after swaping of num1:",num1)
print("after swaping of num2:",num2)

'''output:
        Enter the value of num1:-5
        Enter the value of num2:-6
        before swaping of num1: 5
        before swaping of num2: 6
        after swaping of num1: 6
        after swaping of num2: 5'''

#------------------------------------------------------------------------------------------------------
#7.Python Program to Convert Kilometres to Mile

kilometer=float(input("Enter number of kilometers:"))
onemile=0.621371
con_mile=kilometer*onemile
print(con_mile)

'''output:
       Enter number of kilometers:5
       3.106855'''

#------------------------------------------------------------------------------------------------------------
#8.Python Program to Check Leap Year

year = int(input("enter the year:-"))
if (year % 400 == 0) and (year % 100 == 0):
    print(year," is a leap year")
else:
    print(year," is not a leap year")
    
'''output:
    enter the year:-2000
    2000  is a leap year
    enter the year:-2022
    2022  is not a leap year'''
#-------------------------------------------------------------------------------------------------------------    
#9.Python Program to Check Prime Number

n=int(input("enter the value of n:-"))
if(n>1):
    for i in range(2,n):
        if(n%i)==0:
            print(n,"is not a prime number")
            break
    else:
        print(n,"is a prime number")
else:
    print(n,"is a invalid number")

'''output:
    enter the value of n:-5
    5 is a prime number
    enter the value of n:-4
    4 is not a prime number '''
#--------------------------------------------------------------------------------------------------------------
#10.Python Program to Find the Factorial of a Number

n=int(input("Enter the value of n:"))
if(n<0):
    print("Invalid no")
elif(n==0):
    print("factorial of 0 is 1")
else:
    fact=1
fact=1
for i in range(1,n+1):
    fact=fact*i
print(fact)

'''output:
       Enter the value of n:5
       120
       Enter the value of n:0
       factorial of 0 is 1
       1
       Enter the value of n:-2
       Invalid no
       '''
    
#------------------------------------------------------------------------------------------------------------
#11.Python Program to Print the Fibonacci sequence 

n=int(input("Enter the value of num:"))
num1=0
num2=1
if(n<0):
    print("Please enter the positive number")
elif(n==0):
    print("Enter the valid number")
else:
    for i in range (0,n):
        num3=num1+num2
        num1=num2
        num2=num3
    print(num3,end=" ")
    
'''output:
    Enter the value of num:5
    8
    Enter the value of num:-8
    Please enter the positive number
    Enter the value of num:0
    Enter the valid number '''

#------------------------------------------------------------------------------------------------------
#12.Python Program to Check Armstrong Number

n=int(input("enter the value of n:-"))
num=str(n)
sum=0
for i in num:
    sum=sum+int(i)*int(i)*int(i)
if(sum==n):
    print(n,"is a armstrong")
else:
    print(n,"is not a armstrong")
    
'''output:
    enter the value of n:-153
    153 is a armstrong
    enter the value of n:-452
    452 is not a armstrong '''

#-----------------------------------------------------------------------------------------------------------
#13.Python Program to Find Armstrong Number in an Interval
lower=int(input("Enter the value of lower:"))
upper=int(input("Enter the value of upper:"))

for num in range(lower,upper+1):
    order=len(str(num))
    sum=0
    temp=num
    while temp>0:
        digit=temp%10
        sum+=digit**order
        temp//=10
    if num==sum:
        print(num)
        
'''output:
        Enter the value of lower:100
        Enter the value of upper:500
        153
        370
        371
        407 '''

#---------------------------------------------------------------------------------------------------------
#14.Python Program to Find the Sum of Natural Numbers

num=int(input("Enter the value of num:"))
sum=0
for i in range(0,num+1):
    sum=sum+i
print(sum)

'''output:
        Enter the value of num:12
        78
      '''
#-----------------------------------------------------------------------------------------------------------
#15.Python Program to Find the Factors of a Number
num=int(input("Enter the value of num:"))
for i in range(1,num+1):
    if num%i==0:
        print(i)
'''output:
        Enter the value of num:12
        1
        2
        3
        4
        6
        12 '''

#-----------------------------------------------------------------------------------------------------------       
#16.Python program to convert decimal into other number systems
#Binary to Decimal:
        
dec = int(input("Enter the value of decimal:"))
a=[]
while(dec>0):
    dig=dec%2
    a.append(dig)
    dec=dec//2
a.reverse()
print("Binary number of is:")
for i in a:
    print(i,end=" ")

'''output:
    Enter the value of decimal:16
    Binary number of is:
    1 0 0 0 0
'''
#Binary to octal:
    
dec = int(input("Enter the value of decimal:"))
a=[]
while(dec>0):
    dig=dec%8
    a.append(dig)
    dec=dec//8
a.reverse()
print("Octal number of is:")
for i in a:
    print(i,end=" ")
    
'''output:
       Enter the value of decimal:33
       Octal number of is:
       4 1'''

#Binary to Hexadecimal:

hexa_table = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
                    5: '5', 6: '6', 7: '7',
                    8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C',
                   13: 'D', 14: 'E', 15: 'F'}
hexadecimal=" "
decimal=int(input("Enter the decimal value:"))
while(decimal>0):
    remainder=decimal%16
    hexadecimal=hexa_table[remainder] + hexadecimal
    decimal=decimal//16
print(hexadecimal)

'''output:
        Enter the decimal value:68
        44
        Enter the decimal value:45
        2D '''
    
#----------------------------------------------------------------------------------------------------------
#17.Python Program to Find LCM

num1=int(input("Enter the value of num1:-"))
num2=int(input("Enter the value of num2:-"))
if(num1>num2):
    smaller=num1
else:
    smaller=num2
while(True):
    if(smaller%num1==0 and smaller%num2==0):
        print(smaller)
        break
    smaller=smaller+1
    
'''output:
    Enter the value of num1:-12
    Enter the value of num2:-24
    24'''

#-------------------------------------------------------------------------------------------------------
#18.Python Program to Find HCF
    
num1=int(input("Enter the value of num1:-"))
num2=int(input("Enter the value of num2:-"))
if(num1>num2):
    smaller=num1
else:
    smaller=num2
for i in range(1,smaller+1):
    if((num1 % i == 0) and (num2 % i == 0)):
            hcf = i
print(hcf)

'''output:
      Enter the value of num1:-24
      Enter the value of num2:-48
      24 '''      














