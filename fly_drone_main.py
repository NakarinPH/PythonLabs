# Nakarin Philangam
# 01/25/2022

from drone import Drone

drone = Drone()


def main():
    user_input = '1', '2', '3', '4'

    while user_input:

        # Promp the user for an input
        user_input = input("Enter 1 for accelerate, 2 for decelerate, 3 for ascend, 4 for for descend, 0 to exit: ")

        if user_input == '1':
            drone.accelerate()
            print("Speed: %-5.0f" % drone.speed + "Height: %-5.0f" % drone.height)
        elif user_input == '2':
            drone.decelerate()
            print("Speed: %-5.0f" % drone.speed + "Height: %-5.0f" % drone.height)
        elif user_input == '3':
            drone.ascend()
            print("Speed: %-5.0f" % drone.speed + "Height: %-5.0f" % drone.height)
        elif user_input == '4':
            drone.descend()
            print("Speed: %-5.0f" % drone.speed + "Height: %-5.0f" % drone.height)
        elif user_input == '0':
            exit()
        else:
            print("Invalid input")
            continue


if __name__ == "__main__":
    main()
