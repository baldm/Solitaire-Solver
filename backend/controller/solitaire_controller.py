from model.action_model import Action_model
from model.state_model import State_model

class Solitaire_controller():
    def __init__(self):
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
                    if self.is_move_legal(action):
                        actions.append(action)
        return actions
        

    def result():
        ## applies a given action to a given state and returns state
        pass

    def is_move_legal():
        ## checks if an action is valid
        pass

    def is_terminal():
        ## returns bool
        pass