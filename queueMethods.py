def addPlayer(myQueue):
    name = input("Enter a name: ")
    if name in myQueue:
        print(name + " is already in the queue")
        print("Current queue", myQueue)
    else:
        myQueue.append(name)
        print("Congratulations! " + name + " is added in the queue successfully")
        print("Current queue", myQueue)



def removePlayer(myQueue):
    served_player = myQueue.pop(0)
    print(served_player + " is finished the ride and now removed from the queue, thank you!")
    print("The next players: ", myQueue)
