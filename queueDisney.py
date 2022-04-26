from queueMethods import addPlayer, removePlayer


def main():
    # Initializing a queue
    myQueue = ['Peter', 'Ann']

    print('Welcome to Disney rides menu. Please select the menu')
    print("Current queue: ", myQueue)

    loop = True

    while loop:
        print('[1] - Add a player in the queue')
        print('[2] - Serve the next player in the queue')
        print('[3] - Show the queue')
        print('[4] - Look up a player')
        print('[5] - Exit the menu')
        selectors = input("Enter a number from 1-5: ")

        if selectors == '1':
            # call the method to add a player in the queue
            addPlayer(myQueue)
        elif selectors == '2':
            # call a method to remove a player from the queue
            removePlayer(myQueue)
        elif selectors == '3':
            # call a method to show the queue
            showQueue(myQueue)
        elif selectors == '4':
            # call a method to look up if the player is in the queue
            lookUpPlayer(myQueue)
        elif selectors == '5':
            quit()
        else:
            print("Invalid")
    #loop = input("Continueues? y/n: ")

main()
