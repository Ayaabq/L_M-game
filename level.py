# هذا الكلاس عبارة عن كلاس الليفل 
# تعبر عن اللعبة بالحالة البدائية لكل مرحلة  intityيمكننا اعتبارة ك
# وهو أعلى طبقة بتتواصل مع الجيسون فورا 

from piece import Piece

class Level:
    def __init__(self,board_size  , target_cells,block_cells,pieces):
        self.board_size = board_size
        self.target_cells = target_cells
        self.block_cells = block_cells
        self.pieces = pieces


# هون عرفت  مرحلة وبعدين مصفوفة مراحل، قبل ما ضيف ملف الجيسون كنت عم استعملا 
# هلق ما الها استعمال 
l1 = Level(
    board_size=5,
    target_cells=[(0,2), (1, 3), (4,4)],
    block_cells=[(2 , 2), (3,3)],
    pieces=[
        Piece(color="red",is_magnetic=True, position=(0,0)),
        Piece(color="purple", is_magnetic=True, position=(1 ,1)),
        Piece(color="purple" , is_magnetic=True ,position=(1 ,2)),
        Piece(color="grey" ,is_magnetic=False, position=(2,2))
    ]
)

levels = [l1]
