def add_too(num1,num2):
    return num1+num2
first=int(input("enter first number"))
last=int(input("enter last number"))
print(add_too(first,last))

name=input("enter first name")
sec=input("enter last name")
print(add_too(name,sec))

nam=float(input("enter first num"))
secound=float(input("enter last number"))
print(add_too(nam,secound))

# even odd number condectoin
def odd_even(num):
    if num%2==0:
        return "even"
    else:
        return "odd"
    print(odd_even(12))

# exersize 1 chaptir 1
def biger(a,b):
    if a>b:
        return a
    else:
        return b
num1=int(input("enter first number"))
num2=int(int("enter last number"))
bigger=(num1,num2)
print(f"{bigger}is greater")
