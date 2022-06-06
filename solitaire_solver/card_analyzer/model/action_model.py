class Action_model():
    def __init__(self,card_index,from_row,to_row):
        self.prev_action = self
        self.card_index = card_index
        self.from_row = from_row
        self.to_row = to_row
        self.get_talon = False
        self.get_card = False