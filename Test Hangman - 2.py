import random, Man
import mysql.connector as sql


def highscore(score):

    def checked(un="", flag=0):  # Flag to determine if value to be row to be deleted
        if un == "":
            un = "Alpha"
        cur.execute("INSERT INTO {} VALUES('{}', {})".format(tn, un, score))  # Inserting new high score
        mydb.commit()
        if flag != 0:
            # Removing lowest score
            cur.execute("DELETE FROM {} WHERE NAME = '{}' AND SCORE = {}".format(tn, lowest[0], lowest[-1]))
            mydb.commit()

    # Connecting to MySQL server
    print("Your score -", score)
    mydb = sql.connect(host="localhost", user="root", password="<insert_password_here", database="Hangman")
    cur = mydb.cursor()

    levels = {'1': 'EASY', '2': 'MEDIUM', '3': 'HARD'}  # Difficulty and table name
    tn = levels[dif]  # Obtaining table name
    cur.execute("SELECT * FROM {} ORDER BY SCORE DESC".format(tn))  # Obtaining all scores
    res = cur.fetchall()
    if len(res) == 5:  # Checking if table is filled
        lowest = res[-1]
        if score >= lowest[-1]:  # Checking if sore more than lowest
            while True:
                name = input("Enter your name:").upper()
                if len(name) <= 20:  # Validating name according to table requirements
                    break
                else:
                    print("Name must be less than 20 characters.")
            checked(name, 1)  # All conditions satisfied update table
    else:
        while True:
            name = input("Enter your name:").upper()
            if len(name) <= 20:  # Validating name according to table requirements
                break
            else:
                print("Name must be less than 20 characters.")
        checked(name)  # All condition satisfied update table

    # Displaying all high scores
    cur.execute("SELECT * FROM {} ORDER BY SCORE DESC".format(tn))  # Displaying all scores
    res = cur.fetchall()
    print()
    print("{:^28}".format("HIGH SCORES"), "\n{:<22}{:<6}".format("NAME", "SCORE"), "\n{:-^28}".format(""))
    for i in res:
        print("{:<22}{:<6}".format(i[0], i[1]))


def instructions():
    print(''' 
Instructions
1. Enter letters one at a time on prompt to guess the word.
2. If the letter is correct it will be displayed.
3. If the letter is wrong a screen will open and begin drawing a man.
4. You will have 6 tries at the beginning of each round. Each failed guess
   will lead to a loss of a point. The number of tries left at the end of
   the round is your score for that round.
5. The game ends when all 6 points(tries) have been lost.
''')


# Pick difficulty
def difficulty(flag=1):  # Flag value to show appropriate dialogue
    if flag == 1:  # Difficulty options
        instructions()
        print('''\nWelcome to Hangman. 
Begin by choosing difficulty. 
Enter: 1 - Easy
       2 - Medium
       3 - Difficult''')
    else:
        print("Invalid choice.\n")

    global dif  # Difficulty to be accessible to word picking function
    dif = input("Enter choice of difficulty here:")
    if dif in ['1', '2', '3']:
        game()  # Proceeding to the game
    else:
        difficulty(flag=0)  # Function recurs till choice made is valid


# Start dialogue
def begin(flag=1):  # Parameter to check condition for call and display appropriate dialogue
    if flag == 1:
        print("Hello. Would you like to play hangman??")
    else:
        print("Invalid choice.\n")

    ans = input("Enter YES or NO - ").upper()  # User enters choice here
    if ans == 'NO':
        print("Ok. Thank you.")
    elif ans == 'YES':
        difficulty()  # Proceeding to next step - picking difficulty level
    else:
        begin(flag=0)  # Function recurs till choice made is valid


# Word picker
def wordpick():
    # difficulty = {Category: File}
    easy = {'COLOURS': "Colours.txt", 'ANIMALS': "Animals.txt"}
    med = {'JOBS AND OCCUPATIONS': "Jobs.txt", 'FLOWERS': "Flowers.txt"}
    hard = {'AUTHORS': "Authors.txt", 'LANGUAGES': "Languages.txt"}
    levels = {'1': easy, '2': med, '3': hard}

    cat = random.choice(list(levels[dif].keys()))  # Picks category
    with open(levels[dif][cat], "r") as f:  # Opens file to access words
        w = f.readlines()
        word = random.choice(w)  # Picks word from entire list

    return cat, word.rstrip()


# Next level
def advance(score, flag=1):  # Score carries forward total points from each round
    if flag == 1:  # Flag checks condition for call
        print("\nWould you like to continue?")
    else:
        print("Invalid choice.")

    ans = input("Enter YES or NO - ").upper()  # User enters choice here
    if ans == 'NO':  # Displays final score
        highscore(score)
        print("Ok. Thank you.")  # Quits the game
    elif ans == 'YES':
        game(score)  # Carries forward the score
    else:
        advance(score, flag=0)  # Function recurs till choice made is valid


# Begins the game
def game(score=0):  # Default score is zero
    # Set up base
    letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")  # Creating list of letters
    cat, word = wordpick()  # Obtaining category and word
    word = list(word)  # Creating a list of word
    dash = ["_" if not i.isspace() else " " for i in word]  # List for dashes
    tries = 6  # Number of tries

    print("\nCategory -", cat)
    print(*dash)

    while tries > 0:
        print("\nLetters available -", *letters)
        x = input("Enter a letter:").upper()  # Standardising input

        ''' Validating the input
            Ensuring only single letters are entered. 
            Checking if letter is already used.
            If all conditions satisfied. Checking for letter in word'''

        if x.isalpha():
            if len(x) == 1:
                if x in letters:
                    letters.remove(x)  # Removing letters being input if not already used

                    if x in word:  # Checking for presence of letter in word
                        # Replacing dash with corresponding letter
                        dash = [dash[i] if word[i] != x else x for i in range(len(dash))]

                    else:
                        tries -= 1  # Wrong guesses
                        Man.man(tries)  # Drawing man

                    print(*dash)

                else:
                    print("Letter already used.")
            else:
                print("Enter one letter at a time.")
        else:
            print("Only letters to be entered.")

        if "_" not in dash:  # Checking if all letter guessed
            score += tries  # Adding points to total score
            print("Congratulations! You got the word!\n")
            print("Your score -", score)
            advance(score, flag=1)  # Moving to next word
            break  # Breaking loop when word guessed

    else:  # All guesses over
        print("Answer -", "".join(word), "\nBetter luck next time.\n")
        highscore(score)


# Main
begin()
