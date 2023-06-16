
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

def sum_list(lst):

    if len(lst) == 0:
        return 0

    if type(lst[0]) == list:
        my_lst = sum_list(lst[0])
        return my_lst + sum_list(lst[1:])

    else:
        try:
            return lst[0] + sum_list(lst[1:])
        except:
            return sum_list(lst[1:])

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE

# converts the input string to list.
lst = eval(input())
print(sum_list(lst))

