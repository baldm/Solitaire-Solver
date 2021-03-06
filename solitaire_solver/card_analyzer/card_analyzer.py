from .ai.Agent import Agent
from .ai.BFS import BFS
from .model.action_model import Action_model
from .model.state_model import State_model
from .controller.solitaire_controller import Solitaire_controller


class CardAnalyzer:

    def __init__(self):
        self.strategy = BFS()
        self.game = Solitaire_controller()
        self.agent = Agent(self.game, self.strategy)
        self.state = None

    #Give the AI a new card or board
    def update_card(self, card):
        #If its a card
        if len(card) == 1:
            #Insert where last card was moved from
            if self.state.action.get_talon or self.state.action.from_row == -1 :
                self.state.talon[0] = card[0]
            else:
                self.state.board[self.state.action.from_row][-1] = card[0]
                
            self.state.prev_state = self.state
        else:
            #It's a new board
            #A new game is created
            stock = ['[]'] * 24
            talon = []
            foundations = [[], [], [], []]
            self.state = State_model(card, foundations, stock, talon)

    def get_next_moves(self):
        
        # run ai
        self.state = self.agent.find_moves(self.state)

        # if new card is needed
        if self.state != False:

            temp_state = self.state

            output = []
            card_move = []
            card_to = []
            move_from = []
            get_talon = []
            #Get all actions executed, to reach current state
            while temp_state != temp_state.prev_state:
                action: Action_model = temp_state.action

                if action.get_talon:
                    if len(temp_state.prev_state.talon) > 0:
                        card_move.append(temp_state.prev_state.talon[0])
                    else:
                        card_move.append('')
                    card_to.append('')
                    move_from.append('')
                    get_talon.append(True)

                else:
                    get_talon.append(False)
                    # Appending the card we move
                    if action.from_row == -1:
                        card_move.append(temp_state.prev_state.talon[0])
                    else:
                        card_move.append(
                            temp_state.prev_state.board[action.from_row][action.card_index])
                    card_to.append(str(action.to_row))
                    move_from.append(str(action.from_row))
                temp_state = temp_state.prev_state

            #Reverse all lists, since we get the moves in reversed order
            card_to.reverse()
            card_move.reverse()
            move_from.reverse()
            get_talon.reverse()
            #Make a list with dictionaries, containing all moves
            for i in range(0, len(card_to)):
                output.append(
                    {'move_from': move_from[i], 'move_card': card_move[i], 'move_to': card_to[i], 'reg_card': '', 'get_talon': get_talon[i], 'game_over': False}
                )
            return output
        else:
            #The game can't be won
            return False

        
