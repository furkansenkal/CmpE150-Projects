
glass_size = int(input())
straw_pos = int(input())

# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE


def space_printer(n):
    if n == 0:
        return
    print(' ', end='')
    space_printer(n - 1)

# This function print spaces n times side by side, and I used it in other functions when needed


def straw_printer(n):
    if n == 0:
        return
    space_printer(straw_pos - n)
    print('o')
    straw_printer(n - 1)

# This function prints the straw's part that above the glass,
# I used space_printer in this function so it is like two nested loops,
# In this function space_printer print spaces starting from zero,
# and increasing one per line at its maximum it prints as much spaces as value of (straw_pos-1).


def stick_printer(n):
    if n == 0:
        return
    space_printer(glass_size)
    if n == glass_size + 1:
        print('--')
    else:
        print('||')
    stick_printer(n - 1)

# This function prints the bottom side of the glass.
# It first prints one '--' and then print as much '||' as value of glass_size.
# Also, before printing them calls space_printer and print as much spaces as value of glass_size in each line.


def star_printer(n):
    if n == 0:
        return
    print('*', end='')
    star_printer(n - 1)

# This function print stars n times side by side, and I used it in other functions when needed


def glass_printer(n, m):
    if n == 0:
        stick_printer(glass_size + 1)
        return
    space_printer(glass_size - n)
    print('\\', end='')
    if m <= 0:
        star_printer(2 * n)
    else:
        space_printer(straw_pos - 1)
        print('o', end='')
        space_printer(2 * n - straw_pos)
    print('/')
    glass_printer(n - 1, m - 1)

# This function serves to completely print a glass.
# In other words, it is printing one element of the large loop when it is called.
# For example, if the loop will consist of 3 elements as as in the case when the inputs are 3 and 4
# This function is called 3 times.
# Variable 'n' determines the number stars (which is 2*n actually) in each row,
# and determines when the function will end
# Variable 'm' determines whether we should print the straw's part in the glass or not,
# and the first value of 'm' determined by the following function (loop_printer).


def loop_printer(n, m):
    if n == 0:
        return
    straw_printer(straw_pos)
    glass_printer(glass_size, m)
    loop_printer(n - 2, m + 1)

# This function calls other functions in the correct order,
# and determines how many times the glass should be printed.
# Variable 'n' determines how many elements (which is actually n/2) the loop consists of.
# Variable 'm' determines how many parts of the straw should be in the glass for each element of loop.
# for example in zeroth element of the loop m=0 and there are only stars in the glass,
# if m=1 in first line of glass there is one 'o' and as many spaces as needed.
# if m=2 first two line of glass consist of 'o' and spaces, and it goes on like that


if (2 * glass_size - straw_pos) % 2 == 0:
    loop_printer(2 * glass_size - straw_pos + 4, 0)
else:
    loop_printer(2 * glass_size - straw_pos + 3, 0)
# This if-else block determines the how many times should loop_printer be called
# when (2 * glass_size - straw_pos) expression is odd or even.
# For instance, if this expression is odd, loop_printer function should work until
# there is one space between the straw's last part and the glass' left side in the last element of the loop.
# But, if it is even, loop_printer function should work until
# there is no space between the straw's last part and the glass' left side in the last element of the loop.
# So, this block allows this situations to happen correctly.

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE

