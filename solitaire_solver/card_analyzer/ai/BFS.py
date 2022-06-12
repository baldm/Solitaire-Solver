import queue
from ..model.state_model import State_model
from ..controller.solitaire_controller import Solitaire_controller
from ..model.action_model import Action_model


class BFS():
    def __init__(self) -> None:
        self.frontier : queue.Queue = queue.Queue()
        self.expanded = []
        self.leaves = []


    def __call__(self, state : State_model, game : Solitaire_controller):
        self.frontier.put(state)
        while not self.frontier.empty():
            currentState = self.frontier.get()
            #Checks if the game is won
            if game.is_goal(currentState):
                return currentState
            #checks if a new photo is needed
            elif game.is_terminal(currentState):
                self.leaves.append(currentState)
            else:
                self.expand(currentState, game)
        
        ##Make Heuristic on leaves and return best state
        if self.leaves:
            return self.leaves[0]
    
        return False
    

    def expand(self,state : State_model, game : Solitaire_controller):
        ##Generate all new states
        
        actions : list[Action_model] = game.Actions(state)

    
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