#program that automatically prints the solution to the fizzbuzz game from 0 to 100

for number in range(1,101):
    if number%5 == 0 and number%3 == 0:
        print("FizzBuzz")
    elif number%5 == 0:
        print("Buzz")
    elif number%3 == 0:
        print("Fizz")
    else:
        print(number)