# Original exercise did not includ while loops or logical operators (yet) - personal challenge
print("Welcome to Python Pizza Deliveries!")

while True:
  size = input("What size pizza do you want? S, M, or L ")
  if size.lower() not in ("s", "m", "l"):
    print("Not an appropriate choice, try again")
    # Returns to the start of the loop and asks for input again until appropriate choice
  else:
    break

while True:
  add_pepperoni = input("Do you want pepperoni? Y or N ")
  if add_pepperoni.lower() not in ("y", "n"):
    print("Not an appropriate choice, try again")
  else:
    break

while True:
  extra_cheese = input("Do you want extra cheese? Y or N ")
  if extra_cheese.lower() not in ("y", "n"):
    print("Not an appropriate choice, try again")
  else:
    break

# Starting off the bill with $0
bill = 0

if size == "S" or size == "s":
  bill = 15
elif size == "M" or size == "m":
  bill = 20
else:
  bill = 25

if add_pepperoni == "Y" or add_pepperoni == "y":
    if size == "S" or size == "s":
        bill += 2
    else:
        bill += 3    

if extra_cheese == "Y" or extra_cheese == "y":
    bill += 1

print(f"Your final bill is: ${bill}")
    
