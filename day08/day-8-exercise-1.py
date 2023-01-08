from math import ceil

def paint_calc(height, width, cover):
    area = height * width
    num_cans = ceil(area/cover)
    print(f"You'll need {num_cans} cans of paint.")

# Define a function called paint_calc() so that the code below works.   

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
# 1 can of paint can cover 5 square meters (coverage = 5)
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)


