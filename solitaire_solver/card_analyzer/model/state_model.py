


class State_model():
    def __init__(self,board : list(list),foundations : list(list),stock : bool, talon : list):
        self.board = board
        self.foundations = foundations
        self.prev_state : State_model = self
        self.action = False
        self.stock = stock
        self.talon = talon

    def equals(self,state):
        if self.board == state.board and self.foundations == state.foundations:
            return True
        return False

