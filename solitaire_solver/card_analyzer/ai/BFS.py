
from ..model.state_model import State_model
from ..controller.solitaire_controller import Solitaire_controller
from ..model.action_model import Action_model


class BFS():
    def __init__(self) -> None:
        self.frontier = []
        self.expanded = []
        self.leaves = []
        self.got_talon = False
        self.talons = []
        
        


    def __call__(self, state : State_model, game : Solitaire_controller):
        self.leaves = []
        self.expanded = []
        self.frontier = []
        self.got_talon = False
        self.talons = []
        

        self.frontier.append(state)
        
        while  len(self.frontier) > 0 and len(self.leaves) < 120 and len(self.frontier) < 1000:
            currentState = self.frontier[0]
            self.frontier.pop(0)
            #Checks if the game is won
            if game.is_goal(currentState):
                return currentState
            else:
                self.expand(currentState, game)
        
        ##Make Heuristic on leaves and return best state
        if self.leaves:
            best_state = self.leaves[0]
            best_val = game.eval(best_state)
            for state in self.leaves:
                temp_val = game.eval(state)
                if temp_val > best_val:
                    best_state = state
                    best_val = temp_val
            
            return best_state
        
        return False
    

    def expand(self,state : State_model, game : Solitaire_controller):
        ##Generate all new states
        
        actions : list[Action_model] = game.Actions(state)
        
    
        for action in actions:
           

            new_state = game.Result(state,action)
            

            if not (self.exists(new_state) or (self.talon_exist(new_state) and action.get_talon)):
                self.expanded.append(new_state)
                if not self.talon_exist(new_state):
                    self.talons.append(new_state.talon)

                is_pruned = self.new_prune(new_state)
                
                if game.is_terminal(new_state):
                    self.leaves.append(new_state)
                else:
                    self.frontier.append(new_state)

                if is_pruned:
                    break
            
                

    def prune(self,state : State_model):
        if state.foundations != state.prev_state.foundations:
            length = 0
            last_length = 0
            for foundation in state.foundations:
                if len(foundation) > length:
                    length = len(foundation)
            
            for foundation in state.prev_state.foundations:
                if len(foundation) > length:
                    last_length = len(foundation)

            new_number = 0
            for foundation in state.foundations:
                if len(foundation) == length or len(foundation) == (length -1) :
                    break
            
            else:
                self.frontier = []
                self.expanded = []
                self.leaves = []
                

    def new_prune(self, state : State_model):
        length = 0
        last_length = 0

        for index,foundation in enumerate(state.foundations):
            for foundation in state.foundations:
                if len(foundation) > length:
                    length = len(foundation)
                if len(state.prev_state.foundations[index]) > last_length:
                    last_length = len(state.prev_state.foundations[index])
        
        if length > last_length:
            for foundation in state.foundations:
                if len(foundation) != length and len(foundation) != (length -1) :
                    break
            
            else:
                self.frontier = []
                self.expanded = []
                self.leaves = []
                self.talons = []
                return True
        
        else:
            if state.action and not state.action.get_talon and state.action.to_row >= len(state.board):
                self.frontier = []
                self.expanded = []
                self.leaves = []
                self.talons = []
                return True

        return False

    def talon_exist(self, new_state : State_model):
        for talon in self.talons:
            if talon == new_state.talon:
                return True
        return False

    def is_move_redundant(self,state : State_model, action : Action_model, game : Solitaire_controller):
        if state.prev_state != state and not action.get_talon and action.to_row < len(state.board):
            if action.from_row == -1:
                return False
            else:
                card = state.prev_state.board[action.from_row][action.card_index]

            if len(state.prev_state.board[action.to_row]) == 0 and len(state.prev_state.board[action.from_row]) == 0:
                if (action.from_row != -1 and state.prev_state.board[action.from_row][0] != card):
                    return True
            elif len(state.prev_state.board[action.to_row]) == game.order[card[0]] and len(state.prev_state.board[action.from_row]) == game.order[card[0]]:
                if game.same_symbols(state.prev_state.board,3) < game.same_symbols(state.board,3):
                    return True
        return False
             
        




    def exists(self,new_state : State_model):
        for state in self.expanded:
                if state.equals(new_state):
                    return True 
        for state in self.leaves:
            if state.board == new_state.board:
                return True        
        return False