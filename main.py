# للأستاذة سالي سوف أضع تعليقات للتوضيح كيفية عمل مشروعي



from game import Game
from utils import load_levels_from_json

def main():
        #   وهنا نقرأ الملفjson بخزين المراحل بملف 

    levels = load_levels_from_json('levels.json')

    level = int(input("Choose a level (0 for level 1, 1 for level 2, etc.): "))
    game = Game(levels, level_index=level)
    game.run()

if __name__ == "__main__":
    main()

