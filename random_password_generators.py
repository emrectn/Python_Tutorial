import string
import random


def randompassword():
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
    size = random.randint(8, 12)
    a = ''.join(random.choice(chars) for x in range(size))
    return a

randompassword()