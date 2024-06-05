import numpy as np
import pandas as pd

# Fill it

x = np.array(
    [50, 60, 70, 100, 40, 70, 40, 80, 90, 60]
)

y = np.array(
    [10, 12, 12, 19, 9, 14, 8, 16, 15, 11]
)


z = 1 / x
zy = z * y
z2 = np.power(z, 2)
y2 = np.power(y, 2)

# Cherta functions
x_mean = np.mean(x)
y_mean___ = np.mean(y)
z_mean = np.mean(z)
y_mean = np.mean(y)
zy_mean = np.mean(zy)
y2_mean = np.mean(y2)
z2_mean = np.mean(z2)

# coef
a: float = (zy_mean - z_mean * y_mean) / (z2_mean - z_mean * z_mean)

# intercept
b: float = y_mean - a * z_mean

# function f(x)
y_func = b + a * z

# (y - y_func)^2
flag1 = (y - y_func) * (y - y_func)

# (y - y_mean)^2
flag2 = (y - y_mean___) * (y - y_mean___)

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
    'z': z,
    'zy': zy,
    'y^2': y2,
    'z^2': z2,
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
print(f"z_: {z_mean}")
print(f"y_: {y_mean}")
print(f"zy_: {zy_mean}")
print(f"z^2_: {z2_mean}")
print(f"y^2_: {y2_mean}")

print()
print("Function coefficients of (b+a*z)")
print(f"A: {a}")
print(f"B: {b}")
print(f"sigma_x: {np.sqrt(np.mean(x * x) - np.mean(x) * np.mean(x))}")
print(f"sigma_y: {np.sqrt(np.mean(y * y) - np.mean(y) * np.mean(y))}")

print()
print(f"Correlation: {r_xy}")
print(f"Determination: {R}")
print(f"Approximation error: {A_mean}")
print()