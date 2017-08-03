# Defining all the methods


# returns the values that sure to be part of the candidate key
def sure2becands(mylist, numb):
    mytmplst = fullboard(numb)
    for i in range(len(mylist)):
        for val in mylist[i]:
            if val in mytmplst:
                mytmplst.pop(mytmplst.index(val))
    return mytmplst

######## NEW FUNCTIONS #######
def checklen(cell, checkboard, key):
    return len(cell) <= len(checkboard) - checkboard.index(key) and len(cell) > 1


def isdoubledep(key, left, checkboard):
    flag = True
    for cell in left:
        if key == cell[0] and checklen(cell, checkboard, key):
            for i in range(len(cell)):
                if cell[i] != checkboard[checkboard.index(key) + i]:
                    flag = False
    return flag
######## NEW FUNCTIONS #######

# returns a lists of lists with all the candidate keys
def calculatecands(left, right, scand, num):
    # todo - try to save some space and make some funcs of this
    iscands = []
    checkboard = []  # used to check if the boards fills up
    candslist = []  # the list that has the full candidate keys of each loop
    lst2check = fullboard(num)
    reps = 0
    x = 0
    flag = True
    # if scand is empty append


    # appends the keys that are definitely part of the candidate to iscands and to checkboard
    while x <= reps:
        if scand:  # if scand is not empty , append it to iscands and checkboard
            for value in scand:
                iscands.append(value)
                checkboard.append(value)
        else:  # else append the first left cell
            reps = len(left) - 1
            for value in left[x]:
                iscands.append(value)
                checkboard.append(value)
        for key in checkboard:
            if ispartof2dlist(list(key), left) != 0:  # if key is in list(left)
                for cell in left:
                    for val in cell:
                        ################
                        #PROBLEM ,  can we have 1-23 14-5?
                        ################
                        if key == val:  # and cell.index(val) == 0:  # if you find the key and its the first of the cell
                            # code that tests if val is a part of a big cell and if we want to use that one or another cell
                            if len(cell) > 1:
                                if len(cell) <= len(checkboard) - checkboard.index(key):
                                    # if the key is a part of a big cell (more than 1 value)
                                    # and there are enough values in the checkboard in order for the cell to work
                                    for i in range(len(cell)):
                                        if cell[i] != checkboard[checkboard.index(key) + i]:
                                            flag = False
                                            # check if the values are actually right
                                elif checkboard[-1] == key:
                                    for value in cell:
                                        if value not in checkboard:
                                            checkboard.append(value)
                                            iscands.append(value)
                                else:
                                    continue
                                # end of double cell code
                            a = left.index(cell)
                            for j in right[a]:
                                if j not in checkboard and flag is True:
                                    checkboard.append(j)
                            flag = True
            elif checkboard[-1] == key:
                reps = len(left) - 1
                for val in left[x]:
                    if val not in checkboard:
                        checkboard.append(val)
                        iscands.append(val)
            if comparelists(checkboard, lst2check):
                candslist.append(iscands)
                break
        checkboard = []
        iscands = []
        x += 1
    return candslist


def comparelists(list1, list2):
    list1 = list1[:]
    list2 = list2[:]
    list1.sort()
    list2.sort()
    if list1 == list2:
        return True
    else:
        return False


def fullboard(num):
    mylist = []
    for i in range(num):
        mylist.append(str(i + 1))
    return mylist


# if there is a higher number than the no. of rows then its not valid
def validcheck(cols, board):
    flag = False
    tmp = board
    tmp = tmp.translate(None, ' -')
    for value in tmp:
        if int(value) > int(cols):
            print "Input not valid"
            flag = True
            break
    return flag


def ispartof2dlist(lskeys, my2dlist):
    tag = 0
    tmplst = []
    for cell in my2dlist:
        for key in lskeys:
            if key in cell:
                tmplst.append(key)
        if tmplst and tag == 0:
            if len(cell) == len(lskeys):
                tag = 2
            else:
                tag = 1

    return tag


def isinbothlists(list1, list2, num):
    board = []
    for i in range(1, num + 1):
        for cell in list1:
            for var in cell:
                for val in list2:
                    if var in val and var not in board:
                        board.append(var)
    return board


def splitinput(string):
    keys = []
    res = []
    lsofk = []
    lsofr = []
    values = [[0 for x in range(50)] for y in range(50)]
    # divides the string to the individual dependencies in lists
    # splits the string to the individual dependencies
    deps = string.split()
    # splits the dependencies to the individual values
    for value in deps:
        values[deps.index(value)] = value.split("-")
        for k in values[deps.index(value)][0]:
            keys.append(k)
        lsofk.append(keys)
        keys = []
        for j in values[deps.index(value)][1]:
            res.append(j)
        lsofr.append(res)
        res = []

    return lsofk, lsofr


# TODO -fix the wrong nf bug

def findnm(left, right, cands, num):
    nf2 = True
    nf3 = True
    bcnf = True
    leftind = []
    rightind = []
    doublist = isinbothlists(left, right, num)

    for index in range(len(left)):
        if ispartof2dlist(left[index], cands) == 1 and ispartof2dlist(right[index], cands) == 0:
            nf2 = False

    inboth = isinbothlists(left, right, num)
    for value in inboth:
        for cell in left:
            for val in cell:
                if val == value:
                    leftind.append(left.index(cell))
        for cell in right:
            for val in cell:
                if val == value:
                    rightind.append(right.index(cell))

    if nf2:
        for val in inboth:
            tmpindex = inboth.index(val)
            if ispartof2dlist(val, cands) == 0 and ispartof2dlist(right[leftind[tmpindex]],
                                                                  cands) == 2 and ispartof2dlist(
                    left[rightind[tmpindex]], cands) == 0:
                nf3 = False
        if nf3:
            for var in left:
                if ispartof2dlist(var, cands) != 2:
                    bcnf = False
    if nf2:
        if nf3:
            if bcnf:
                return "BCNF"
            else:
                return "3NF"
        else:
            return "2NF"
    else:
        return "1NF"


# TODO - work on the bcnf shit

def tobcnf(candlst, lefts, rights, num):
    bcnft = []
    if len(candlst) == 1:
        for cell in candlst:
            for val in cell:
                bcnft.append(val)
        bcnft.append("-")
        for value in fullboard(num):
            if value not in bcnft:
                bcnft.append(value)
    return bcnft


# -------------------------------------------------------------------

# Main

while True:
    columns = int(raw_input("Enter number of rows:"))
    inpt = raw_input("Enter dependencies with '-' split by ' '(ex. 1-23 2-3):")
    if not validcheck(columns, inpt): break
keys, results = splitinput(inpt)
surecands = sure2becands(results, columns)
endcands = calculatecands(keys, results, surecands, columns)
for cell in endcands:
    print "key no.", endcands.index(cell) + 1, "is", ','.join(cell)
print "table is", findnm(keys, results, endcands, columns)
if findnm(keys, results, endcands, columns) != "BCNF":
    print ''.join(tobcnf(endcands, keys, results, columns)), "is BCNF"
