"""Given an integer, n, perform the following conditional actions:

If n is odd, print Weird

If n  is even and in the inclusive range of 2 to5 , print Not Weird

If  n is even and in the inclusive range of 6 to20 , print Weird

If n  is even and greater than 20 ,"""

n = int(input())  


if n % 2 != 0:
    print("Weird")


else:
    
    if 2 <= n <= 5:
        print("Not Weird")
    
    
    elif 6 <= n <= 20:
        print("Weird")
    
    
    elif n > 20:
        print("Not Weird")

       """ The provided code stub reads two integers from STDIN,  and . Add code to print three lines where:

The first line contains the sum of the two numbers.

The second line contains the difference of the two numbers (first - second).

The third line con"""

a = int(input())
b = int(input())


print(a + b)
print(a - b)
print(a * b)
"""The provided code stub reads two integers,a and b , from STDIN.
Add logic to print two lines. The first line should contain the result of integer division,  // . The second line should contain the result of float division,  / .
No rounding or formatting is necessary.
"""

a = int(input())
b = int(input())

print(a // b)
print(a / b)

"""The provided code stub reads an integer, , from STDIN. For all non-negative integers ,i<n print .i spure """


n = int(input())


for i in range(n):
    
    print(i * i)




