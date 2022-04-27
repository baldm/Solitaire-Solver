from model.action_model import Action_model
from model.state_model import State_model

class Solitaire_controller():
    def __init__(self):
        values = range(1,13)
        keys = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
        self.order = dict(keys,values)

        pass

    def action(self, state : State_model):
        ## returns list of actions which is possible in given state
        actions = []
        board = state.board
        foundations = state.foundations

        for row in range (0,len(board)+1):
            for card,card_index in board[row]:
                if card == '[]':
                    continue
                for to_row in range(0,len(board) + len(foundations) + 1):
                    action = Action_model(card_index, row, to_row)
                    if self.is_move_legal(action, state):
                        actions.append(action)
        return actions
        

    def result():
        ## applies a given action to a given state and returns state
        pass

    def is_move_legal(actions : Action_model, state : State_model):
        ## checks if an action is valid
        pass

    def descending_order(self,card : str, card_to : str):

        if self.order.get(card_to[0]) - 1 == self.order.get(card[0]):
            return True
        return False
    
    def king_to_empty(card : str, to_row : list):
        if card[0] == 'K':
            if not to_row:
                return True
        return False

    def alternating_color(card : str, card_to : str):
        if (card[1] == 'S' or card[1] == 'C') and (card_to[1] == 'D' or card_to[1] == 'H') :
            return True
        elif (card[1] == 'D' or card[1] == 'H') and (card_to[1] == 'S' or card_to[1] == 'C'):
            return True
        return False
        
       
    



    def is_terminal():
        ## returns bool
        pass