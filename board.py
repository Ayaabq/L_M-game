# هذا الكاس يعبر عن الرقعة 
# يتم تخزين فيه الرقعة بحد ذاتها ولا يركز بشكل كبير على القطع
# الرقعة من خيث الخلايا التي يجب ملئها والخلايا البلوك وحجم الرقعة ...
class Board:
    def __init__(self, size, target_cells, block_cells):
        self.size = size
        # بالبداية سنعرف مصفوفة ثنائية وستكون كلها فارغة اي تحولي كلمة فارغ
        self.grid = [['empty' for _ in range(size)] for _ in range(size)]
        self.target_cells = target_cells  
        self.block_cells = block_cells  
        
        # مكان الخلايا البلوك حنعلمو بكلمة بلوك
        for x, y in block_cells:
            self.grid[x][y] = 'blocked'

    def place_piece(self, piece, position):
        x, y = position
        if (x, y) not in self.block_cells:
            self.grid[x][y] = piece

    def is_empty(self, position):
        x, y = position
        return self.grid[x][y] == 'empty'

    def within_bounds(self, position):
        x, y = position
        return 0 <= x < self.size and 0 <= y < self.size

    def is_blocked(self, position):
       
        x, y = position
        return self.grid[x][y] == 'blocked'

    def all_targets_filled(self):
        return all(self.grid[x][y] != 'empty' for x, y in self.target_cells)
