def get_area(x1, y1, x2, y2, x3, y3):
    return abs((x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)) / 2.0)

def is_inside(x1, y1, x2, y2, x3, y3, x, y):
    # Main triangle area
    A = get_area(x1, y1, x2, y2, x3, y3)
    
    # Three smaller triangles area
    A1 = get_area(x, y, x1, y1, x2, y2)
    A2 = get_area(x, y, x2, y2, x3, y3)
    A3 = get_area(x, y, x1, y1, x3, y3)
    
    # Check if sum is equal
    return A == (A1 + A2 + A3)

# Example: Triangle corners (0,0), (20,0), (10,30) aur point (10,15)
if is_inside(0, 0, 20, 0, 10, 30, 10, 15):
    print("Point inside!")
else:
    print("Point outside!")