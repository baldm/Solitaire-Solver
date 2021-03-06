from ..model.action_model import Action_model
from ..model.state_model import State_model


class Solitaire_controller():
    def __init__(self):
        values = list(range(1, 14))
        keys = ['A', '2', '3', '4', '5', '6',
                '7', '8', '9', 'T', 'J', 'Q', 'K']
        self.order = dict(zip(keys, values))

        self.val_even_board = 10
        
        self.val_same_symbols = 10

        self.val_even_foundations = 100

        self.val_get_talon = 0

        self.val_unkown_cards_in_row = 70

        self.val_almost_even_foundation = 0

        self.val_move_to_foundation = 10

        self.val_move_from_talon = 0

        self.val_move_from_board = 20

        self.val_cards_in_stock = 40

    def Actions(self, state: State_model):
        # returns list of actions which is possible in given state
        actions = []
        board = state.board
        foundations = state.foundations

        # actions regarding moving card from talon
        if len(state.talon) > 0:
            card_index = 0
            card = state.talon[0]
            for to_row in range(0, len(board) + len(foundations)):
                action = Action_model(card_index, -1, to_row)
                #Check if move is legal
                if self.is_move_legal(action, state):
                    #Add to list
                    actions.append(action)

        # If it is possible to draw from stock
        if self.draw_from_stock(state.stock, state.talon):
            action = Action_model()
            action.get_talon = True
            # If there are 3 cards in talon and stock combined, and there is at least 
            # one card in stock, the game must get talon
            if len(state.stock) > 0 and len(state.stock) + len(state.talon) == 3:
                return [action]
            
            actions.append(action)

        # Checks moves for every card in the tableau
        for row_index, row in enumerate(board):
            for card_index, card in enumerate(row):
                if card == '[]':
                    continue
                for to_row in range(0, len(board) + len(foundations)):
                    if to_row != row_index:
                        action = Action_model(card_index, row_index, to_row)
                        #Check if the action is legal
                        if self.is_move_legal(action, state):
                            #Add to list
                            actions.append(action)
        return actions

    def Result(self, state: State_model, action: Action_model):

        temp_board = state.board.copy()
        temp_foundations = state.foundations.copy()
        temp_talon = state.talon.copy()
        temp_stock = state.stock.copy()
        # If action was to get talon
        if action.get_talon:
            #If stock contains 3 or more cards
            if len(temp_stock) >= 3:
                temp_talon = temp_stock[-3:] + temp_talon
                temp_stock = temp_stock[:-3]
                # If we need to shuffle talon into stock
            else:
                #Put talon back in the stock
                temp_stock = temp_talon + temp_stock
                temp_talon = []

            #Create new state
            new_state = State_model(temp_board, temp_foundations, temp_stock, temp_talon)
            new_state.action = action
            new_state.prev_state = state
            #Return neew state
            return new_state

        #Here we define the card 
        if action.from_row == -1:
            #If the card was taken from talon
            cards = [state.talon[0]]
            #We remove the card from talon
            temp_talon.pop(0)
        else:
            #Make a list containing all cards from the moved card, to the end of the row
            cards = temp_board[action.from_row][action.card_index: None]
            #If it was on index 0
            if action.card_index == 0:
                #Remove all cards from row
                temp_board[action.from_row] = []
            else:
                #Remove moved cards from row
                temp_board[action.from_row] = temp_board[action.from_row][:(action.card_index)]

        #Add card(s) to new row
        if action.to_row < len(temp_board):
           #If it was to a row in the board
            temp_board[action.to_row] = state.board[action.to_row] + cards
        else:
            #If it was a to Foundation
            temp_foundations[action.to_row % len(temp_board)] = state.foundations[action.to_row % len(temp_board)] + cards
        
        #Create new state
        new_state = State_model(temp_board, temp_foundations, temp_stock, temp_talon)
        new_state.action = action
        new_state.prev_state = state
        #Retorn new state
        return new_state

    def is_move_legal(self, action: Action_model, state: State_model):
        # If card is taken from talon
        if action.from_row == -1:
            card = state.talon[0]
        else:
            card = state.board[action.from_row][action.card_index]
            
        # if you move to foundations
        if action.to_row >= len(state.board):
            if action.from_row != -1 and state.board[action.from_row][-1] == card or action.from_row == -1:
                to_row = state.foundations[action.to_row % len(state.board)]
                if len(to_row) == 0:
                    if card[0] == 'A':
                        return True
                        # todo add check if same type
                elif self.descending_order( to_row[-1],card) and card[1] == to_row[-1][1]:
                    return True
            return False

        # Logic if moved to row on board
        to_row = state.board[action.to_row]

        if len(to_row) == 0:

            if not self.king_to_empty(card, state.board[action.to_row]):
                return False
            return True
        else:
            card_to = to_row[-1]
            if not self.descending_order(card, card_to):
                return False

            if not self.alternating_color(card, card_to):
                return False

        return True

    def descending_order(self, card: str, card_to: str):

        if self.order[card_to[0]] - 1 == self.order[card[0]]:
            return True
        return False

    def king_to_empty(self, card: str, to_row: list):
        if card[0] == 'K':
            if not to_row:
                return True
        return False

    def alternating_color(self, card: str, card_to: str):
        if (card[1] == 'S' or card[1] == 'C') and (card_to[1] == 'D' or card_to[1] == 'H'):
            return True
        elif (card[1] == 'D' or card[1] == 'H') and (card_to[1] == 'S' or card_to[1] == 'C'):
            return True
        return False

    # If there are less than 3 cards in talon and stock combined, return false
    def draw_from_stock(self, stock: list, talon: list):
        if (len(talon) + len(stock) < 3):
            return False
        return True

    def is_terminal(self, state: State_model):
        for row in state.board:
            if len(row) > 0 and row[-1] == '[]':
                return True
        if len(state.talon) > 0 and state.talon[0] == '[]':
            return True
        return False

    def is_goal(self, state: State_model):
        for row in state.board:
            if row:
                return False
        if state.talon or state.stock:
            return False
        return True

    def eval(self,state : State_model):

        val = 0
        
        

        action : Action_model = state.action
        #If last action was to draw from stock
        if action.get_talon:
            return self.val_get_talon
        else:
            
            #If the last action was to move a card form the Tableau
            if action.from_row != -1:
                val += self.val_move_from_board
                #Add val for each unkown card in row
                for card in state.board[action.from_row]:
                    if card == '[]':
                        val += self.val_unkown_cards_in_row
            else:
                #Add val for getting new card in talon
                val += self.val_move_from_talon

            #If the card the last action moved a card to foundation
            if action.to_row >= len(state.board):
                val -= self.val_move_to_foundation
        
        #Checks if all piles on Tableau is approximately even
        val += self.even_piles(state.board, self.val_even_board) 
        #Checks if same symbols occur in the rows
        val += self.same_symbols(state.board, self.val_same_symbols) 
        #Checks if foundation is approximately even
        val += self.even_piles(state.foundations, self.val_almost_even_foundation)
        #Checks if the foundations is even og 1 less than the largest foundation
        val += self.even_foundations(state.foundations, self.val_even_foundations)
        #Checks how many cards is left in the stock+talon
        val += self.cards_in_stock(state,self.val_cards_in_stock)
        
        

        return val
                  
    def cards_in_stock(self,state : State_model,val):
        val = 0
        #Retorn negative value for each card in the stock + talon
        return -val*(len(state.stock)+len(state.talon))
    def even_piles(self, lists, max_pts):
        val = 0
        board_row_mean_length = 0
        #Determines mean length of rows
        for row in lists:
            board_row_mean_length += len(row)
        board_row_mean_length /= len(lists)
        # Gives points based on how far away from mean length each row is
        for row in lists:
            val += (max_pts - abs(len(row) - int(board_row_mean_length)))
        
        if val < 0:
            return 0

        return val
    def even_foundations(self, foundations, pts):
        val = pts
        length = 0
        #Finds the length of the largest foundation
        for foundation in foundations:
            if len(foundation) > length:
                length = len(foundation)
        if length == 0:
            return 0
        #Checks if each foundation is either equally as long as the largest, or 1 shorter than the largest
        for foundation in foundations:
            if len(foundation) != length and len(foundation) != length-1:
                #Remove points based on how much shorther the foundation is
                val -= (int(pts/4)+ abs(len(foundation)- length)*3)
        if val != pts:
            return val
        return val * length

    


    def same_symbols(self, board, weight):
        val = 0
        #Checks if faceup cards have same symbols
        for row in board:
            for index, card in enumerate(row):
                if card == '[]':
                    continue
                elif index > 1:
                    #If the card has same symbol as the card 2 spaces before
                    if card[1] == row[index-2][1]:
                        #Add weight as value
                        val += weight

        return val

    def ace_to_foundation(self, state : State_model):
        action : Action_model = state.action
        if action.to_row >= len(state.board):
            if state.foundations[action.to_row%len(state.board)][-1][0] == 'A':
                return True
        return False
