
def find_pairs(lst, x):
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

    for i in range(0, len(lst) - 1):

        for y in range(i + 1, len(lst)):

            if lst[i] + lst[y] == x:

                print(f'({lst[i]}, {lst[y]})')

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE


n = int(input())
s = eval(input())
# you_can_do_it(s, n)

find_pairs(s, n)

