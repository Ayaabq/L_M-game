# هذا الكلاس يمثل القعطة بحد ذاتها معدينة مغناطيسية ..


class Piece:
    def __init__(self, color, is_magnetic, position):
        self.color = color
        self.is_magnetic = is_magnetic
        self.position = position

    def __repr__(self):
        return f"{self.color} {'Magnetic' if self.is_magnetic else 'Metal'}"
        
        