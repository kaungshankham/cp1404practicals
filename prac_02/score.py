"""
Score
"""

EXCELLENT_SCORE = 90
PASS_SCORE = 50


def main():
    """Get score from the users and display their status."""
    score = get_score()
    determine_status(score)


def determine_status(score):
    """Determine the status."""
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
    """Get score from user."""
    score = float(input("Enter score: "))
    return score
