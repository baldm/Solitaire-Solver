from controller.solitaire_controller import Solitaire_controller
from model.state_model import State_model
from model.action_model import Action_model
from BFS import BFS
class Agent():
    def __init__(self, game: Solitaire_controller, strategy : BFS) -> None:
        self.game = game
        self.strategy = strategy

    def find_moves(self, board, foundation, stock, talon):
        initial_state = State_model(board, foundation, stock, talon)
        state = self.strategy(initial_state)
        prev_state : State_model = state.prev_state
        actions = []
        while prev_state != state:
            action : Action_model = state.action
            actions.append([action.from_row, action.from_row, action.card_index])
        actions.reverse()
        return actions


