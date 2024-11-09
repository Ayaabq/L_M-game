from collections import deque
import copy
from search_strategy  import SearchStrategy


class BFS(SearchStrategy):
    def __init__(self, game):
        super().__init__(game)

    def solve(self):
        queue = deque([(self.game, [])])  
        initial_state = self.get_state(self.game)

        if self.game.board.all_targets_filled():
            return []  

        self.visited.add(initial_state)

        while queue:
            current_game, move_sequence = queue.popleft()
            possible_moves = self.generate_all_possible_moves(current_game)

            for move in possible_moves:
                
                new_game = copy.deepcopy(current_game)
                new_game.make_move(move)
                new_state = self.get_state(new_game)

                if new_game.board.all_targets_filled():
                    return move_sequence + [move]

                if new_state not in self.visited:
                    # print(self.visited)
                    self.visited.add(new_state)
                    # print(self.visited)
                    queue.append((new_game, move_sequence + [move]))
        # print(queue.pop())
        
        return None
