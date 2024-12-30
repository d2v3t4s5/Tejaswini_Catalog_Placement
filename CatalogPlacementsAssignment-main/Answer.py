import json
from sympy import symbols, Rational

x = symbols('x')  # Define x globally

def read_test_case(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data['keys']['n'], data['keys']['k'], data

def decode_y_values(data):
    points = []
    for key, value in data.items():
        if key != 'keys':
            x = int(key)
            base = int(value['base'])
            y = int(value['value'], base)
            points.append((x, y))
    return points

def lagrange_interpolation(points):
    n = len(points)
    polynomial = 0
    for i in range(n):
        xi, yi = points[i]
        li = 1
        for j in range(n):
            if i != j:
                xj, yj = points[j]
                li *= (x - xj) / (xi - xj)
        polynomial += yi * li
    return polynomial

def find_constant_term(polynomial):
    return polynomial.subs(x, 0)

# Run the code
n, k, data = read_test_case('input2.json')
points = decode_y_values(data)
polynomial = lagrange_interpolation(points)
c = find_constant_term(polynomial)
print(c)
