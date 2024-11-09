# # للأستاذة سالي سوف أضع تعليقات للتوضيح كيفية عمل مشروعي



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
from dfs import DFS  
from solver import Solver

def main():
    # Load game level, initialize game instance
    levels = load_levels_from_json('levels.json')

    level = int(input("Choose a level (0 for level 1, 1 for level 2, etc.): "))
    game = Game(levels, level_index=level)
    
    # Select search algorithm
    algorithm_choice = input("Choose search algorithm (BFS/DFS): ").strip().upper()
    search_algorithm = None
    
    if algorithm_choice == "BFS":
        search_algorithm = BFS(game)
    elif algorithm_choice == "DFS":
        search_algorithm = DFS(game)

    # Ensure a valid algorithm was chosen
    if search_algorithm:
        solver = Solver(game, search_algorithm)
        solver.find_solution()
    else:
        print("Invalid algorithm choice.")

if __name__ == "__main__":
    main()










