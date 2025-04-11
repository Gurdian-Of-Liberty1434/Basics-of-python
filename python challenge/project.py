import random
import string
password = string.ascii_letters + string.digits
password = list(password)
random.shuffle(password)
password = "".join(password)
print(password)