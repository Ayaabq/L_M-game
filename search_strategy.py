#في هذا الكلاس  يوجد كل خوارزميات البحث 
#يعني هو كلاس اب لكل الكلاسات تبع الخوارزميات 
from abc import ABC, abstractmethod

class SearchStrategy(ABC):
    def __init__(self, game):
        self.game = game
        self.visited = set()  # دايما في عنا سيت الفيزيتد

    @abstractmethod
    def solve(self):
        """هاد التابع بطبق خوارزمية البحث وبرجع خطوات الحل يعني الحركات لوصلنا للحل"""
        pass

    def get_state(self, game_instance):
        """
        هاد التابع برجع هاش تيبل للحالات يعني مشان ما نرجع لحالة مزارة
        """
        return tuple(tuple(row) for row in game_instance.get_grid())

    def generate_all_possible_moves(self, game_instance):
        
        # -- جنشوف الحركات الممكنة لكل قطعة --
        possible_moves = []
        movable_pieces = game_instance.get_movable_pieces()  
        grid = game_instance.get_grid() 

        for piece_pos in movable_pieces:
            for x in range(len(grid)):
                for y in range(len(grid[0])):
                    # print(x,y)
                    if grid[x][y] == 'empty':  
                        possible_moves.append((piece_pos, (x, y)))  

        return possible_moves  
