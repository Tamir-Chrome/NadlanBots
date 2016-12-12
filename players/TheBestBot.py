from playerbase import PlayerBase
from utils import *


class TheBestBot(PlayerBase):
    def __str__(self):
        return "The Best Bot"

    def bid(self, player_state, available_locations, current_bid_by_player_id, current_highest_bid):
        if current_highest_bid >= player_state.money/2:
            return BidResponse(forfeit=True)
        return BidResponse(bid=current_highest_bid + 1)

    def bid_for_cheques(self, player_state, available_cheques):
        return min(player_state.cards)
