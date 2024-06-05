import numpy as np
import pandas as pd

# СТЕПЕННАЯ ФУНКЦИЯ

x = np.array(
    [99, 82, 77, 69, 52, 44, 31, 29, 28, 27.5]
)

y = np.array(
    [100, 115, 210, 270, 323, 478, 544, 564, 570, 574]
)

# Precalculations
X = np.log10(x)
Y = np.log10(y)

# Basic calculations

x_mean = np.mean(x)
y_mean_ = np.mean(y)
XY = X * Y
Y2 = np.power(Y, 2)
X2 = np.power(X, 2)

# Cherta functions
X_mean = np.mean(X)
Y_mean = np.mean(Y)
XY_mean = np.mean(XY)
Y2_mean = np.mean(Y2)
X2_mean = np.mean(X2)


# coef
A_: float = (XY_mean - X_mean * Y_mean) / (X2_mean - X_mean * X_mean)

# intercept
B_: float = Y_mean - A_ * X_mean

# function f(x)
y_func = np.power(10, B_) * np.power(x, A_)

# (y - y_func)^2
flag1 = (y - y_func) * (y - y_func)

# (y - y_mean)^2
flag2 = (y - y_mean_) * (y - y_mean_)

# Correlation
r_xy = np.sqrt( 1 - np.sum(flag1) / np.sum(flag2) )


# appeoximation error (non %)
A = np.abs( (y - y_func) / y_func )
A_mean = np.mean(A) 

# determination (non %)
R = r_xy * r_xy



data = {
    'x': x,
    'y': y,
    'X': X,
    'Y': Y,
    'XY': XY,
    'Y^2': Y2,
    'X^2': X2,
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
print(f"X_: {X_mean}")
print(f"Y_: {Y_mean}")
print(f"XY_: {XY_mean}")
print(f"X^2_: {X2_mean}")
print(f"Y^2_: {Y2_mean}")

print()
print("Function coefficients of (10^B*x^A)")
print(f"A: {A_}")
print(f"B: {B_}")
print(f"sigma_x: {np.sqrt(np.mean(x * x) - np.mean(x) * np.mean(x))}")
print(f"sigma_y: {np.sqrt(np.mean(y * y) - np.mean(y) * np.mean(y))}")

print()
print(f"Correlation: {r_xy}")
print(f"Determination: {R}")
print(f"Approximation error: {A_mean}")
print()