'''
random module --> helps to generate random values


import random,time
#random number generation --> OTP (time module hepls to use time functions)
a = random.randint(1000,9999)
#print(a)
for i in range(5):
    time.sleep(2)  # sleep(seconds) --> hepls for a waiting period 
    print(random.randint(1000,9999))
    #time.sleep(2)


import random
player1 = input("enter one of these --> rock,paper,scissors").lower().strip()
player2 = random.choice(["rock","paper","scissors"]).lower()
#print(player1)
#print(player2)

if player1 == "rock" and player2 =="scissors":
    print("player2 won")
elif player1 == "paper" and player2 == "scissors":
    print("player2 won")
elif player1 == player2:
    print("tie")
elif player1 == "rock" and player2 == "paper":
    print("player2 won")
else:
    print("player1 won")

#get the score for each user and declare the winner
#play the game for 10 times --> task (push to github and share it (tasks))
#task2 --> give user a choice --> rps(1)/ng(2)/study(3)/any number no choice only 1,2,3 --> function

import random

comp = random.randint(0,10)
print("----------------------------------------------------------")
print("---------------------Guess The Number---------------------")
print("----------------------------------------------------------")
user = int(input("Enter the number(0-10): "))

if comp == user:
    
    print(f"{comp} and {user}\n U won!..........")
else:
    print(f"{comp} and {user}\nU lost \n/'better luck next time.../'")

import random
s1=0
s2=0
t = 0
for i in range(10):
    player1 = input('Enter one of these --> rock,paper,scissors:').lower().strip()
    player2 = random.choice(['rock','paper','scissors']).lower()

    
    if player1 == 'rock' and player2 =='paper':
        print('player2 won')
        s2=s2+1
    elif player1 == 'paper' and player2 =='scissors':
        print('player2 won')
        s2=s2+1
    elif player1 == 'scissors' and player2 == 'rock':
        print('player2 won')
        s2=s2+1
    elif player1 == player2:
        print('Tie')
        t = t+1
    else:
        print('player1 won')
        s1=s1+1

print(f'score of player 1 is :{s1}')
print(f'score of player 2 is :{s2}')
print(f'tie for {t} times')
if s1 > s2:
    print('Player 1 won the game')
else:
    print('player 2 won the game')


import random
when = ['a long back','once upon a time','few years ago']
who = ['devara','king in the france','barbie queen']
what = ['A magical Sword','Powerful Hammer','Unlimted Arrows']
where = ['Far in the Galaxy','End of Ocean','in India']
how = ['War stared', 'Both fought for 15days','Sad Ending']

#to create a story --> link when to what or who to how....
print(random.choice(when) + " " +random.choice(who))

#buisness card generator --> name,email,mobile number,website link
#segno --> pip install segno


import segno
print(dir(segno))
from segno import helpers
qr = helpers.make_mecard(name="harsha",
                         email="ponnadaindia2005@gmail.com",
                         phone = " +91 8500620018",
                         url = "https://www.linkedin.com/in/venkata-sri-harsha-vardhan-ponnada-b47170430/")
print(qr)
qr.save("mycard.png",scale=10)

# now its your turn --> explore modules
instagram,youtube,email automation ....


#build a virtual assistant using python --> virutal environment
#speak,respond back,greet you,make a conversation,open browser
#locate google maps,tell a story,play a game....
#pop --> functions,control block....

'''
'''
import random


def rps():
    print("\n--- Rock Paper Scissors ---")

    choices = ["rock", "paper", "scissors"]

    player = input("Enter rock, paper or scissors: ").lower()
    player2 = random.choice(choices)

    print("player2:", player2)

    if player not in choices:
        print("Invalid choice")

    elif player == player2:
        print("It's a tie!")

    elif (player == "rock" and player2 == "scissors") or \
         (player == "paper" and player2 == "rock") or \
         (player == "scissors" and player2 == "paper"):
        print("You win!")

    else:
        print("player2 wins!")


def number_guessing():
    print("\n--- Number Guessing Game ---")

    number = random.randint(1, 10)

    guess = int(input("Guess a number between 1 and 10: "))

    if guess == number:
        print("You guessed correctly!")

    else:
        print("Wrong guess!")
        print("Correct number is:", number)


def study():
    print("\n--- Study ---")
    print("Time to study Python!")
    print("Practice coding every day.")


# Main menu
print("===== MENU =====")
print("1. RPS")
print("2. Number Guessing")
print("3. Study")

choice = int(input("Enter your choice: "))

if choice == 1:
    rps()

elif choice == 2:
    number_guessing()

elif choice == 3:
    study()

else:
    print("No choice available")
'''
import random

def rps():
    print("\n--- Rock Paper Scissors ---")

    choices = ["rock", "paper", "scissors"]

    player1_score = 0
    player2_score = 0

    for i in range(5):
        print("\nRound", i + 1)

        player1 = input("Enter rock, paper or scissors: ").lower()
        player2 = random.choice(choices)

        print("Player 2:", player2)

        if player1 not in choices:
            print("Invalid choice")

        elif player1 == player2:
            print("It's a tie!")

        elif (player1 == "rock" and player2 == "scissors") or \
             (player1 == "paper" and player2 == "rock") or \
             (player1 == "scissors" and player2 == "paper"):
            print("player1 win!")
            player1_score += 1

        else:
            print("Player2 wins!")
            player2_score += 1

    print("\n--- Final Score ---")
    print("player1 score:", player1_score)
    print("Player2 score:", player2_score)

    if player1_score > player2_score:
        print("player1 won the game!")

    elif player1_score < player2_score:
        print("Player2 won the game!")

    else:
        print("Game is a tie!")


#rps()
def number_guessing():
    print("\n--- Number Guessing Game ---")

    number = random.randint(1, 10)

    guess = int(input("Guess a number between 1 and 10: "))

    if guess == number:
        print("You guessed correctly!")

    else:
        print("Wrong guess!")
        print("Correct number is:", number)


def study():
    print("\n--- Study ---")
    print("Time to study Python!")
    print("Practice coding every day.")


# Main menu
print("===== MENU =====")
print("1. RPS")
print("2. Number Guessing")
print("3. Study")

choice = int(input("Enter your choice: "))

if choice == 1:
    rps()

elif choice == 2:
    number_guessing()

elif choice == 3:
    study()

else:
    print("No choice available")
