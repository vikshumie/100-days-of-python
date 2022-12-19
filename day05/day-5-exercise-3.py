#Write your code below this row 👇
# Exercise: write a program that calculates the sum of all the even numbers from 1 to 100.
total = 0
for num in range(2,101,2):
    total += num
print(total)    

# OR
# total = 0
# for num in range(1,101):
#   if num % 2 == 0:
#       total += num
# print(total)
