
    
import copy
from search_strategy import SearchStrategy


class HillClimbing(SearchStrategy):
    def __init__(self, game):
        super().__init__(game)

    def solve(self):
        current_game = copy.deepcopy(self.game)  
        current_state = self.get_state(current_game)  
        current_cost = self.evaluate_state(current_game)  

        if current_game.board.all_targets_filled(): 
            print("Solution found at the initial state.")
            return []  

        self.visited.clear()  
        self.visited.add(current_state) 
        move_sequence = [] 

        while True:
            possible_moves = self.generate_all_possible_moves(current_game)  
            best_neighbor = None
            best_move = None
            best_cost = current_cost

            
            for move in possible_moves:
                new_game = copy.deepcopy(current_game)  
                new_game.make_move(move)  
                new_state = self.get_state(new_game)  
                new_cost = self.evaluate_state(new_game)  # Evaluate the new state

                if new_cost < best_cost and new_state not in self.visited:
                    # If the neighbor is better and unvisited, select it
                    best_neighbor = new_game
                    best_move = move
                    best_cost = new_cost

            if best_neighbor and best_cost < current_cost:
                # Move to the best neighbor
                current_game = best_neighbor
                current_state = self.get_state(current_game)
                current_cost = best_cost
                self.visited.add(current_state)  
                move_sequence.append(best_move)  

                if current_game.board.all_targets_filled():
                    print("Congratulations! You filled all target cells and won the game!")
                    return move_sequence  # Immediately return after finding the solution
            else:
                # No better neighbor found, terminate (local maximum reached)
                if not current_game.board.all_targets_filled():
                    print("Local maximum reached or no solution found.")
                    return None  # No solution found
    
    

