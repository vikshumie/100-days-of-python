def prime_checker(number):
    is_Prime = True

    for i in range(2, number):
        if number % i == 0:
            is_Prime = False
    if is_Prime == True:
        print("It's a prime number.")        
    else:
        print("It's not a prime number.")

n = int(input("Check this number: "))
prime_checker(number=n)



