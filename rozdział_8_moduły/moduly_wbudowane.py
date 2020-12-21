import math
import random
import statistics
import keyword

print(math.pow(2, 3))

print(random.randint(0, 100))

nums = [1, 5, 33, 12, 46, 33, 2]

# średnia
print(statistics.mean(nums))

# mediana
print(statistics.median(nums))

# dominanta
print(statistics.mode(nums))

# sprawdzanie słów kluczowych

print(keyword.iskeyword("for"))
print(keyword.iskeyword("foootbal"))