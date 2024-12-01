import copy
from heapq import heappop, heappush  # Priority Queue
from search_strategy import SearchStrategy

class AStar(SearchStrategy):
    def __init__(self, game):
        super().__init__(game)

    def solve(self):
        """
        Implements A* search to find the optimal solution path.
        Uses a priority queue where nodes are evaluated by the sum of their cost and heuristic.
        """
        priority_queue = []  # Priority queue to hold nodes (cost + heuristic, game state, moves)
        initial_state = self.get_state(self.game)
        initial_heuristic = self.evaluate_state(self.game)  # Initial heuristic based on empty target cells

        # If the initial state is already solved
        if self.game.board.all_targets_filled():
            return []  # No moves needed

        heappush(priority_queue, (initial_heuristic, 0, self.game, []))  # (f = h + g, g, game, path)
        self.visited.clear()  # Reset visited states
        self.visited.add(initial_state)

        while priority_queue:
            f_cost, g_cost, current_game, move_sequence = heappop(priority_queue)

            if current_game.board.all_targets_filled():  # Solution found
                return move_sequence

            possible_moves = self.generate_all_possible_moves(current_game)

            for move in possible_moves:
                new_game = copy.deepcopy(current_game)  # Create a new game state for the move
                new_game.make_move(move)  # Apply the move
                new_state = self.get_state(new_game)  # Get the state hash
                h_cost = self.evaluate_state(new_game)  # Heuristic (remaining empty target cells)

                if new_state not in self.visited:
                    self.visited.add(new_state)
                    new_g_cost = g_cost + 1  # Cost to reach this state (increment by 1 per move)
                    f_cost = new_g_cost + h_cost  # Total cost (f = g + h)
                    heappush(priority_queue, (f_cost, new_g_cost, new_game, move_sequence + [move]))

        return None  # No solution found

