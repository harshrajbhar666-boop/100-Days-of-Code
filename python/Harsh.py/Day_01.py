'''#Apna naam
print("Harsh Rajbhar")
print("Atul Kumar")

#Do number(variable)

a=76
b=90

c=a+b
print(c)

#Float,Strinf,f-string

name="Harsh"
age=76

print(f"mara  naam {name} aur mare age {age}")

#User sa input lana hai 

user=input("Enter Your Name:")
user_age=int(input("Enter Your Age:"))

print(user,user_age)

#Celsius se Fahrenheit

c=float(input("celsius:"))
f = c * 9 / 5 + 32
print(f"{c}C = {f}F")

#Swap

x,y,z,v=2,3,4,5
print(x,y,z,v)

a=40
b=50

a,b=b,a

print(a,b)

#Marks

marks = 90
print("Marks: " + str(marks))'''

# Do decimal 

m1=int(input("M1:"))
m2=int(input("M2:"))
m3=int(input("M3:"))

avg=(m1+m2+m3)/3

print(f"Average={avg:.2f}")

#Simple interest

p = float(input("Paisa: "))
r = float(input("Rate: "))
t = float(input("Saal: "))
si = (p * r * t) / 100
print(f"Interest = {si:.2f}")

#Chhota receipt

item = "Chai"
price = 15
qty = 2
print("-" * 20)
print(f"{item} x {qty} = {price * qty}")
print("-" * 20)
