
from utils import print_board  

class Solver:
    def __init__(self, game, search_algorithm):
        self.game = game
        self.search_algorithm = search_algorithm

    def find_solution(self):
        """Finds and prints the solution using the selected search algorithm."""
        solution = self.search_algorithm.solve()
        
        if solution:
            print("Solution found in moves:", len(solution))
            self.print_solution_steps(solution)
        else:
            print("No solution found.")

    def print_solution_steps(self, solution):
        """Applies each move in the solution sequence and prints the grid after each move."""
        print("Starting grid:")
        print_board(self.game.get_grid(), self.game.board.target_cells)  # Print initial state
        
        for move in solution:
            print(f"\nApplying move: {move}")
            self.game.make_move(move)
            print_board(self.game.get_grid(), self.game.board.target_cells)
