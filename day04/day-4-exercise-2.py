# Import the random module here
import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
# Instead of typing: Batman, Superman, Wonder Woman, Iron Man, Captain America
names = names_string.split(", ")

# Note: don't use random.choice() according to exercise
# paying_name = random.choice(names)
# print(paying_name + " is going to buy the meal today!")

# len() function to capture number of people input
num_names = len(names)
# Use randint to generate a random number for indexing. 
# Num_names - 1 necessary as Python begins indexing at 0
random_num = random.randint(0, num_names - 1)
# Index the list of names to see who is paying. Ex. names[0] would yield Batman
paying_name = names[random_num]
# Anddd print the name of the lucky superhero
print(f"{paying_name} is going to buy the meal today!")