
from collections import deque
import copy
from search_strategy import SearchStrategy


import copy

class DFS(SearchStrategy):
    def __init__(self, game):
        super().__init__(game)

    def solve(self):
        
        if self.game.board.all_targets_filled():
            return []  

        self.visited.clear()  
        max_depth = 10  #  عمق شجرة البحث لان لو تركناها عراحتها كتير بتطول لتلاقي حل واصلا باللعبة مافي مرحلة بدا اكتر من عشر خطوات
        return self.dfs(self.game, [], 0, max_depth)

    def dfs(self, current_game, move_sequence, depth, max_depth):
        if depth > max_depth:
            
            return None
        
        current_state = self.get_state(current_game)
        if current_state in self.visited:
            
            return None

        self.visited.add(current_state)

        if current_game.board.all_targets_filled():
            # print(move_sequence)
            return move_sequence

        possible_moves = self.generate_all_possible_moves(current_game)

        # TODO:  أنو يدورعالأقصر يصير
        for move in possible_moves:
            new_game = copy.deepcopy(current_game)  
            new_game.make_move(move)

            
            solution = self.dfs(new_game, move_sequence + [move], depth + 1, max_depth)
            if solution:
                return solution  

        return None  

    
