
glass_size = int(input())
straw_pos = int(input())

# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

loop_num = 2*glass_size-straw_pos+2
# the loop_num variable determines the gap between the glass' last point and straw
# but it is working inversely proportional
# for example, when loop_num equals to 0, the gap is at its maximum value
if loop_num % 2 == 1:
    loop_num -= 1
# If the loop_num variable is an odd number, At the end,There should be no gap between the glass' last point and straw
# but if it is an even number there have to one white space between straw and glass' last point

for counter in range(0, loop_num+2, 2):  # This line is determining the number of states to be drawn

    for straw in range(straw_pos):
        for pipet in range(straw):
            print(' ', end='')
        print('o')
# This loop is drawing the part of straw above the glass

    for glass in range(glass_size):
        for cam in range(glass):
            print(' ', end='')
        print('\\', end='')
# This loop is selecting the point where the glass will start and draws the left hand part of it

        if 2*glass < counter:
            for drink in range(2 * (glass_size - glass)):
                if straw_pos-1 == drink:
                    print('o', end='')
                else:
                    print(' ', end='')
        else:
            for drink in range(2 * (glass_size - glass)):
                print('*', end='')
# This nested if statement is, depending on which state we are in,
# places stars or the piece of straw in the rows inside the glass

        print('/', end='')
        print()
    for glass_bottom in range(glass_size):
        print(' ', end='')
    print('--')
    for glass_bottom2 in range(glass_size):
        for bottom2 in range(glass_size):
            print(' ', end='')
        print('||')

# This part completes the bottom and the right part of the glass

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE


