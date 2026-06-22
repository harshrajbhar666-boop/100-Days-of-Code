# Write a program to store seven fruits in a list entered by the user.

fruits_list=[]

print("Enter Fruits Name ")

for i in range(7):
    fruits=input(f"fruits{i+1}")

    fruits_list.append(fruits)

    print("\n Fruits list ")
    print("fruits_list")

    # Write a program to accept marks of 6 students and display them in a sorted manner.

    marks_list=[]

    print("Student marks")

    for i in range(6):
        marks=float(input(f"student{i+1}"))
        marks_list.apprnd(marks)

        marks_list.sort()

        print("marks_list")

      #  Check that a type cannot be changed in python.

'''       my_tuple = (2, 4, 5, 6, 45, 34)


Result = my_tuple.count(4)

print("4:", result)'''

      # Write a program to sum a list with 4 numbers.
      numbers = [10, 20, 30, 40]

total = 0 

for i in numbers:
    total = total + i

print("list total sum", total)

         # Write a program to count the number of zeros in the following tuple: a = (7, 0, 8, 0, 0, 9)

         a = (7, 0, 8, 0, 0, 9)

         a=a.count()


