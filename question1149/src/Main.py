
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
b_string = input()


def functione(b_string,count=0):
    for i in b_string:
        if i == '0' or i == '1':
            continue
        else:
            print('This is not a binary string')
            return
    liste = b_string.split('0')
    for i in liste:
        if len(i) < count:
            continue

        else:
            count = len(i)
    print(count)

functione(b_string)



# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE

