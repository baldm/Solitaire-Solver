from sympy import false
from model.action_model import Action_model
from model.state_model import State_model

class Solitaire_controller():
    def __init__(self):
        values = range(1,13)
        keys = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
        self.order = dict(keys,values)
        pass

    def Actions(self, state : State_model):
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
        

    def Result(self, state : State_model, action : Action_model):

        board = state.board
        foundations = state.foundations

        if action.to_row < len(board):
            board[action.to_row] += board[action.from_row][action.card_index-1 : None]
        else:
            foundations[action.to_row%len(board)] = board[action.from_row][action.card_index : None]


        board[action.from_row] = board[action.from_row][:action.card_index-1]
        new_state = State_model(board,foundations,state.stock,state.talon,state.stock)
        state.action = action
        return new_state


    def is_move_legal(self, action : Action_model, state : State_model):
        card = state.board[action.from_row][-1]
        #if you move to foundations
        if action.to_row > len(state.board):
            to_row = state.foundations[action.to_row%len(state.board)]
            if False in to_row:
                if card[0] == 'A':
                    return True
                    ## todo add check if same type
            elif self.descending_order(card,to_row[-1]) and card == state.board[action.to_row][-1]:
                return True
            return False


        #Logic if moved to row on board
        to_row = state.board[action.to_row]

        if False in to_row:

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
    def draw_from_stack(stock : list, talon : list):
        if(len(talon)+len(stock)<3):
            return False
        return True

    ## Can't move a card to the talon from other piles
    def from_and_to_pile_is_legal(card_from : str, card_to : str, talon : list):
        if not card_from in talon:
            if card_to in talon:
                return False
        return True





    def is_terminal(self,state : State_model):
        for row in state.board:
            if row[-1] == '[]':
                return True
        return self.is_goal(state)

    def is_goal(self, state : State_model):
        for row in state.board:
            if not False in row:
                return False
        return True
