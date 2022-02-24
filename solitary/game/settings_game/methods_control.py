

def press_undo(loc):
    if loc[0] > 40 and loc[0] < 104:
        if loc[1] > 702 and loc[1] < 766:
            return True
    return False

def press_NEW_GAME(loc):
    if loc[0] > 792 and loc[0] < 856:
        if loc[1] > 702 and loc[1] < 766:
            return True
    return False

def start_new_game(loc):
    #result 1 mean YES
    #result 2 mean NO orpress outsidew the options
    #result 3 mean no option pressed
    if loc[0] > 312 and loc[0] < 429:
        if loc[1] > 381 and loc[1] < 418:
            return 1
    elif loc[0] > 482 and loc[0] < 598:
        if loc[1] > 380 and loc[1] < 419:
            return 2
    elif loc[0] < 250 or loc[0] > 650 or loc[1] < 200 or loc[1] > 456:
            return 2
    return 3

def set_collection_quantity(collectionU):
    # rearange the quantity of the list Spare collection separattely to avodi unorganizatoin
    i0 =0
    while i0<7:
        collectionU[i0].set_quantity(len(game_Omega[0].listSpare[i0]))
        i0+=1
        




