import random
import string


def generate_random_string(length=10):
    letter = string.ascii_letters
    otp = "".join(random.choice(letter) for _ in range(length))
    return otp