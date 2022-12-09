#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

# Welcome message
print("Welcome to the tip calculator.")
# Ask for total bill, percentage, and how many people to split the bill
bill = float(input("What was the total bill? "))
percent_tip = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
total_people = int(input("How many people to split the bill? "))

percent_float = percent_tip/100
total_tip = bill * percent_float
total_bill = bill + total_tip
# format(value, '.2f') for 2 decimal places
amount_split = format(total_bill/total_people, '.2f')

print(f"Each person should pay: ${amount_split}")