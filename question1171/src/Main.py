
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
def find_actions(given_board, max_actions, given_board_lst=[],actionlst=[],hamlecounter=0):
    target_board = '123\n456\n789'
    target_board_lst = []

    for i in range(3):
        target_board_lst.append(list(str(target_board.split('\n')[int(i)])))
    for i in range(3):
        given_board_lst.append(list(str(given_board.split('\n')[int(i)])))
    # converting boards to 2d lists
    for i in range(0,len(given_board_lst)-1):

        for j in range(len(given_board_lst[int(i)])-1):
            if given_board_lst[int(i)][int(j)]==target_board_lst[int(i)][int(j)]:
                continue
            #Checking given boards each element left to right if it is same with target boards element it continues
            else:
                if given_board_lst[int(i)][int(j)] == target_board_lst[int(i)][int(j)+1]:
                    actionlst.append(f'move {given_board_lst[i][j]} right'),
                    hamlecounter+=1
                    # If given boards elements is not in the same location at target boards element it trys to find it in row
                    # If it finds the element hamlecounter increases by 1 and if appends move tile right to action list
                if given_board_lst[int(i)][int(j)] == target_board_lst[int(i)+1][int(j)]:
                    actionlst.append(f'move {given_board_lst[i][j]} down')
                    hamlecounter+=1
                    #Denedim olmadı hocam:(
    if hamlecounter > max_actions:
        print([])
        return
    else:
        print(actionlst)
        return





# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE

line1 = input()
line2 = input()
line3 = input()
given_board = line1+'\n'+line2+'\n'+line3

max_actions = int(input())

solution = find_actions(given_board,max_actions)

print(solution)

