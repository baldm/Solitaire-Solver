class State_model():
    def __init__(self,board,foundations):
        self.board = board
        self.foundations = foundations
        self.prev_state = self

    def equals(self,state):
        if self.board == state.board and self.foundations == state.foundations:
            return True
        return False

