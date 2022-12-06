# Print "I am a handsome boy" so many times, and if customers type "no", then shutdown the game.

flag = True
while flag:
    print("I am a handsome boy")
    userChoice = input("continue? y means yes n means no")
    if userChoice == 'y':
        pass
    else:
        flag = False
