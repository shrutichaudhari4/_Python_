#function
def add_two(a,b):
    return a+b
total=add_two(5,6)
print(total)    


def sub_two(a,b):
    return a-b
c=sub_two(6,1)
print(c)    

def myfile(name):
    return name[-1]
print(myfile("shruti"))      

def even_odd(num):
    if num%2==0:
        return "even"
    else:
        return "odd"    
print(even_odd(9))        
oRR
def even_odd(num):
    if num%2==0:
        return "even"
    return "odd"
print(even_odd(9))    


def is_even(num):
    if num%2==0:
        return True
    return False    
print(is_even(9))

def is_even(num):
    return num%2==0
print(is_even(9))


def myfile(name,roll):
    return name,roll
print(myfile("shruti",21))    
print(myfile("priya",88)) 
print(myfile("mitali",77))

def greatest(a,b):
    if a>b:
        return "a"
    return "b"
num1=int(input("enter the number"))
num2=int(input("enter the sec number"))
bigger=greatest(num1,num2)
print(f"{bigger} is greatest")        

def greatest(a,b,c):
    if a>b and a>c:
        return "a"
    elif b>a and b>c:
        return "b" 
    else:
        return "c"

num1=int(input("enter the number"))
num2=int(input("enter the number"))
num3=int(input("enter the number")) 
d=greatest(num1,num2,num3) 
print(f"{d} is greatest")

#function inside function T 76
def new_greatest(a,b,c):
    bigger= greatest(a,b)
    return greatest(bigger,c)

print(new_greatest(10,20,30))

T 77
 
def pallindrome(a):
    if a[::-1]==a:
        return "It is a pallindrome"
    return "not pallindrome"
print(pallindrome("madam"))        

T 82 fibonacci series :
def fibonacci_seq(n):
    a=0 #first number
    b=1 #second number
    if n==1:
        print(a)
    elif n==2:
        print(a,b) #a,b ,0 1
    else:
        print(a,b ,end = " ")
        for i in range(n-2):
            c=a+b #c=1
            a=b #a=1  
            b=c #b=1
            print(b,end=" ")     
fibonacci_seq(10)             





# def PrimeChecker(a):    
#     if a > 1:  
#         # Iterating over the given number with for loop  
#         for i in range(2, int(a/2) + 1):  
#             # If the given number is divisible or not  
#             if (a % i) == 0:  
#                 print(a, "is not a prime number")  
#                 break  
#         # Else it is a prime number  
#         else:  
#             print(a, "is a prime number")  
#     # If the given number is 1  
#     else:  
#         print(a, "is not a prime number")  
# a = int(input("Enter an input number:"))
# PrimeChecker(a)        


