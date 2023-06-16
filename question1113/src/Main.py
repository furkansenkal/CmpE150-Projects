
number = int(input())

# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
number_list = []
num = str(number)
for i in num:
    i = int(i)
    number_list.append(i)
dict_final = dict()
if number > 99999:
    for n in number_list:
      try:
        dict_final[n] = dict_final[n] + 1
      except:
        dict_final[n] = 1

elif number < 100000:
    for n in number_list:
      try:
        dict_final[n] = dict_final[n] + 1
      except:
        dict_final[n] = 1

    bigcount = None
    bigdigit = None
    for digit, count in dict_final.items():
        if bigcount is None or count > bigcount:
            bigdigit = digit
            bigcount = count
    dict_final = {bigdigit: bigcount}




# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
        
for i in range(10):
    if i in dict_final:
        print(i, '->', dict_final[i])

