


def power(b, e):
    # DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

    if e == 0:
        return 1

    elif e == 1:
        return b

    if b == 0 and e < 0:
        return 0

    else:
        if e < 0:
            return 1/(b * power(b, - e - 1))
        return b * power(b, e - 1)

    # DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE


input_base = float(input())
input_exponent = int(input())

print("{:.4f}".format(power(input_base, input_exponent)), end="")

