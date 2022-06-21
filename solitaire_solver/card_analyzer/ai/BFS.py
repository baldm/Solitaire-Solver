
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
            if len(self.leaves) > 80 or (len(self.expanded )> 2000 and len(self.frontier )> 15):
                break
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
        #Get all possible actions
        actions : list[Action_model] = game.Actions(state)
        temp_frontier = []
        
        #For each Action
        for action in actions:
            #Generate new state
            new_state = game.Result(state,action)
            #If the state doesnt exit, the talon doesnt exist and the move is not redundant
            if not (self.exists(new_state) or (self.talon_exist(new_state) and action.get_talon) or self.is_redundant(new_state,game) ):
                self.expanded.append(new_state)
                #If the talon doesnt exist, append to list
                if not self.talon_exist(new_state):
                    self.talons.append([new_state.talon,new_state.stock])
                #Check if all other child states needs to be pruned
                is_pruned = self.new_prune(new_state, game)

                #Check if state is the goal
                if game.is_goal(new_state):
                    self.frontier = [new_state]
                    temp_frontier = []
                    break
                #Check if state is a leaf
                elif game.is_terminal(new_state):
                    self.leaves.append(new_state)
                    #If other childstates needs to be pruned
                    if is_pruned:
                        temp_frontier = []
                        break
                else:   
                    #Add to frontier
                    temp_frontier.append(new_state)
                #If other childstates needs to be pruned
                if is_pruned:
                    temp_frontier = [new_state]
                    if self.no_unkowns(new_state):
                        self.frontier = []
                    break
        #Making sure only one action for each card is generated
        for index,state in enumerate(temp_frontier):
            #If it is not the first state
            if index != 0:
                #Define prev_state and prev_action as well as current action
                prev_state = state.prev_state
                prev_action = temp_frontier[index-1].action
                action = state.action
                #If neither of the actions is get_talon
                if not action.get_talon and not prev_action.get_talon:
                    #Defines card which was moved
                    if action.from_row == -1:
                        card = prev_state.talon[0]
                    else:
                        card = prev_state.board[action.from_row][action.card_index]
                    
                    #defines card which were moved in prev action
                    if prev_action.from_row == -1:
                        prev_card = prev_state.talon[0]
                    else:
                        prev_card = prev_state.board[prev_action.from_row][prev_action.card_index]
                    
                    # If its the same card and the card is moved to the Tableau in both cases
                    if prev_card == card and action.to_row < len(state.board) and prev_action.to_row < len(state.board):

                        #Remove the state which is evaluated as worst
                        if game.same_symbols(state.board[action.to_row], 10)  > game.same_symbols(temp_frontier[index-1].board[prev_action.to_row],10):
                            temp_frontier.pop(index-1)
                        else:
                            temp_frontier.pop(index)
                        
        #Add the temp frontier to the frontier
        self.frontier += temp_frontier
                



    def is_redundant(self,state : State_model, game : Solitaire_controller):


        # If the state is not the initial state
        if state.prev_state != state:
            #Define action
            action = state.action
            
            #If last parent is not the initial state and last action wasnt to get talon
            if state.prev_state != state.prev_state.prev_state and not state.prev_state.action.get_talon:
                # Define prev action
                prev_action = state.prev_state.action
                #If prev action was to move from talon to foundation
                if prev_action.from_row == -1 and state.foundations != state.prev_state.foundations:
                    # If this action is not to get a new talon or to move a card from Tableau to Foundation
                    if not action.get_talon or (action.from_row != -1 and action.to_row < len(state.board)) :
                        #Then the move is redundant
                        return True

            #If a card is moved from the Tableau
            if not action.get_talon and action.from_row != -1:
                #If the card is moved to another row in the Tableau
                if action.to_row < len(state.board):
                    #Define row it was moved to
                    to_row = state.prev_state.board[action.to_row]
                else:
                    #The move is never redundant, if you move to foundation
                    return False
                #Define the row you move from, before the move is made
                from_row = state.prev_state.board[action.from_row]
                # If the card is not the bottom of one pile, and is moved to another pile in the Tableau
                if action.card_index != 0 and len(to_row) > 0:
                    #If the card is not revealing a new card
                    if from_row[action.card_index-1][0] == to_row[-1][0]:
                        #If the move results in a worse state
                        if game.same_symbols(from_row,10) > game.same_symbols(state.board[action.to_row],10):
                            return True
                #If the card is in the bottom of a row
                elif action.card_index == 0:
                    #If the card is moved to an empty row
                    if len(to_row) == 0:
                        #The move is redundant
                        return True
                    else:
                        
                        empty_rows = 0
                        kings = 0
                        king_in_talon = False

                        for row in state.board:
                            #If the first card in row is a king
                            if row and row[0][0] == 'K':
                                kings += 1
                            #If the row is empty
                            elif len(row) == 0:
                                empty_rows += 1

                        #If it is possible to draw from stock
                        if game.draw_from_stock(state.stock,state.talon):
                            temp_action = Action_model()
                            temp_action.get_talon = True
                            temp_state = game.Result(state,temp_action)
                            #Define if a king is available in current sequence of stock
                            while temp_state.talon != state.talon:
                                if len(temp_state.talon) > 0 and len(state.talon) > 0 and temp_state.talon[0] == state.talon[0]:
                                    break
                                if len(temp_state.talon) > 0 and temp_state.talon[0][0] == 'K':
                                    king_in_talon = True
                                    break
                                temp_state = game.Result(temp_state,temp_action)
                                
                        
                        # If there is 4 kings in the Tableau or no kings are available
                        #and there is no empty rows before the move
                        if kings == 4 or king_in_talon and empty_rows == 0:
                            #Then the move is redundant
                            return True
                    
                
                    

        return False

    def new_prune(self, state : State_model, game : Solitaire_controller):

        length = 0
        last_length = 0
        shortest_length = 100   
        if state.action and not state.action.get_talon:
            # If all cards are known, and a move puts a card into foundation
            if self.no_unkowns(state):
                if state.action.to_row >= len(state.board):
                    return True
            # If we get a terminal state by removing a card from the board
            if game.is_terminal(state):
                if state.action.from_row != -1 and state.action.to_row < len(state.board):
                    return True
            # If you move to a row on Tableau
            if state.action.from_row < len(state.board):
                # If it results in a terminal state
                if state.action.card_index != 0 and state.board[state.action.from_row][-1] == '[]':
                    return False

        #Find the length of the largest foundation           
        for index,foundation in enumerate(state.foundations):
            for foundation in state.foundations:
                if len(foundation) > length:
                    length = len(foundation)
                if len(foundation) < shortest_length:
                    shortest_length = len(foundation)
                if len(state.prev_state.foundations[index]) > last_length:
                    last_length = len(state.prev_state.foundations[index])

        # If prev_states longest foundation is shorter than current states longest foundation
        if length > last_length:
            for foundation in state.foundations:
                # If all foundations is either same length as or one less than the longest pile
                if len(foundation) != length and len(foundation) != (length -1) :

                    break
            else:
                return True
        
        else:
            # If the card is moved to foundation from the board, and the longest Foundation in prev_state has same length as the longest in current
            if state.action and not state.action.get_talon and state.action.to_row >= len(state.board) and state.action.from_row != -1:
                #If it is the shortest list in foundation
                if len(state.foundations[state.action.to_row%len(state.board)]) == shortest_length:
                    return True

        return False

    def talon_exist(self, new_state : State_model):
        for pair in self.talons:
            if pair[0] == new_state.talon and pair[1] == new_state.stock:
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