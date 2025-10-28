'''Max of Three Numbers
Ask the user for 3 numbers and print the largest one.'''

a = int(input("Enter 1st number:"))
b = int(input("Enter 2nd number:"))
c = int(input("Enter 3rd number:"))

if a> b and a>c:
    print("Largest number is:", a)
elif b>a and b>c:
    print("Largest number is:",b)
else:
    print("Largest number is:",c)

