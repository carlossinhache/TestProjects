def prime_checker(number):
    # prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    if number == 1 or number == 0:
        print("That's not prime nor compsite o.O")
    if number != 2:
        if number%2==0:
            print("It's not a prime number.")
        elif number%3==0:
            print("It's not a prime number.")
        else:
            print("It's a prime number.")
    else:
        print("It's a prime number.")

n = int(input("Check this number: "))
prime_checker(number=n)