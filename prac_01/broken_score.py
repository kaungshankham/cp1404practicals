"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!
EXCELLENT_SCORE = 90
PASS_SCORE = 50

score = float(input("Enter score: "))
if score < 0 or score > 100:
    print("Invalid score")
else:
    if score >= EXCELLENT_SCORE:
        message = "Excellent"
    elif score >= PASS_SCORE:
        message = "Pass"
    else:
        message = "Bad"
print(message)
