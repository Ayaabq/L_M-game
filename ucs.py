import copy
from heapq import heappop, heappush  
from search_strategy import SearchStrategy

class UCS(SearchStrategy):
    def __init__(self, game):
        super().__init__(game)

    def solve(self):
        priority_queue = []
        initial_state = self.get_state(self.game)

        if self.game.board.all_targets_filled():
            return []  
            
        heappush(priority_queue, (0, self.game, []))
        self.visited.clear()
        self.visited.add(initial_state)

        while priority_queue:
            current_cost, current_game, move_sequence = heappop(priority_queue)

            if current_game.board.all_targets_filled():
                return move_sequence

            possible_moves = self.generate_all_possible_moves(current_game)

            for move in possible_moves:
                new_game = copy.deepcopy(current_game)
                new_game.make_move(move)
                new_state = self.get_state(new_game)

                if new_state not in self.visited:
                    self.visited.add(new_state)
                    new_cost = current_cost + 1
                    heappush(priority_queue, (new_cost, new_game, move_sequence + [move]))

        return None  
 