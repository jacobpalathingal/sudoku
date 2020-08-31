// TEST GIT CHANGES
with open("C:/Users/palat/Documents/sudoku.txt.txt") as sudoku:
    A=[line.split() for line in sudoku]

l=([list(map(int,i))for i in A])


dc=[row[:] for row in l]

for i in range (9):
    for j in range (9):
        if dc[i][j] == 0:
            dc[i][j]= [1,2,3,4,5,6,7,8,9]
        else:
            dc[i][j]=[dc[i][j]]


def run():
    print(dc[0])
    print(dc[1])
    print(dc[2])
    print(dc[3])
    print(dc[4])
    print(dc[5])
    print(dc[6])
    print(dc[7])
    print(dc[8])

unit1=[dc[0][0],dc[0][1],dc[0][2],dc[1][0],dc[1][1],dc[1][2],dc[2][0],dc[2][1],dc[2][2]]
unit2=[dc[0][3],dc[0][4],dc[0][5],dc[1][3],dc[1][4],dc[1][5],dc[2][3],dc[2][4],dc[2][5]]
unit3=[dc[0][6],dc[0][7],dc[0][8],dc[1][6],dc[1][7],dc[1][8],dc[2][6],dc[2][7],dc[2][8]]
unit4=[dc[3][0],dc[3][1],dc[3][2],dc[4][0],dc[4][1],dc[4][2],dc[5][0],dc[5][1],dc[5][2]]
unit5=[dc[3][3],dc[3][4],dc[3][5],dc[4][3],dc[4][4],dc[4][5],dc[5][3],dc[5][4],dc[5][5]]
unit6=[dc[3][6],dc[3][7],dc[3][8],dc[4][6],dc[4][7],dc[4][8],dc[5][6],dc[5][7],dc[5][8]]
unit7=[dc[6][0],dc[6][1],dc[6][2],dc[7][0],dc[7][1],dc[7][2],dc[8][0],dc[8][1],dc[8][2]]
unit8=[dc[6][3],dc[6][4],dc[6][5],dc[7][3],dc[7][4],dc[7][5],dc[8][3],dc[8][4],dc[8][5]]
unit9=[dc[6][6],dc[6][7],dc[6][8],dc[7][6],dc[7][7],dc[7][8],dc[8][6],dc[8][7],dc[8][8]]

def check_row(x):
    count=0
    row_changed = False
    while count<9:
        if (len(dc[x][count]) == 1):
            for num in range (9):
                if (len(dc[x][num])!=1 and dc[x][count][0] in dc[x][num]):
                    dc[x][num].remove(dc[x][count][0])
                    row_changed = True
        count=count+1
    return row_changed

def check_col(x):
    count=0
    col_changed = False
    while count<9:
        if (len(dc[count][x]) == 1):
            for num in range (9):
                if (len(dc[num][x])!=1 and dc[count][x][0] in dc[num][x]):
                    dc[num][x].remove(dc[count][x][0])
                    col_changed = True
        count=count+1 
    return col_changed
  
def check_unit(x):
    if x == 1:
        unit=unit1
    if x == 2:
        unit=unit2
    if x == 3:
        unit=unit3
    if x == 4:
        unit=unit4
    if x == 5:
        unit=unit5
    if x == 6:
        unit=unit6
    if x == 7:
        unit=unit7
    if x == 8:
        unit=unit8
    if x == 9:
        unit=unit9
    count=0
    unit_changed = False
    while count<9:
        if (len(unit[count]) == 1):
            for num in range (9):
                if (len(unit[num])!=1 and unit[count][0] in unit[num]):
                    unit[num].remove(unit[count][0])          
                    unit_changed = True
        count=count+1    



def check_all_rows():
    row_changes = False
    for row in range(9):
        if check_row(row):
            row_changes = True
    return row_changes

def check_all_cols():
    col_changes = False
    for col in range(9):
        if check_col(col):
            col_changes = True
    return col_changes

def check_all_units():
    unit_changes = False
    for unit in range(1, 10):
        if check_unit(unit):
            unit_changes = True
    return unit_changes

def check_puzzle():
    keep_going = True
    while keep_going:
        keep_going = False
        if check_all_rows():
            keep_going = True
        if check_all_cols():
            keep_going = True
        if check_all_units():
            keep_going = True
        two_notes_row()
        two_notes_col()
        
 

def two_notes_row():
    for r in range (9):
        for i in range(9):
            if len(dc[r][i])==2:
                y=dc[r][i][0]
                z=dc[r][i][1]
                for d in range(9):
                    if (len(dc[r][d])==2 and d!=i and dc[r][d][0]==y and dc[r][d][1]==z): 
                        for g in range(9):
                                if g!=i and g!=d and (y in dc[r][g] or z in dc[r][g]):
                                    if y in dc[r][g]:
                                        dc[r][g].remove(y)
                                    if z in dc[r][g]:
                                        dc[r][g].remove(z)

def two_notes_col():
    for r in range (9):
        for i in range(9):
            if len(dc[r][i])==2:
                y=dc[r][i][0]
                z=dc[r][i][1]
                for d in range(9):
                    if (len(dc[d][i])==2 and d!=r and dc[d][i][0]==y and dc[d][i][1]==z): 
                        for g in range(9):
                            if g!=i and g!=d and (y in dc[g][i] or z in dc[g][i]):
                                    if y in dc[g][i]:
                                        dc[g][i].remove(y)
                                    if z in dc[g][i]:
                                        dc[g][i].remove(z)

def stand_alone_row():
    list=[]
    repeats=[]
    for row in range(9):
        for index in range(9):
            if len(dc[row][index])>=2:
               list=dc[row][index]
               count=index+1
               while count<9:
                    if len(dc[row][count])>=2:
                        for value in dc[row][count]:
                            if value in list:
                                 list.remove(value)
                                 repeats.append(value)
                            if value not in list and value not in repeats:
                                 list.append(value)
                    count=count+1
               if len(list)>=1:
                  for i in range(9):
                    for j in list:
                        if j in dc[row][i]:
                            dc[row][i].remove(j)



check_puzzle()
stand_alone_row()
run()
