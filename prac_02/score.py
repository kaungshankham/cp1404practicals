"""
Score
"""

EXCELLENT_SCORE = 90
PASS_SCORE = 50


def main():
    score = get_score()
    determine_status(score)


def determine_status(score):
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


def get_score():
    score = float(input("Enter score: "))
    return score


main()
