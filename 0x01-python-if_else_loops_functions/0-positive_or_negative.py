#!/usr/bin/python3
import random
a = random.randint(-10, 10)
if a > 0:
    print(a, "is posetive")
elif a == 0:
    print(a, "is zero")
else:
    print(a, "is negative")
