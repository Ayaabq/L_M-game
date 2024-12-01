# # سوف أضع تعليقات للتوضيح كيفية عمل مشروعي


from astar import AStar

from game import Game
from utils import load_levels_from_json
# اذا اردت لعب اللعبة بمفردك ازيل التعليقات وعلق تحت
# def main():
#         #   وهنا نقرأ الملفjson بخزين المراحل بملف 

#     levels = load_levels_from_json('levels.json')

#     level = int(input("Choose a level (0 for level 1, 1 for level 2, etc.): "))
#     game = Game(levels, level_index=level)
#     game.run()

# if __name__ == "__main__":
#     main()


from bfs import BFS  
from hill_climbing import HillClimbing
from dfs import DFS  
from solver import Solver
from ucs import UCS

def main():
    # Load game level, initialize game instance
    levels = load_levels_from_json('levels.json')

    level = int(input("Choose a level (0 for level 1, 1 for level 2, etc.): "))
    game = Game(levels, level_index=level)
    
    # Select search algorithm
    algorithm_choice = input("Choose search algorithm (BFS/DFS/UCS/HC for Hill Climbing/A*): ").strip().upper()
    search_algorithm = None
    
    if algorithm_choice == "BFS":
        search_algorithm = BFS(game)
    elif algorithm_choice == "DFS":
        search_algorithm = DFS(game)
    elif algorithm_choice == "UCS":  
        search_algorithm = UCS(game)
    elif algorithm_choice == "HC":  
        search_algorithm = HillClimbing(game)
    elif algorithm_choice == "A*":
        search_algorithm = AStar(game)
        print("solving...")
    # Ensure a valid algorithm was chosen
    if search_algorithm:
        solver = Solver(game, search_algorithm)
        solver.find_solution()
    else:
        print("Invalid algorithm choice.")

if __name__ == "__main__":
    main()










