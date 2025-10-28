#Take a score (0–100) and print a grade:
#A: 90+, B: 80-89, C: 70-79, D: 60-69, F: <60

score = int(input("Enter your score:"))

if score >= 90:
    print("Your Grade is: A")
elif score >= 80 and score < 90:
    print("Your Grade is: B")
elif score >= 70 and score < 80:
    print("Your Grade is: C")
elif score >= 60 and score < 70:
    print("Your Grade is: D")
else:
    print("Your Grade is: F")