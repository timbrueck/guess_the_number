import random
import string

attempt = 0
score = 0    
attempts_left = 3

print("Welcome")
print("Whats your upper border?")
print("Remember, when your upper border is > 30 you will have only 15 tries")
upper_border = int(input(" "))

while(True):
    number = random.randint(1, int(upper_border))
    print("Whats the number?")
    i = int(input(" "))
    
    if upper_border < 10 or upper_border == 10:
        number_from_attempt = 3
    elif upper_border > 10 and upper_border < 20 or upper_border == 20:
        number_from_attempt = 6
    elif upper_border < 20 and upper_border > 30 or upper_border == 30:
        number_from_attempt = 10
    
    else:
        number_from_attempt = 15


    if i == number:
        print("You are right")
        score += 1
    else:
        print("You are wrong!")
        attempt += 1
        attempts_left = int(number_from_attempt) - attempt
        print("Attemps left: " + str(attempts_left))

    if attempts_left == 0 or i == number:
        print("The number was " + str(number))
        break

