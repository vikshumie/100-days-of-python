#Separate art.py file that has ASCII art of a gavel named logo
#clear() function dependent on IDE
from replit import clear
from art import logo

def highest_bidder(bid_record):
  winner = ""
  winning_bid = 0
  for person in bid_record:
    amount = bid_record[person]
    if amount > winning_bid:
      winning_bid = amount
      winner = person
  print(f"The winner is {winner} with a bid of ${winning_bid}")

bid_log = {}
auction_in_progress = True

print(logo)

while auction_in_progress:
  bidder_name = input("What is your name?: ")
  bid_amount = int(input("What's your bid?: $"))
  bid_log[bidder_name] = bid_amount
  
  more_people = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
  
  if more_people == "no":
    clear()
    highest_bidder(bid_log)
    auction_in_progress = False
  elif more_people == "yes":
    clear()