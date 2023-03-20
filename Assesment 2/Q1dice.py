import random
N = int(input("Enter N:"))
M = 0

for i in range(N):
    black_die = random.randint(1, 6)
    green_die = random.randint(1, 6)
    if black_die > green_die:
        M += 1

probability = M / N

print("The probability that the number of eyes on the black die is larger than the number of eyes on the green die:", probability)

