class Rectangle:

  def __init__(self, width, height):
    self.height = height
    self.width = width

  def __str__(self):
    return "Rectangle(width={0}, height={1})".format(self.width, self.height)

  def set_height(self, new_height):
    self.height = new_height

  def set_width(self, new_width):
    self.width = new_width

  def get_area(self):
    return (self.height * self.width)

  def get_perimeter(self):
    return ((2 * self.height) + (2 * self.width))

  def get_diagonal(self):
    return ((self.height ** 2 + self.width ** 2) ** .5)

  def get_picture(self):
    # check if width or height > 50
    if self.height > 50 or self.width > 50:
      return "Too big for picture."

    # create picture
    picture = ""
    for i in range(self.height):
      current_line = ""
      for j in range(self.width):
        current_line += '*'
        
      current_line += '\n'
      picture += current_line

    return picture

  def get_amount_inside(self, another_shape):
    amount = (self.get_area() // another_shape.get_area())
    
    return amount

    
class Square(Rectangle):
  
  def __init__(self, side):
    self.height = side
    self.width = side

  def set_side(self, side):
    self.height = side
    self.width = side

  def __str__(self):
    return "Square(side={0})".format(self.width)

  
    
