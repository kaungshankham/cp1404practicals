"""
Password
"""

PASSWORD_LENGTH = 10


def main():
    """Get password from user and display stars."""
    password = get_invalid_password()
    display_stars(password)


def get_invalid_password():
    """Check the password meets the PASSWORD_LENGTH."""
    password = input("Enter password: ")
    while len(password) < PASSWORD_LENGTH:
        password = input("Enter password: ")
    return password


def display_stars(password):
    """display stars using password's length."""
    print("*" * len(password))


