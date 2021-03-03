import random

guess = 1
maks = random.randint(1, 101)
print('Think the number from 1 to 100 on your mind')

while (maks):
    guessing = input(f'Is it {maks}? press"l" for low, press"H" for high and press"C" for correct number : ').lower()
    if guessing == "l":
        maks -= 1
    elif guessing == "h":
        maks += 1
    elif guessing == "c":
        print(f"Yeayy the computer found your number {maks}")

print('Game Over')

