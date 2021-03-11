x = "i suck"

while x == "i suck":
    input("Welcome to the best rock, paper, scissors game you have ever played! [press enter to continue] ")

    user = input("Please choose your weapon! [rock, paper, or scissors] ")

    if user == "rock":
        bot = "paper"
    elif user == "paper":
        bot = "scissors"
    elif user == "scissors":
        bot = "rock"

    print("Bot chose " + bot + ". You suck!")

    x = input('Type "i suck" to try again or press enter to be a loser! ')
    y = 1
    while y == 1:
        print("hahahaha stupid loser ")
