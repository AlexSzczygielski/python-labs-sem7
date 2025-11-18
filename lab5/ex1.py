#ex1.py
#Calculates roots of the quadratic equation

import cmath
def solve_quad(a,b,c):
    delta = b**2 - 4*a*c
    sqrt_delta = cmath.sqrt(delta)
    return (-b + sqrt_delta) / (2*a), (-b - sqrt_delta) / (2*a)

def get_quad_str(a,b,c):
    return f"{a}x^2 + {b}x + {c}"

def print_quad_result(a,b,c):
    print(f"Quadratic equation: {get_quad_str(a,b,c)} has roots: {solve_quad(a,b,c)}")

if __name__ == "__main__":
    print_quad_result(1,5,6)
    print_quad_result(1,2,1)
    print_quad_result(1,0,1)
    