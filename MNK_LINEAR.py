import numpy as np
import pandas as pd

# Fill it

x = np.array(
    [50, 60, 70, 100, 40, 70, 40, 80, 90, 60]
)

y = np.array(
    [10, 12, 12, 19, 9, 14, 8, 16, 15, 11]
)


# Basic calculations
xy: np.array = x * y
y2 = np.power(y, 2)
x2 = np.power(x, 2)

# Cherta functions
x_mean = np.mean(x)
y_mean = np.mean(y)
xy_mean = np.mean(xy)
y2_mean = np.mean(y2)
x2_mean = np.mean(x2)

# linear coef
a: float = (xy_mean - x_mean * y_mean) / (x2_mean - x_mean * x_mean)

# linear intercept
b: float = y_mean - a * x_mean

# Linear function f(x)
y_func = a * x + b

# appeoximation error (non %)
A = np.abs( (y - y_func) / y_func )
A_mean = np.mean(A) 

# correlation (non %)
r_xy = a * np.sqrt( (x2_mean - (x_mean * x_mean)) / (y2_mean - (y_mean * y_mean)) )

# determination (non %)
R = r_xy * r_xy


data = {
    'x': x,
    'y': y,
    'xy': xy,
    'y^2': y2,
    'x^2': x2,
    'y_func': y_func,
    'A': A
}

df = pd.DataFrame(data)

print()
print(df)

print()
print("Cherta values (mean)")
print(f"x_: {x_mean}")
print(f"y_: {y_mean}")
print(f"xy_: {xy_mean}")
print(f"x^2_: {x2_mean}")
print(f"y^2_: {y2_mean}")

print()
print("Function coefficients of (ax+b)")
print(f"a: {a}")
print(f"b: {b}")
print(f"sigma_x: {np.sqrt(np.mean(x * x) - np.mean(x) * np.mean(x))}")
print(f"sigma_y: {np.sqrt(np.mean(y * y) - np.mean(y) * np.mean(y))}")

print()
print(f"Correlation: {r_xy}")
print(f"Determination: {R}")
print(f"Approximation error: {A_mean}")
print()