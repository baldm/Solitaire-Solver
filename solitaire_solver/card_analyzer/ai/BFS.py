import queue
from model.state_model import State_model
from controller.solitaire_controller import Solitaire_controller


class BFS():
    def __init__(self) -> None:
        self.frontier : queue.Queue = queue.Queue()
        self.expanded = []


    def __call__(self, state : State_model, game : Solitaire_controller):
        self.frontier.put(state)
        while not self.frontier.empty():
            currentState = self.frontier.get()
            if game.is_terminal(currentState):
                return currentState
            self.expand(currentState, game)
        return False
    

    def expand(self,state : State_model, game : Solitaire_controller):
        ##Generate all new states
        
        actions = game.Actions(state)
        for action in actions:
            new_state = game.Result(state,action)
            if not self.exists(new_state):
                new_state.prev_state = state
                self.frontier.put(new_state)
                self.expanded.append(new_state)

            

    def exists(self,new_state : State_model):
        for state in self.expanded:
                if state.equals(new_state):
                    return True
        
        return False