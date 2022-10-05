#!/usr/bin/env python3

# Created By: Jessah
# Date: Oct 5, 2022
# This program calculates tax and total when given subtotal.
# Using British Columbia taxes


def main():

    # Get subtotal from user

    subtotal = float(input("Enter the subtotal: "))

    # Calculate the tax and total with BC tax rate and user given subtotal
    # 0.12 is when GST and PST are added together

    tax = subtotal * 0.12
    total = subtotal + tax

    # Display the output for the tax and total

    print("")
    print("The tax is: ${:.2f}".format(tax))

    print("")
    print("The total including tax is: ${:.2f}".format(total))


if __name__ == "__main__":
    main()
