"""Command line tool for rolling dice"""

# Built In
import random
import re
import sys


def roll(inp):
    """Check if a given input matches pattern dice roll pattern"""
    if re.match(pattern=r"[1-9]\d*[d][1-9]\d*", string=inp):
        quantity, value = inp.split("d")  # Will be formatted as `QUANTITY`d`VALUE`

        # roll `quantity` of dice with `value` number of sides
        rolls = [random.randint(1, int(value)) for dice in range(1, int(quantity) + 1)]

        msg = ""
        if len(rolls) > 1:  # If more than 1 dice is rolled, do a bit of formatting
            msg += "Dice:"
            for r in rolls:
                msg += f" {r},"  # Add each dice roll to the message

            msg = msg.rstrip(",")  # Strip the final comma
            msg += f"\nTotal: {sum(rolls)}"  # Add the total at the end

            if len(rolls) > 2:  # If 3 or more dice were rolled, show lowest and highest
                unique = sorted(list(set(rolls)))
                msg += f" (▼ {unique[0]} ▲ {unique[-1]})"

        else:  # Otherwise only one dice was rolled
            msg = rolls[0]

        print(msg)

    else:
        print(f"{inp} does not match expected formatting, "
              "please use QUANTITYdVALUE format. "
              "For example 1d20 to roll a single twenty sided dice")

if __name__ == "__main__":
    try:
        roll(sys.argv[1])
    except IndexError:
        print("Please provide how many dice of what value you'd like to roll... e.g 1d20")
