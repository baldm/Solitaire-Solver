


from solitaire_solver.card_analyzer.model.action_model import Action_model


class State_model():
    def __init__(self,board : list[list],foundations : list[list],stock : list, talon : list):
        self.board = board
        self.foundations = foundations
        self.prev_state : State_model = self
        self.action : Action_model = False
        self.stock = stock
        self.talon = talon

    def equals(self,state : 'State_model'):
        if self.board == state.board and self.talon == state.talon:
            return True
        return False

