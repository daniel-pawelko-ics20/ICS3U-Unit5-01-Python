#!/usr/bin/env python3

# Created by: Daniel Pawelko
# Created on: Jan 2022
# Functions and what not


def fahrenheit():
    # function to convert celsius to fahrenheit

    # input/process/output
    try:
        # input
        celsius = input("Enter a temperature (°C): ")
        celsius = float(celsius)

        # process
        tf = (9 / 5) * celsius + 32

        # output
        print(f"{celsius}°C is equal to {round(tf, 2)}°F.")
    except:
        print("Please input a number")


def main():
    # main function for function program

    # calling fahrenheit function
    fahrenheit()

    # done
    print("")
    print("Done.")


if __name__ == "__main__":
    main()
