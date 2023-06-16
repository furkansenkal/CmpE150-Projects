
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
element_number = int(input())
initial_list = []
for i in range(element_number):
    elements = int(input())
    initial_list.append(elements)
if element_number == 0:
    final_list = []
else:
    removed_element = int(input())
    final_list = []
    for j in initial_list:
        if j == removed_element:
            continue
        else:
            final_elements = j * removed_element
            final_list.append(final_elements)

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
print(final_list)
