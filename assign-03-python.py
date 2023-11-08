#!/usr/bin/env python3
# Created by: Alex M
# Created on: Oct. 11, 2023
# This program gets user input and checks if its within the limits of canadian roller coaster park.
import constants


def main():
    print("Hello fellow human, welcome to canada's wonderland roller coaster")
    print(
        "To ride the roller coaster, we need your your height and weight to be within the limits "
    )
    str_user_height = input(" Enter your height in meters ")
    str_user_weight = input(" Enter your weight in pounds ")

    try:
        flo_user_height = float(str_user_height)
        flo_user_weight = float(str_user_weight)
    except ValueError:
        print("invalid input, enter weight in pounds and height in meters.")
    else:
        if (
            flo_user_height > constants.MAX_HEIGHT
            and flo_user_height < constants.MIN_HEIGHT
            and flo_user_weight > constants.MAX_WEIGHT
            and flo_user_weight < constants.MIN_WEIGHT
        ):
            print("you cant get on the roller coaster. sorry:) ")
        if flo_user_weight >= constants.OBESE:
            print("")
            print(" DAYM!! you cannot ride this ")
        elif (
            flo_user_height < constants.MAX_HEIGHT
            and flo_user_height > constants.MIN_HEIGHT
            and flo_user_weight < constants.MAX_WEIGHT
            and flo_user_weight > constants.MIN_WEIGHT
        ):
            print("You can get on the roller coaster, have fun")
        else:
            print("you cant get on the roller coaster. sorry:) ")
    finally:
        print("thank you for visiting. :) ")


if __name__ == "__main__":
    main()
