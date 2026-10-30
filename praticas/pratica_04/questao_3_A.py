''''
import random
while True:
    num = random.randint(10, 50)
    if num == 10 or num == 50:
        break
print(num)
'''

import random

num = random.randint(10, 50)
while num != 10 and num != 50:
    num = random.randint(10, 50)

print(num)