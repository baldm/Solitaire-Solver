from .ai.Agent import Agent
from .ai.BFS import BFS
from .model.action_model import Action_model
from .model.state_model import State_model
from .controller.solitaire_controller import Solitaire_controller

class CardAnalyzer:

    def __init__(self,board):
        self.card_info = ""
        stock = ['[]'] * 24
        talon = []
        foundations = [[],[],[],[]]


        strategy = BFS()
        self.game = Solitaire_controller()
        self.agent = Agent(self.game,strategy)
        self.state = State_model(board,foundations,stock,talon)
    
        
        

        # TODO: Her kan i implementer de objecter i skal bruge til det

    def _goes_here(self):
        # TODO: her kan i implentere hjælpe funktioner til at finde næste move
        pass
    


    def update_card(self,card):
        if self.state.action.from_row == -1:
            self.state.talon[0] = card
        else:
            for row in self.state.board:
                if row and row[-1] == '[]':
                    row[-1] = card
                    break
            
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
            get_talon= []

            while temp_state != temp_state.prev_state:
                action : Action_model = temp_state.action

                if action.get_talon:
                    card_move.append('')
                    card_to.append('')
                    move_from.append('')
                    get_talon.append(True)

                else:
                    get_talon.append(False)
                #Appending the card we move
                    if action.from_row == -1:
                        card_move.append[temp_state.talon[0]]
                    else:
                        card_move.append(temp_state.board[action.from_row][action.card_index])
                    card_to.append(action.to_row)
                    move_from.append(action.from_row)
                temp_state = temp_state.prev_state

                
            card_to.reverse()
            card_move.reverse()
            move_from.reverse()
            get_talon.reverse()


            values = [move_from,card_move,card_to,get_talon]
            keys = ['move_from','move_card','move_to','get_talon']
            output = dict(zip(keys,values))



        # make list of moves and return them
        return output
        
       # [
       #     {'move_from': 3, 'move_card': '4H', 'move_to': '5C'},
       #     {'move_from': 4, 'move_card': '3S', 'move_to': '4H'}
       # ]
