
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
initial_amount = int(input())
interest_rate = float(input())
duration = int(input())
total_amount = initial_amount * (1 + interest_rate / 100) ** duration
# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
print("{:.2f}".format(total_amount))

