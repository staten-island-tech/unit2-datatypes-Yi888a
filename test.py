#bill = input("Bill please. ")
#bill = float(bill)
#tip = int(tip)
#if tip == 0:
	#print(f"You're too cheap. Your total is {bill + tip}")
#else :
    #print(f"Your total is {bill + tip}")

#bill = float(input("Bill please. "))
#User_input = input("How was your service? Bad, Ok, Good, Great? ")
#if User_input == "Bad":
  #  tip = bill * 0.00
#elif User_input == "Ok":
   # tip = bill * 0.15
#elif User_input == "Good":
   # tip = bill * 0.20
#elif User_input == "Great":
  #  tip = bill * 0.25
#else:
   # tip = 0
#print(f"Your tip is {tip}, and your total is {bill + tip}")

#import math
#def gcf(a, b):
    #return math.gcd(a, b)
#user_input = input("input two numbers, separated by a comma. ")
#num1 = int(user_input.split(",")[0])
#num2 = int(user_input.split(",")[1])
#print(gcf(num1, num2))

#def factor():
    #factors = []
    #number = int(input("What number do you want to factor? "))
    #for i in range(1, number + 1):
       # if number % i == 0:
       #     factors.append(i)
 #   print(factors)

#factor()

#def odd_even():
   # number = int(input("What number do you want to check? "))
    #if number % 2 == 0:
        #print("Even")
  #  else:
       # print("Odd")
#odd_even()

def guess_number():
    import random
    number = random.randint(1, 10)
    guess = int(input("Guess a number between 1 and 10. "))
    while guess != number:
        if guess < number:
            print("Too low.")
        else:
            print("Too high.")
        guess = int(input("Guess again. "))
    print("Correct!")
guess_number()