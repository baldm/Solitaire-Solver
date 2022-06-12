from ..model.action_model import Action_model
from ..model.state_model import State_model

class Solitaire_controller():
    def __init__(self):
        values = list(range(1,14))
        keys = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
        self.order = dict(zip(keys,values))
        

    def Actions(self, state : State_model):
        ## returns list of actions which is possible in given state
        actions = []
        board = state.board
        foundations = state.foundations
        
        
        ## actions regarding moving card from talon
        if len(state.talon) > 0:
            card_index = 0
            card = state.talon[0]               
            for to_row in range(0,len(board) + len(foundations)):
                action = Action_model(card_index, -1, to_row)
                if self.is_move_legal(action, state):
                    actions.append(action)

        
        ## If it is possible to draw from stock
        if self.draw_from_stock(state.stock,state.talon):
            action = Action_model()
            action.get_talon = True
            actions.append(action)

                
        #Checks moves for every card in the tableau
        for row_index,row in enumerate(board):        
            for card_index,card in enumerate(row):
                if card == '[]':
                    continue
                for to_row in range(0,len(board) + len(foundations)):
                    if to_row != row_index:
                        action = Action_model(card_index, row_index, to_row)
                        if self.is_move_legal(action, state):
                            actions.append(action)
        return actions
        

    def Result(self, state : State_model, action : Action_model):

        board = state.board
        foundations = state.foundations
        talon = state.talon
        stock = state.stock

        if action.get_talon:
            if stock >= 3:
                talon = stock[-3:] + talon
                stock = stock[:-3]
                ## If we need to shuffle talon into stock
            else:
                stock = talon + stock
                talon = []
            
            new_state = State_model(board,foundations,stock,talon)
            new_state.action = action  
            return new_state

        if action.from_row == -1:
            cards = [state.talon[0]]
            talon.pop(0)
        else:
            cards = board[action.from_row][action.card_index-1 : None]
            board[action.from_row] = board[action.from_row][:action.card_index-1]

        if action.to_row < len(board):
            board[action.to_row] += cards
        else:
            foundations[action.to_row%len(board)] += cards

        
        new_state = State_model(board,foundations,stock,talon)
        new_state.action = action
        return new_state
        

    def is_move_legal(self, action : Action_model, state : State_model):
        ##If card is taken from talon
        if action.from_row == -1:
            card = state.talon[-1]
        else:
            card = state.board[action.from_row][-1]
        #if you move to foundations
        if action.to_row >= len(state.board):
            to_row = state.foundations[action.to_row%len(state.board)]
            if len(to_row) == 0:
                if card[0] == 'A':
                    return True
                    ## todo add check if same type
            elif self.descending_order(card,to_row[-1]) and card[1] == state.board[action.to_row][-1][1]:
                return True
            return False


        #Logic if moved to row on board
        to_row = state.board[action.to_row]
      
        if len(to_row) == 0:
            
            if not self.king_to_empty(card,state.board[action.to_row]):
                return False
            return True
        else:
            card_to = to_row[-1]
            if not self.descending_order(card,card_to):
                return False

            if not self.alternating_color(card,card_to):
                return False

        return True

    def descending_order(self, card : str, card_to : str):

        if self.order.get(card_to[0]) - 1 == self.order.get(card[0]):
            return True
        return False
    
    def king_to_empty(self, card : str, to_row : list):
        if card[0] == 'K':
            if not to_row:
                return True
        return False

    def alternating_color(self, card : str, card_to : str):
        if (card[1] == 'S' or card[1] == 'C') and (card_to[1] == 'D' or card_to[1] == 'H') :
            return True
        elif (card[1] == 'D' or card[1] == 'H') and (card_to[1] == 'S' or card_to[1] == 'C'):
            return True
        return False

        ## If there are less than 3 cards in talon and stock combined the game is locked and unsolvable
    def draw_from_stock(self,stock: list, talon: list):
            if (len(talon) + len(stock) < 3):
                return False
            return True

    def is_terminal(self,state : State_model):
        for row in state.board:
            if row and row[-1] == '[]':
                return True
        if state.talon and state.talon[-1] == '[]':
            return True
        return False
       
    def is_goal(self, state : State_model):
        for row in state.board:
            if row:
                return False
        if state.talon or state.stock:
            return False
        return True
        