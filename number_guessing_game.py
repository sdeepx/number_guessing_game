import random

secret_no = random.randint(1,15)

guess_co = 0
guess_no = 0
guess_li = 6
out_of_guess = False
print(" ")
print("Enter A Guess Number Between 1 - 15 -- \n")
while guess_no != secret_no and not(out_of_guess):
    if guess_co < guess_li:

        try:
            guess_no = int(input("Enter your guess number : "))
            print(" ")

            if guess_no < 1 or (guess_no > 15):
                print("[+] you have to enter a number between 1 and 15 \n")
            else:
                if secret_no > guess_no:
                    print("Your guess is too low.")
                elif secret_no < guess_no:
                    print("Your guess is too high.")
                guess_co +=1
                if guess_no != secret_no and not(out_of_guess):
                    print("you have only", guess_li - guess_co, "chances \n")
                else:
                    print("WOW! nice. You have more", guess_li - guess_co,"chances but you did it.. :) ")


        except:
            print("[-] invalid input. Sorry you have to enter a number.")
    else:
        out_of_guess = True

if out_of_guess:
    print("Sorry! you lose the game \n")
    print("The secret number was",secret_no)
else:
    print("You win the game!")
