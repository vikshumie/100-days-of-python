# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
# For loop exercise - DO NOT use len() and sum() functions
total_height = 0
num_people = 0

for individual_height in student_heights:
    total_height += individual_height
    num_people += 1

avg_height = round(total_height/num_people)
print(avg_height)
