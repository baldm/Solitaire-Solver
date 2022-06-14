from ..model.action_model import Action_model
from ..model.state_model import State_model


class Solitaire_controller():
    def __init__(self):
        values = list(range(1, 14))
        keys = ['A', '2', '3', '4', '5', '6',
                '7', '8', '9', 'T', 'J', 'Q', 'K']
        self.order = dict(zip(keys, values))

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
                if self.is_move_legal(action, state):
                    actions.append(action)

        # If it is possible to draw from stock
        if self.draw_from_stock(state.stock, state.talon):
            action = Action_model()
            action.get_talon = True
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
                        if self.is_move_legal(action, state):
                            actions.append(action)
        return actions

    def Result(self, state: State_model, action: Action_model):

        temp_board = state.board.copy()
        temp_foundations = state.foundations.copy()
        temp_talon = state.talon.copy()
        temp_stock = state.stock.copy()

        if action.get_talon:
            if len(temp_stock) >= 3:
                temp_talon = temp_stock[-3:] + temp_talon
                temp_stock = temp_stock[:-3]
                # If we need to shuffle talon into stock
            else:
                temp_stock = temp_talon + temp_stock
                temp_talon = []

            new_state = State_model(temp_board, temp_foundations, temp_stock, temp_talon)
            new_state.action = action
            new_state.prev_state = state
            return new_state

        if action.from_row == -1:
            cards = [state.talon[0]]
            temp_talon.pop(0)
        else:
            cards = temp_board[action.from_row][action.card_index: None]
            temp_board[action.from_row] = temp_board[action.from_row][:(action.card_index-1)]

        if action.to_row < len(temp_board):
           
            temp_board[action.to_row] = state.board[action.to_row] + cards
        else:
            temp_foundations[action.to_row % len(temp_board)] = state.foundations[action.to_row % len(temp_board)] + cards

        new_state = State_model(temp_board, temp_foundations, temp_stock, temp_talon)
        new_state.action = action
        new_state.prev_state = state
        return new_state

    def is_move_legal(self, action: Action_model, state: State_model):
        # If card is taken from talon
        if action.from_row == -1:
            card = state.talon[0]
        else:
            card = state.board[action.from_row][action.card_index]
            
        # if you move to foundations
        if action.to_row >= len(state.board):
            to_row = state.foundations[action.to_row % len(state.board)]
            if len(to_row) == 0:
                if card[0] == 'A':
                    return True
                    # todo add check if same type
            elif self.descending_order(card, to_row[-1]) and card[1] == state.board[action.to_row % len(state.board)][-1][1]:
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

        # If there are less than 3 cards in talon and stock combined the game is locked and unsolvable
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

        if action.get_talon:
            return 200
        else:
            if self.ace_to_foundation:
                val += 2000

            if action.from_row != -1:
                val += 50
                for card in state.board[action.from_row]:
                    if card == '[]':
                        val += 5
            else:
                val += 250

            if action.to_row >= len(state.board):
                val -= 1

        val += self.even_piles(state.board, 5) # if weight = 5, max 35
        val += self.even_piles(state.foundations, 10) # if weight = 10, max 40
        val += self.same_symbols(state.board, 1) # if weight = 1, max 37

        return val
        

    def even_piles(self, lists, max_pts):
        val = 0
        board_row_mean_length = 0
        
        for row in lists:
            board_row_mean_length += len(row)
        board_row_mean_length /= len(lists)

        for row in lists:
            val += (max_pts - abs(len(row) - int(board_row_mean_length)))
        
        if val < 0:
            return 0

        return val

    def same_symbols(self, board, weight):
        val = 0

        for row in board:
            for index, card in enumerate(row):
                if card == '[]':
                    continue
                elif index > 1:
                    if card[1] == row[index-2][1]:
                        val += weight

        return val

    def ace_to_foundation(self, state : State_model):
        action : Action_model = state.action
        if action.to_row >= len(state.board):
            if state.foundations[action.to_row%len(state.board)][-1][0] == 'A':
                return True
        return False
