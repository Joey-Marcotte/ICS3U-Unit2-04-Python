#!/usr/bin/env python3

# Created by: Joey Marcotte
# Created on: September 2019
# This is rectangle math program with variables

import constants


def main():
    # this function calculates the price of a pizza per inch

    # input
    diameter = int(input("Enter diameter of pizza you would like (inch): "))

    # process
    sub_total = constants.LABOR + constants.RENT + \
        (diameter * constants.COST_PER_INCH)
    total = sub_total + (sub_total * constants.HST)

    # output
    print("")
    print("The cost for a {0} inch pizza is: ${1:,.2f}"
          .format(diameter, total))


if __name__ == "__main__":
    main()
