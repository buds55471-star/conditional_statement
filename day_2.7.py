'''Check Character Type
Input a character. Check if it's a letter, digit, or special character.'''

chr = input("Enter your character name:")

if chr.isalpha():
    print("It's a letter")
elif chr.isdigit():
    print("It's a digit")
elif chr =="!@#$%^&*()":
    print("It's a special character")
