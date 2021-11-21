import random, turtle, time


def man(x=0):
    # Noose
    if x == 1:
        turtle.left(90)
        turtle.penup()
        turtle.forward(150)
        turtle.pendown()
        turtle.forward(60)
        turtle.right(90)
        turtle.forward(125)
        turtle.backward(250)
        turtle.forward(125)
        turtle.right(90)
        turtle.forward(60)
        turtle.left(90)

        # Head
        for i in range(540):
            turtle.right(1)
            turtle.forward(0.8)

        # Body
        turtle.left(90)
        turtle.forward(125)

    if x == 2:
        # Left Leg
        turtle.right(42.5)
        turtle.forward(90)
        turtle.backward(90)

    if x == 3:
        # Right Leg
        turtle.left(85)
        turtle.forward(90)
        turtle.backward(90)

        turtle.right(42.5)
        turtle.backward(85)

    if x == 4:
        # Left Hand
        turtle.right(42.5)
        turtle.forward(80)
        turtle.backward(80)

    if x == 5:
        # Right Hand
        turtle.left(85)
        turtle.forward(80)
        turtle.backward(80)
        time.sleep(1)
        turtle.clearscreen()

    if x == 0:
        time.sleep(1)
        turtle.clearscreen()


# Starting off
print("Would you like to play Hangman?")
ans = input("Enter yes/no here:").upper()

if ans == "NO":
    print("Ok Thanks")
elif ans != "NO" and ans != "YES":
    ans = input("Enter option yes/no:").upper()

while ans == "YES":
    # List of possible words
    Colour = ['AMBER', 'AQUAMARINE', 'AMETHYST', 'AZURE', 'BLACK', 'BROWN', 'BRONZE', 'BURGUNDY', 'CERULEAN', 'BEIGE',
              'CARMINE', 'COPPER', 'CRIMSON', 'CORAL', 'EMERALD', 'GREEN', 'INDIGO', 'ULTRAMARINE', 'MAGENTA', 'MAROON',
              'MAUVE', 'ORANGE', 'PEACH', 'PURPLE', 'SILVER', 'SCARLET', 'TURQUOISE', 'VIOLET', 'WHITE', 'YELLOW',
              'IVORY', 'LAVENDER', 'LILAC', 'SAPPHIRE', 'TAUPE', 'CERISE']

    Flower = ['AMARYLLIS', 'ASTER', 'AZALEA', 'BUTTERCUP', 'CARNATION', 'CHRYSANTHEMUM', 'COSMOS', 'DAFFODIL', 'DAHLIA',
              'PETUNIA', 'DELPHINIUM', 'GARDENIA', 'GERANIUM', 'GLADIOLUS', 'HEATHER', 'HIBISCUS', 'HONEYSUCKLE',
              'HYACINTH', 'IMPATIENS', 'JASMINE', 'LOTUS', 'MAGNOLIA', 'MARIGOLD', 'MAYFLOWER', 'NARCISSUS', 'ORCHID',
              'PANSY', 'PEONY', 'DAISY', 'SNOWDROP', 'SNOWFLAKE', 'SUNFLOWER', 'TULIP']

    Asian = ['AFGHANISTAN', 'ARMENIA', 'BANGLADESH', 'BHUTAN', 'LEBANON', 'CHINA', 'INDIA', 'JAPAN', 'GEORGIA', 'NEPAL',
             'INDONESIA', 'ISRAEL', 'MALAYSIA', 'JORDAN', 'KUWAIT', 'CAMBODIA', 'CYPRUS', 'SYRIA', 'MONGOLIA', 'QATAR'
             'MYANMAR', 'PAKISTAN', 'PALESTINE', 'RUSSIA', 'SINGAPORE', 'MALDIVES', 'TAIWAN', 'THAILAND', 'TURKEY',
             'VIETNAM', 'YEMEN', 'AZERBAIJAN']

    Sport = ['AEROBATICS', 'QUIDDITCH', 'BADMINTON', 'BASEBALL', 'BASKETBALL', 'CANOEING', 'CHEERLEADING', 'CRICKET',
             'CYCLING', 'DODGEBALL', 'FOOTBALL', 'GLIDING', 'GYMNASTICS', 'HANDBALL', 'HIKING', 'HOCKEY', 'KABADDI',
             'SWIMMING', 'LACROSSE', 'ARCHERY', 'RUGBY', 'RUNNING', 'SAILING', 'TENNIS', 'SHOOTING', 'SKATING',
             'SKYDIVING', 'SLEDDING', 'SOCCER', 'SOFTBALL', 'VOLLEYBALL', 'THROWBALL']

    List = {'COLOURS': Colour, 'FLOWERS': Flower, 'ASIAN COUNTRIES': Asian, 'SPORTS': Sport}
    Cat = random.choice(list(List.keys()))  # Picks category
    word = random.choice(List[Cat])  # Picks word respectively
    tries = 0

    # List of letters used and unused
    Letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    # Game starts
    print("\nCategory - ", Cat)
    g = list("_" * len(word))
    for i in g:  # Printing the blanks
        print(i, end=" ")
    print("\n")

    while tries < 5:
        print("Available letters - ", end="")
        for k in Letters:
            print(k, end=" ")
        print()

        x = input("Enter a letter:").upper()

        if x.isalpha():  # Alphabet or number

            if len(x) == 1:  # Single letter or multi-letter

                if x in Letters:  # Used or unused
                    Letters.pop(Letters.index(x))

                    if x in word:  # Presence in word
                        for i in range(len(word)):  # Placing letters in place
                            if g[i] == "_" and word[i] == x:
                                g[i] = x
                    elif x not in word:
                        tries += 1
                        print("Wrong attempts - ", tries)
                        man(tries)
                    for j in g:  # Letters and Blanks
                        print(j, end=" ")
                    print("\n")

                else:
                    print("\nLetter is already used. Enter another letter.")

            else:
                print("\nEnter single letter only.")

        else:
            print("\nInvalid character. Enter a letter.")

        if "_" not in g:  # No more blanks - Win
            print("Yay! You win!", "\n")
            man()
            break

    else:  # Tries over
        print("Answer - ", end="")
        for i in word:  # Actual word
            print(i, end=" ")
        print("\n", "You lose!", "\n")

    # Continuation
    print("Would you like to continue?")
    ans = input("Enter yes/no here:").upper()
    print()
    if ans == "NO":
        print("Ok Thanks")
        break
    elif ans == "YES":
        continue
    else:
        print("Invalid option.")
        ans = input("Enter option again:").upper()
