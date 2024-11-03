# في هذا الملف يوجد توابع مساعدة فقط لا علاقة لها بأي كلاس

from piece import Piece  
import json
from level import Level


#التابع المسؤول عن طباعة الرقعة في كل مرة 
def print_board(grid, target_cells):
    color_abbreviations = {
        "red": "R",
        "purple": "P",
        "grey": "G",
        "blocked": "X"  
    }
    
    for x, row in enumerate(grid):
        row_display = " | ".join(
            "O" if (x, y) in target_cells and cell == 'empty' 
            else color_abbreviations.get(cell.color, " ") if isinstance(cell, Piece)  
            else color_abbreviations.get(cell, " ")
            for y, cell in enumerate(row)
        )
        print(row_display)
        
        if x < len(grid) - 1:
            print("-" * (4 * len(grid) - 1))


# هذا التابع يقوم بأخذ مسار ملف الجيسون وثم يحوله إلى مصفوفة اوبجكتات من نوع ليلفل 
def load_levels_from_json(json_file):
    with open(json_file, 'r') as f:
        data = json.load(f)

    levels = []
    for level_data in data:
        pieces = [Piece(piece_data['color'], piece_data['is_magnetic'], piece_data['position']) for piece_data in level_data['pieces']]
        level = Level(
            board_size=level_data['board_size'],
            target_cells=level_data['target_cells'],
            block_cells=level_data['block_cells'],
            pieces=pieces
        )
        levels.append(level)
    
    return levels
