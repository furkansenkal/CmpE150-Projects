
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
x = int(input())
y = int(input())
asal_list = []
for num in range(x, y + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            asal_list.append(num)
if asal_list == []:
    print('No prime numbers found.')
else:
    for j in asal_list:
        print(j, 'is a prime number!')

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE

