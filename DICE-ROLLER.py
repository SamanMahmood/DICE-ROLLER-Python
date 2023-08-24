import random

def roll_dice():
    return random.randint(1, 6)

# Roll the dice 
result = roll_dice()
print(f"You rolled a {result}")
# if you have two dice then you can print two reault in f string. 
# and if your choice have more dice then you add twice result.
print(f"You rolled a {result} {result}")

