from art import logo

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1/n2

operations = {
  "+": add, 
  "-": subtract, 
  "*": multiply, 
  "/": divide
}

def calculator():
  print(logo)
  
  num1 = float(input("What's the first number?: "))
  for sign in operations:
    print(sign)
  is_calculating = True
  
  while is_calculating:
    
    operation_sign = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    
    calculator_function = operations[operation_sign]
    answer = calculator_function(num1, num2)
    
    print(f"{num1} {operation_sign} {num2} = {answer}")
    
    to_continue = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.: ")
    if to_continue == 'y':
      num1 = answer
    else:
      is_calculating = False
      calculator()

calculator()