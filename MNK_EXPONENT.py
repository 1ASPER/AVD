import numpy as np
import pandas as pd

# Fill it

x = np.array(
    [50, 60, 70, 100, 40, 70, 40, 80, 90, 60]
)

y = np.array(
    [10, 12, 12, 19, 9, 14, 8, 16, 15, 11]
)


# Precalculations
Y = np.log10(y)

# Basic calculations
x_mean = np.mean(x)
y_mean__ = np.mean(y)
Yx: np.array = Y * x
Y2 = np.power(Y, 2)
x2 = np.power(x, 2)

# Cherta functions
x_mean = np.mean(x)
Y_mean = np.mean(Y)
Yx_mean = np.mean(Yx)
Y2_mean = np.mean(Y2)
x2_mean = np.mean(x2)


# сoef
A_: float = (Yx_mean - x_mean * Y_mean) / (x2_mean - x_mean * x_mean)

# intercept
B_: float = Y_mean - A_ * x_mean

# Exponentional function f(x)
y_func = np.power(10, A_ * x + B_)

# (y - y_func)^2
flag1 = (y - y_func) * (y - y_func)

# (y - y_mean)^2
flag2 = (y - y_mean__) * (y - y_mean__)

# Correlation
r_xy = np.sqrt( 1 - (np.sum(flag1) / np.sum(flag2)) )

# appeoximation error (non %)
A = np.abs( (y - y_func) / y_func )
A_mean = np.mean(A) 

# determination (non %)
R = r_xy * r_xy


data = {
    'x': x,
    'y': y,
    'Y': Y,
    'xY': Yx,
    'Y^2': Y2,
    'x^2': x2,
    'y_func': y_func,
    '(y - y_func)^2': flag1,
    '(y - y_mean_)^2': flag2,
    'A': A
}

df = pd.DataFrame(data)

print()
print(df)

print()
print("Cherta values (mean)")
print(f"x_: {x_mean}")
print(f"Y_: {Y_mean}")
print(f"xY_: {Yx_mean}")
print(f"x^2_: {x2_mean}")
print(f"Y^2_: {Y2_mean}")

print()
print("Function coefficients of ( 10^(A*x+B) )")
print(f"A: {A_}")
print(f"B: {B_}")
print(f"sigma_x: {np.sqrt(np.mean(x * x) - np.mean(x) * np.mean(x))}")
print(f"sigma_y: {np.sqrt(np.mean(y * y) - np.mean(y) * np.mean(y))}")

print()
print(f"Correlation: {r_xy}")
print(f"Determination: {R}")
print(f"Approximation error: {A_mean}")
print()