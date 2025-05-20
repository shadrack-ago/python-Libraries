import math
print(math.sqrt(16))  # Output: 4.0
print(math.pi)        # Output: 3.141592653589793

# 2. Importing Part of a Library Sometimes, you don’t need the whole toolbox.

# You can import specific functions like this:
from math import sqrt, sin, radians, pow, radians

print("Square root of 36:", sqrt(36))
print("Sine of 90 degrees:", sin(radians(90)))
print("Power of 2^3:", pow(2, 3))

import random
fruits = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
select= random.choice(fruits)
print("Random fruit:", select)

#  3. datetime – Work with dates and time
import datetime
now = datetime.datetime.now()
print("Current date and time:", now)

today=datetime.date.today()
print("Today's date:", today)


from datetime import datetime, timedelta
time= datetime.now()
print("Current time:", time)

