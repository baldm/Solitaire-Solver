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

        # TODO: Her kan i implementer de objecter i skal bruge til det

    def _goes_here(self):
        # TODO: her kan i implentere hjælpe funktioner til at finde næste move
        pass

    def update_card(self, card):
        if len(card) == 1:
            if self.state.action.get_talon or self.state.action.from_row == -1 :
                self.state.talon[0] = card
            else:
                for row in self.state.board:
                    if row and row[-1] == '[]':
                        row[-1] = card
                        break
        else:
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

            while temp_state != temp_state.prev_state:
                action: Action_model = temp_state.action

                if action.get_talon:
                    card_move.append('')
                    card_to.append('')
                    move_from.append('')
                    get_talon.append(True)

                else:
                    get_talon.append(False)
                    # Appending the card we move
                    if action.from_row == -1:
                        card_move.append[temp_state.talon[0]]
                    else:
                        card_move.append(
                            temp_state.board[action.from_row][action.card_index])
                    card_to.append(str(action.to_row))
                    move_from.append(str(action.from_row))
                temp_state = temp_state.prev_state

            card_to.reverse()
            card_move.reverse()
            move_from.reverse()
            get_talon.reverse()

            for i in range(0, len(card_to)):
                output.append(
                    {'move_from': move_from[i], 'move_card': card_move[i], 'move_to': card_to[i], 'get_talon': get_talon[i]})
            return output
        else:
            return False

        # make list of moves and return them

       # [
       #     {'move_from': '3', 'move_card': '4H', 'move_to': '-1'},
       #     {'move_from': '4', 'move_card': '3S', 'move_to': '8'}
       # ]
