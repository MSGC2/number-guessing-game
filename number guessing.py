import random

computer_number = random.randint(1, 100)

def is_same(target, number):
    if target == number:
        result="WIN"
    elif target > number:
        result="Low"
    else:
        result="high"
    return result

print("hello.\nI have thought of a number between 1 and 100.")

guess = int(input("can you guess the number?"))

higher_or_lower = is_same(computer_number, guess)

while higher_or_lower != "WIN":
    if higher_or_lower == "Low":
        guess = int(input("Sorry, you are to Low. Try again. "))
    else:
        guess = int(input("Sorry, you are to high. Try again. "))

    higher_or_lower = is_same(computer_number, guess)


input("Correct!\nWell Done\n\n\nPress RETURN to exit.")
