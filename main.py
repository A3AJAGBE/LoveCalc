"""
A program that tests the compatibility between two people.
Using the super scientific method recommended by BuzzFeed.
"""

# Display a message to start
print("Love Calculator!")
print("Check your compatibility with your partner\n")

# Prompt for the names
your_name = input("What is your name? \n").lower()
partner_name = input("What is their name? \n").lower()

# Combine the names
combine = your_name + partner_name

# Count the occurrence of 'true love' characters
t = combine.count('t')
r = combine.count('r')
u = combine.count('u')
e = combine.count('e')
true = t + r + u + e
l = combine.count('l')
o = combine.count('o')
v = combine.count('v')
# e is missing because its already completed above
love = l + o + v + e

# Concatenate and convert to loop through
truelove = str(true) + str(love)
lovescore = int(truelove)

# Interpret the output
if (lovescore < 10) or (lovescore > 90):
    print(f"Your compatibility score is {lovescore}, you go together like coke and mentos.")
elif (lovescore >= 40) and (lovescore <= 50):
    print(f"Your compatibility score is {lovescore}, you are alright together.")
else:
    print(f"Your compatibility score is {lovescore}.")
