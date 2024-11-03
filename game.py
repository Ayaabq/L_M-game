
# في هذا الكلاس يتم تعريف قواعد وقوانين اللعب  وطريقة الحركة 

from board import Board
from piece import Piece
from utils import print_board


class Game:
    def __init__(self,levels, level_index=0):
        self.level = levels[level_index]
        self.board = Board(self.level.board_size, self.level.target_cells, self.level.block_cells)
        self.pieces = self.level.pieces
        # مصفوفة الستيت تخزن بكل مرة حالة الرقعة ولكن افكر في تغيير هذه البنية من أجل خوارزميات البحث القادمة
        self.states = []
        
        # نقوم بإضافة القطع على الرقعة ونحفظ الحالة البدائية
        for piece in self.pieces:
            self.board.place_piece(piece, piece.position)
        self.save_state()
    
    # هذا التابع الذي يقوم بتخزين الحالة 
    # بينسخ الرقعة وبعدين بضيف النسخة عالليست مشان ما ياخد ريفرنس للرقعة تقوم تتغير بعدين 
    def save_state(self):
        grid_copy = [row[:] for row in self.board.grid]
        self.states.append(grid_copy)

    # هاد التابع بشيك اذا هي الستيت او يعني هي الرقعة وصلنالها من قبل 
    def has_reached_state(self, grid):
        return any(grid == state for state in self.states)
    
    # هاد التابع بشوف اذا ممكن القطعة تتحرك او لا
    def can_move_piece(self ,position,direction):
        
        # حنأسند البوزيشن لمتغيرات
        x, y = position

        # بناء على ستريبنغ الاتجاه ححد البوزيشن الجديد
        if direction == "up":
            new_position = (x-1,y)
        elif direction == "down":
            new_position = (x +1, y)
        elif direction == "left":
            new_position = (x, y-1)
        elif direction == "right":
            new_position = (x ,y +1)
        else:
            
            return False
        
        # عم بتأكد اذا البوزيشن الجديد جوا حدود المصفوفة
        if not self.board.within_bounds(new_position):
            return False

        # بنشيك انو مالو فاضي 
        is_empty= self.board.is_empty(new_position)
        is_not_blocked =not self.board.is_blocked(new_position)
        
        return is_empty and is_not_blocked

    # هاد التابع  بحرك باتجاه البوزيشن يلي بياخدو 
    # يعني بنستخدمو مع القطع الحمرا 
    # بنعطيه البوزيشن الجديد تبعها وهو بحرك باتجاهو 
    # يعني بيجذب القطع باتجاهو
    def move_adjacent_pieces_towards(self, new_position):
        # عم أسند البوزيشن لمتغيرات
        x,y=new_position

        # هيك بنحرك عاليمين
        for j in range(y-1, -1, -1):
            piece = self.board.grid[x][j]
            if piece != 'empty':  
                self.move_piece_to((x,j), (x,j+1))
        # عاليسار
        for j in range(y + 1, self.board.size):
            piece = self.board.grid[x][j]
            if piece != 'empty':
                self.move_piece_to((x , j ), (x, j-1 ))
        
        # من فوق
        for i in range(x-1, -1 , -1 ):
            piece = self.board.grid[i][y]
            if piece != 'empty':
                self.move_piece_to((i,y), (i+1, y))
        
        
        # من تحت
        for i in range(x+1, self.board.size):
            piece = self.board.grid[i][y]
            if piece != 'empty':
                self.move_piece_to( ( i , y), (i-1, y))

    
    
   # هاد التابع لتحريك القطع هاد بستدعيه من جوا اللعبة يعني مو يلي اليوزر بحرك فيه القطع
   # يعني هون ما بعالج ااذا في حالات دحل غلط لان اصلا عم استدعيه من توابع اللعبة  اما يلي بحرك فيه اليوزر بعالج حالات اكتر 
    def move_piece_to(self,current_position , new_position ):
        # عم نشيك انو البوزيشن مو برا المصفوفة ومو فاضي يعني فيو قطعة وجوا المصفوفة
        if self.board.within_bounds(new_position) and self.board.is_empty(new_position):
            # هون حنجيب القطعة
            piece = self.board.grid[current_position[0]][current_position[1]]

            # حنتأكد انو الشي يلي بالبوزيشن هو قطعة معدنية او حديدية يعني مالو بلوك مثلا
            if isinstance(piece, Piece):
                # هون حنحرك للبوزيشن الجديد
                self.board.grid[current_position[0]][current_position[1]]='empty'
                piece.position =new_position
                self.board.place_piece( piece , new_position)


   
    #هاد التابع لما اليوزر بدو يحرك
    def move_piece(self, current_position, new_position):
        x, y = current_position

        # بنتأكد  انو البوزيشن يلي اختارو اليوزر ليحركو جوا حدود الغريد
        if not self.board.within_bounds(current_position ):
            print(" current_position is out of buonds"  )
            return

        # بنتأكد من البوزيشن الجديد انو جوا حدود الغريد
        if not self.board.within_bounds(new_position):
            print("new position out of bound ")
            return

        # بنشبك انو البوزيشن الجديد متاح
        if not self.board.is_empty(new_position) or self.board.is_blocked(new_position):
            print("possition occupied or block")
            return

        # حنجيب القعطة يلي بالبوزيشن الحالي
        piece = self.board.grid[x][y]

        # بنتأكد انو القطعة بتقدر تتحرك مالها رمادية مثلا
        if piece == 'empty':
            print("no piece at the specefied position ")
            return
        if piece.color == "grey":
            print("you cannot move a grey piece directly")
            return

        # هون حنغير البوزيشن
        # بنفضي القديم وبنعبي الجديد
        self.board.grid[x][y] ='empty'
        piece.position=new_position
        self.board.place_piece(piece , new_position )
        print(f"moved {piece} to {new_position}")

        # هون بنشوف كيف الحركة حتحرك باقي القطع يعني اذا حمرة شو واذا بنفسجية شو
        if piece.color == "red":
            self.move_adjacent_pieces_towards(new_position)
        elif piece.color == "purple":
            self.move_adjacent_pieces_away(new_position)

        # بنخزن الحالة لان يعني بنكون لعبنا مرحلة وخلصنا 
        self.save_state()

        # وبكل مرة بنشيك اذا فزنا  
        if self.board.all_targets_filled():
            print("Congratultions! you fill all target cell and win the game!")
            exit()

    
    

    # def move_connected_pieces_away(self, new_position, direction):
    #     move=False
    #     if direction not in ["up", "down", "left", "right"]:
    #         raise ValueError("Invalid direction. Must be 'up', 'down', 'left', or 'right'.")
        
    #     line_of_pieces = self.get_connected_pieces(new_position, direction)
        
    #     # if not line_of_pieces:
    #     #     return False  

    #     last_piece_position = line_of_pieces[-1]
    #     lx, ly = last_piece_position

    #     if direction == "up":
    #         after_line_position = (lx - 1, ly)
    #     elif direction == "down":
    #         after_line_position = (lx + 1, ly)
    #     elif direction == "left":
    #         after_line_position = (lx, ly - 1)
    #     elif direction == "right":
    #         after_line_position = (lx, ly + 1)

    #     if self.board.within_bounds(after_line_position) and self.board.is_empty(after_line_position):
    #         # Move each piece in the line one step away in the specified direction
    #         for pos in reversed(line_of_pieces):
    #             self.move_piece_away(pos, direction)
    #         move= True  # Movement occurred
    #     return move

      #هات التابع بنستعملو لتحريك القطع بعيدا عن قطعة النبفسجية 
      # البنفسجية بتحرك قطعة او مجموعة قطع متصلة فهاد التابع بياخد اول قطعة قريبة من البنفسجية وبشوف اذا الها قطع ملزوقين فيها وبحركن معها
    def move_connected_pieces_away(self,new_position,direction):
        move = False

        if direction not in ["up","down" ,"left","right" ]:
            raise ValueError("invald direction")
            # if not line_of_pieces:
                 #     return False  

        # بنجيب ليستة قطع متصلة من التابع تبع الغيت
        line_of_pieces = self.get_connected_pieces(new_position ,direction)

        # عم ندور عالبوزيشن او الخطوة يلي بعد القطع
        last_piece_position =line_of_pieces[-1]
        lx,ly =last_piece_position

        #بنحدد المكان الجديد بعد القطع
        if direction =="up":
            after_line_position = (lx-1, ly)
        elif direction=="down":
            after_line_position = (lx+1, ly)
        elif direction=="left":
            after_line_position = (lx, ly-1 )
        elif direction == "right":
            after_line_position = (lx, ly+1 )

        # بنحرك القطعة اذا ممكن
        if self.board.within_bounds(after_line_position) and self.board.is_empty(after_line_position):
            for pos in reversed(line_of_pieces):
                self.move_piece_away(pos,direction)
            move=True

        return move


    
     # هاد التابع بشوف مجاورات النهدية مشان يدفشن ويحركن
    # جواتو بنستدعي التابع يلي فوقو تبع التحريك
    # يعني هاد ما بحرك فعليا بس شغلتو يجب المجاورات ويبعتن لهداك
    def move_adjacent_pieces_away(self,new_position):
        directions =["up","down","left", "right"  ]

        
        for direction in directions:
            x,y= new_position
            while True:
                # حمخزن الاحداثيات قبل ما تتغير
                x1,y1 = x, y

                # حنغير الاحداثيات بناء عالاتجاه
                if direction =="up":
                    x-=1
                elif direction== "down":
                    x+=1
                elif direction == "left":
                    y-=1
                elif direction =="right":
                    y+=1

                # بنوقف اذا طلعنا برا المصفوفة
                if not self.board.within_bounds((x, y)):
                    break

                # بنستدعي تابع التحرك اذا لقينا قطعة يعني مالا فاضية ولا بلوك
                if self.board.grid[x][y]!='empty' and   self.board.grid[x][y] !='block':
                    if self.move_connected_pieces_away((x1,y1) , direction):
                        break

 #هاد التابع بجيب الخلايا يلي فيها قطع متصلين
    def get_connected_pieces(self,  start_position ,direction):
        connected =[]
        x,  y =start_position
        while True:
            if direction== "up":
                x-=1
            elif direction == "down":
                x+=1
            elif direction == "left":
                y-=1
            elif direction == "right":
                y+=1
            if not self.board.within_bounds((x, y)) or self.board.is_empty((x, y)):
                break
    
            connected.append((x, y))
            
        return connected

    def get_direction(self, from_position, to_position):
        fx, fy = from_position
        tx, ty = to_position
        if fx == tx:
            return "right" if fy < ty else "left"
        elif fy == ty:
            return "down" if fx < tx else "up"
    # هاد التابع بحرك قطعة وحدة بعكس جهة البنفسحية
    # شغلتو انو بنستدعيه من التابع يلي بحرك القطع المتصلة فوق
    def move_piece_away(self, current_position, direction):
        cx, cy = current_position

        if direction == "up":
            new_position = (cx-1, cy)
        elif direction == "down":
            new_position = (cx+1, cy)
        elif direction == "left":
            new_position = (cx, cy-1)
        elif direction == "right":
            new_position =(cx, cy+1)
        #حنصل عم نحرك بالاتجاه لحتى نلاقي خلية فاضية
        while self.board.within_bounds(new_position) and not self.board.is_empty(new_position):
            if direction == "up":
                new_position = (new_position[0]- 1 , new_position[1])
            elif direction == "down":
                new_position = (new_position[0]+1 , new_position[1])
            elif direction == "left":
                new_position = (new_position[0],new_position[1]-1)
            elif direction == "right":
                new_position = (new_position[0],new_position[1]+ 1 )
        #اذا لقينا خلية فاضية وجوا حدود المصفوفة بنحرك
        if self.board.within_bounds(new_position) and self.board.is_empty(new_position):
            piece = self.board.grid[cx][cy]
            if isinstance(piece, Piece):
                self.board.grid[cx][cy] = 'empty'
                piece.position = new_position
                self.board.place_piece(piece, new_position)

    def run(self):
        while True:
            print_board(self.board.grid, self.level.target_cells)
            print("Target cels:", self.level.target_cells)

            try:
                current_x = int(input("Enter the row of the piece to move: "))
                current_y = int(input("Enter the column of the piece to move: "))
                new_x = int(input("Enter the new row: "))
                new_y = int(input("Enter the new column: "))
                self.move_piece((current_x, current_y), (new_x, new_y))
            except ValueError:
                print("Invalid input, enter numbers.")
    
    
    
    
  