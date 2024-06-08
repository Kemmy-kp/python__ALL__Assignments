'''How will you set the starting value in generating random numbers?

To set the starting value (seed) for generating random numbers in Python,
you can use the random.seed() function from the random module. The seed value
initializes the random number generator algorithm, which then produces a
sequence of pseudo-random numbers.'''

import random

seed_value = 42  

random.seed(seed_value)


random_num1 = random.random()
random_num2 = random.randint(1, 10)
