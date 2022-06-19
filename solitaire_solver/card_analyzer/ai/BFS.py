
from os import stat
from ..model.state_model import State_model
from ..controller.solitaire_controller import Solitaire_controller
from ..model.action_model import Action_model


class BFS():
    def __init__(self) -> None:
        self.frontier = []
        self.expanded = []
        self.leaves = []
        
        self.talons = []
        
        


    def __call__(self, state : State_model, game : Solitaire_controller):
        self.leaves = []
        self.expanded = []
        self.frontier = []
        
        self.talons = []
        

        self.frontier.append(state)
        
        while  len(self.frontier) > 0:
            if len(self.leaves) > 500:
                break
            currentState = self.frontier[0]
            
            self.frontier.pop(0)
            #Checks if the game is won
            if game.is_goal(currentState):
                return currentState
            else:
                self.expand(currentState, game)
        
        if len(self.frontier) > 0:
            print('frontier not empty')
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
        temp_frontier = []
        
        for action in actions:

            new_state = game.Result(state,action)
            
            if not (self.exists(new_state) or (self.talon_exist(new_state) and action.get_talon) or self.is_redundant(new_state,game) ):
                self.expanded.append(new_state)
                if not self.talon_exist(new_state):
                    self.talons.append([new_state.talon,new_state.stock])

                is_pruned = self.new_prune(new_state, game)

                if game.is_goal(new_state):
                    self.frontier = [new_state]
                    temp_frontier = []
                    break
                elif game.is_terminal(new_state):
                    self.leaves.append(new_state)
                    if is_pruned:
                        temp_frontier = []
                        break
                else:
                        temp_frontier.append(new_state)

                if is_pruned:
                    temp_frontier = [new_state]
                    break
                

        self.frontier += temp_frontier
                



    def is_redundant(self,state : State_model, game : Solitaire_controller):



        if state.prev_state != state:
            action = state.action
            

            if state.prev_state != state.prev_state.prev_state and not state.prev_state.action.get_talon:
                prev_action = state.prev_state.action

                if prev_action.from_row == -1 and state.foundations != state.prev_state.foundations:

                    if not action.get_talon or (action.from_row != -1 and action.to_row < len(state.board)) :
                        return True


            if not action.get_talon and action.from_row != -1:
                if action.to_row < len(state.board):
                    to_row = state.prev_state.board[action.to_row]
                else:
                    return False
                    
                from_row = state.prev_state.board[action.from_row]
                card = from_row[action.card_index]
                if action.card_index != 0 and len(to_row) > 0:
                    if from_row[action.card_index-1][0] == to_row[-1][0]:
                        if game.same_symbols(from_row,10) > game.same_symbols(state.board[action.to_row],10):
                            return True
                elif action.card_index == 0:
                    if len(to_row) == 0:
                        return True
                    else:
                        empty_rows = 0
                        kings = 0
                        king_in_talon = False

                        for row in state.board:
                            if row and row[0][0] == 'K':
                                kings += 1
                            elif len(row) == 0:
                                empty_rows += 1

                            
                        if game.draw_from_stock(state.stock,state.talon):
                            temp_action = Action_model()
                            temp_action.get_talon = True
                            temp_state = game.Result(state,temp_action)
                            
                            while temp_state.talon != state.talon:
                                if len(temp_state.talon) > 0 and len(state.talon) > 0 and temp_state.talon[0] == state.talon[0]:
                                    break
                                if len(temp_state.talon) > 0 and temp_state.talon[0][0] == 'K':
                                    king_in_talon = True
                                    break
                                temp_state = game.Result(temp_state,temp_action)
                                
                        
                        
                        if kings == 4 or king_in_talon and empty_rows == 0:
                            return True
                    
                
                    

        return False

    def new_prune(self, state : State_model, game : Solitaire_controller):

        length = 0
        last_length = 0    
        if state.action and not state.action.get_talon:

            if self.no_unkowns(state):
                if state.action.to_row >= len(state.board):
                    return True

            if game.is_terminal(state):
                if state.action.from_row != -1 and state.action.to_row < len(state.board):
                    return True

            if state.action.from_row < len(state.board):
                if state.action.card_index != 0 and state.board[state.action.from_row][-1] == '[]':
                    return False
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
                return True
        
        else:
            if state.action and not state.action.get_talon and state.action.to_row >= len(state.board):
                
                return True

        return False

    def talon_exist(self, new_state : State_model):
        for pair in self.talons:
            if pair[0] == new_state.talon and pair[1] == new_state.stock:
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
             
    def no_unkowns(self,state:State_model):
        for row in state.board:
            for card in row:
                if card == '[]':
                    return False
        
        for card in state.stock:
            if card == '[]':
                    return False
        
        for card in state.talon:
             if card == '[]':
                    return False

        return True

    
        



    def exists(self,new_state : State_model):
        for state in self.expanded:
                if state.equals(new_state):
                    return True         
        return False