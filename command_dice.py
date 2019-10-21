"""Command line tool for rolling dice"""

# Built In
import operator
import random
import re
import sys


def handle_modifier(total, modifier):
    """Take total for dice roll and modify based on input, return result"""
    lookup = {"+": operator.add, "-": operator.sub}
    if modifier is not None:
        # Modifier will look like `+X` or `-X`
        return lookup[modifier[0]](total, int(modifier[1:]))

    return total


def roll_dice(inp=None):
    """Roll given number of dice of given value"""
    try:
        inp = inp if inp is not None else sys.argv[1]
    except IndexError:
        print("Please provide how many dice of what value you'd like to roll... e.g 1d20")
        return

    # Pattern matches a roll as the first group, followed by a modifier as the second group
    match = re.match(pattern=r"([1-9]\d*[d][1-9]\d*)([+-][1-9]\d*)?", string=inp)
    if match:
        roll, modifier = match.groups()  # Split input into the two groups
        quantity, value = roll.split("d")  # Roll is formatted as `QUANTITY`d`VALUE`

        # roll `quantity` of dice with `value` number of sides
        rolls = [random.randint(1, int(value)) for dice in range(1, int(quantity) + 1)]

        msg = ""
        if len(rolls) > 1:  # If more than 1 dice is rolled, do a bit of formatting
            msg += "Dice:"
            for r in rolls:
                msg += f" {r},"  # Add each dice roll to the message
            msg = msg.rstrip(",")  # Strip the final comma

            # Add the total at the end with modifier
            msg += f"\nTotal: {handle_modifier(total=sum(rolls), modifier=modifier)}"

            if len(rolls) > 2:  # If 3 or more dice were rolled, show lowest and highest
                unique = sorted(list(set(rolls)))
                msg += f" (▼ {unique[0]} ▲ {unique[-1]})"

        else:  # Otherwise only one dice was rolled
            msg = handle_modifier(rolls[0], modifier)

        print(msg)

    else:
        print(f"{inp} does not match expected formatting, "
              "please use QUANTITYdVALUE(+/-)MODIFIER(optional) format.\n"
              "For example 1d20+3 to roll a single twenty sided dice with a "
              "plus three modifier.")


if __name__ == "__main__":
    roll_dice()
