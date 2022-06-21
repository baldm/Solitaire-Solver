
from tests.test_card_analyzer import TestCard_analyzer


test = TestCard_analyzer()
test.setUp()

min_val = 0
max_val = 130
best_val = 0
most_wins = 0
seed = 5000
number_of_games = 40
print('checking val_even_board')


for i in range(min_val,max_val+1,10):
    test.set_seed(seed)
    #print('checking for value ' + str(i))
    win_amount = 0
    test.analyzer.game.val_even_board = i
    
    for j in range(0,number_of_games+1):
        
        if test.testOneGame():
            win_amount += 1

    if win_amount > most_wins:
        best_val = i
        most_wins = win_amount

test.analyzer.game.val_even_board = best_val
print('best value: ' + str(best_val))
print('most wins:' + str(most_wins))


best_val = 0
most_wins = 0
print('checking val_same_symbols')

for i in range(min_val,max_val+1,10):
    test.set_seed(seed)
    #print('checking for value ' + str(i))
    win_amount = 0
    test.analyzer.game.val_same_symbols = i

    for j in range(0,number_of_games+1):
        if test.testOneGame():
            win_amount += 1

    if win_amount > most_wins:
        best_val = i
        most_wins = win_amount

test.analyzer.game.val_same_symbols = best_val
print('best value: ' + str(best_val))
print('most wins:' + str(most_wins))


best_val = 0
most_wins = 0
print('checking val_even_foundations')

for i in range(min_val,max_val+1,10):
    test.set_seed(seed) 
    
    win_amount = 0
    test.analyzer.game.val_even_foundations = i

    for j in range(0,number_of_games+1):
        if test.testOneGame():
            win_amount += 1

    if win_amount > most_wins:
        best_val = i
        most_wins = win_amount

test.analyzer.game.val_even_foundations = best_val
print('best value: ' + str(best_val))
print('most wins:' + str(most_wins))




best_val = 0
most_wins = 0
print('checking val_get_talon')

for i in range(min_val,max_val+1,10):
    test.set_seed(seed)
    
    win_amount = 0
    test.analyzer.game.val_get_talon = i

    for j in range(0,number_of_games+1):
        if test.testOneGame():
            win_amount += 1

    if win_amount > most_wins:
        best_val = i
        most_wins = win_amount

test.analyzer.game.val_get_talon = best_val
print('best value: ' + str(best_val))
print('most wins:' + str(most_wins))


best_val = 0
most_wins = 0
print('checking val_unkown_cards_in_row')

for i in range(min_val,max_val+1,10):
    test.set_seed(seed)
    
    win_amount = 0
    test.analyzer.game.val_unkown_cards_in_row  = i

    for j in range(0,number_of_games+1):
        if test.testOneGame():
            win_amount += 1

    if win_amount > most_wins:
        best_val = i
        most_wins = win_amount

test.analyzer.game.val_unkown_cards_in_row = best_val
print('best value: ' + str(best_val))
print('most wins:' + str(most_wins))


best_val = 0
most_wins = 0
print('checking val_almost_even_foundation')

for i in range(min_val,max_val+1,10):
    test.set_seed(seed)
    
    win_amount = 0
    test.analyzer.game.val_almost_even_foundation = i

    for j in range(0,number_of_games+1):
        if test.testOneGame():
            win_amount += 1

    if win_amount > most_wins:
        best_val = i
        most_wins = win_amount

test.analyzer.game.val_almost_even_foundation = best_val
print('best value: ' + str(best_val))
print('most wins:' + str(most_wins))


best_val = 0
most_wins = 0
print('checking val_move_to_foundation')

for i in range(min_val,max_val+1,10):
    test.set_seed(seed)
    
    win_amount = 0
    test.analyzer.game.val_move_to_foundation = i

    for j in range(0,number_of_games+1):
        if test.testOneGame():
            win_amount += 1

    if win_amount > most_wins:
        best_val = i
        most_wins = win_amount

test.analyzer.game.val_move_to_foundation = best_val
print('best value: ' + str(best_val))
print('most wins:' + str(most_wins))


best_val = 0
most_wins = 0
print('checking val_move_from_talon')

for i in range(min_val,max_val+1,10):
    test.set_seed(seed)
    
    win_amount = 0
    test.analyzer.game.val_move_from_talon = i

    for j in range(0,number_of_games+1):
        if test.testOneGame():
            win_amount += 1

    if win_amount > most_wins:
        best_val = i
        most_wins = win_amount

test.analyzer.game.val_move_from_talon = best_val
print('best value: ' + str(best_val))
print('most wins:' + str(most_wins))


best_val = 0
most_wins = 0
print('checking val_move_from_board')

for i in range(min_val,max_val+1,10):
    test.set_seed(seed)
    
    win_amount = 0
    test.analyzer.game.val_move_from_board = i

    for j in range(0,number_of_games+1):
        if test.testOneGame():
            win_amount += 1

    if win_amount > most_wins:
        best_val = i
        most_wins = win_amount

test.analyzer.game.val_move_from_board = best_val
print('best value: ' + str(best_val))
print('most wins:' + str(most_wins))


best_val = 0
most_wins = 0
print('checking val_cards_in_stock')

for i in range(min_val,max_val+1,10):
    test.set_seed(seed)
    
    win_amount = 0
    test.analyzer.game.val_cards_in_stock = i

    for j in range(0,number_of_games+1):
        if test.testOneGame():
            win_amount += 1

    if win_amount > most_wins:
        best_val = i
        most_wins = win_amount


test.analyzer.game.val_cards_in_stock = best_val
print('best value: ' + str(best_val))
print('most wins:' + str(most_wins))