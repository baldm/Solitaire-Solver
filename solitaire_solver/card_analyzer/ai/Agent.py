from ..controller.solitaire_controller import Solitaire_controller
from ..model.state_model import State_model
from ..model.action_model import Action_model
from .BFS import BFS
class Agent():
    def __init__(self, game: Solitaire_controller, strategy : BFS) -> None:
        self.game = game
        self.strategy = strategy

    def find_moves(self, initial_state):
        initial_state.prev_state = initial_state
        return self.strategy(initial_state)



