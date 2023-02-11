def slant_check(matrix,P1,P2):
    empty_lst1 = []
    empty_lst2= []
    lst1 = []
    lst2 = []
    x = len(matrix)
    v = len(matrix) - 1
    t = 0 
    g = 0
    n = True
    while n:
        for i in range(x):
            if matrix[i][i] == P1 or matrix[t][i] == P1:
                empty_lst1.append(matrix[i][i])
            if matrix[i][i] == P2 or matrix[t][i] == P2:
                empty_lst2.append(matrix[i][i])
        while v >= g:
            if matrix[g][v] == P1:
                lst1.append(matrix[g][v]) 
            if matrix[g][v] == P2:
                lst2.append(matrix[g][v])
            t -= 1
            v -= 1
            g += 1
        if len(empty_lst1) == x:
            return True
        if len(empty_lst2) == x:
            return True
        if len(lst1) == x:
            return True
        if len(lst2) == x:
            return True
        return False
def vertical_check(lst,P1,P2):
    for i in range(len(lst) - 2):
        for j in range(len(lst)):
            if lst[i][j] == P1 and lst[i + 1][j] == P1 and lst[i + 2][j] == P1:
                return True
            if lst[i][j] == P2 and lst[i + 1][j] == P2 and lst[i + 2][j] == P2:
                return True
            
    return False
def horizontal_check(lst,P1,P2):
    for i in range(len(lst)):
        for j in range(len(lst) - 2):
            if lst[i][j]== P1 and lst[i][j + 1]== P1 and lst[i][j + 2]== P1 :
                return True
            if lst[i][j]== P2 and lst[i][j + 1]== P2 and lst[i][j + 2]== P2 :
                return True
    return False
def find_grid2(place,lst):
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if place == lst[i][j]:
                return lst.index(lst[i])

def find_grid1(place,lst):
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if place == lst[i][j]:
                return lst[i].index(place)
            
def print_lst(lst):
    for i in range(len(lst)):
        for j in range(len(lst[i]) - 2):
            print(lst[i][j],'|', lst[i][j + 1],'|', lst[i][j + 2])
            print('----------')
def tic_tac_toe():
    lst = [[1,2,3],
           [4,5,6],
           [7,8,9]]
    P1 = 0
    P2 = 0
    counter_loop = 0
    _ = 0 
    new_lst = [1,2]
    while True:
        P1 = input('Player1 select "x" or "o" ? (Type in x or o):\n').lower()
        if P1 == 'x':
            print('Player2 is now "o"!\n')
            P2 = 'o'
            break
        if P1 == 'o':
            print('Player2 is now "x"!\n')
            P2 = 'x'
            break
        else:
            print('Try Again\n')
    print_lst(lst)
    while _ < len(lst): 
        for i in range(len(lst[_])):
            if counter_loop == 9:
                print("Tie!")
                break
            place_grid1 = input('Where would Player 1 like to place? : ')
            if int(place_grid1) >= 10 or int(place_grid1) <= 0:
                print('Try Again')
                place_grid1 = input('Where would Player 1 like to place? : ')
                break
            place_grid = int(place_grid1)
            counter_loop += 1
            inner_index1 = find_grid1(place_grid,lst)
            outer_index1 = find_grid2(place_grid,lst)
            lst[outer_index1][inner_index1] = P1
            print_lst(lst)
            if horizontal_check(lst,P1,P2) == True:
                print("Player 1 wins!!")
                counter_loop = 9 
                break
            if vertical_check(lst,P1,P2) == True:
                print("Player 1 wins!!")
                counter_loop = 9 
                break
            if slant_check(lst,P1,P2) == True:
                print("Player 1 wins!!")
                counter_loop = 9 
                break
            if counter_loop == 9:
                print("Tie!")
                break
            place_grid2 = input('Where would Player 2 like to place? : ')
            if int(place_grid2) >= 10 or int(place_grid2) <=0:
                print('Try Again')
                place_grid2 = input('Where would Player 2 like to place? : ')
                break
            place_gridy = int(place_grid2)
            counter_loop += 1
            inner_index2 = find_grid1(place_gridy,lst)
            outer_index2 = find_grid2(place_gridy,lst)
            lst[outer_index2][inner_index2] = P2
            print_lst(lst)
            if horizontal_check(lst,P1,P2) == True:
                print("Player 2 wins!!")
                counter_loop = 9 
                break
            if vertical_check(lst,P1,P2) == True:
                print("Player 2 wins!!")
                counter_loop = 9 
                break
            if slant_check(lst,P1,P2) == True:
                print("Player 2 wins!!")
                counter_loop = 9 
                break
            if counter_loop == 9:
                print("Tie!")
                break        
        if counter_loop == 9:
            break
        
        _ += 1

    
tic_tac_toe()