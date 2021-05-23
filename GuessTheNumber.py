from random import randint

random_number = randint(1, 100)

print(random_number)

user_guess = input("Enter a number between 1 and 100: ")

if type(user_guess) == int:
    print("yes")
    user_guess = int(user_guess)



while user_guess != random_number and type(user_guess) == int:
    #if user_guess != random_number:
    if user_guess > random_number:
        print("Too high!")
        user_guess = input("Enter a number between 1 and 100: ")
        user_guess = int(user_guess)
    else:
        print("Too low!")
        user_guess = input("Pick a number between 1 and 100: ")
        user_guess = int(user_guess)


if user_guess == random_number:
    print("Correct!")

m = 16

m = "this2009"
print(m.isnumeric())

