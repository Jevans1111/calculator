from calculator import add, subtract, multiply, divide, CircleArea

def test_add():
   assert add(2, 3) == 5

def test_divide():
   assert divide(6, 2) == 3

def test_multiply():
   assert multiply(4, 8) == 32

def test_subtract():
   assert subtract(9, 5) == 4

def test_divide_uneven():
   assert divide(5, 2) == 2.5
   
def test_add_negative():
   assert add(-2, -3) == -5

def test_multiply_by_zero():
   assert multiply(7, 0) == 0

def test_circleArea():
   assert CircleArea(-4) == "Error"
