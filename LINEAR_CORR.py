program = """Нахождение уравнения линейной корреляции"""

# Заполнить ниже

# U -> x (горизонталь)
# V -> y (вертикаль)

x = [10, 16, 22, 28, 34, 40]
y = [17, 23, 29, 35, 41, 47]

nu = [5, 26, 63, 70, 19, 17] # nx 
nv = [7, 47, 72, 49, 23, 2] # ny

u = [-3, -2, -1, 0, 1, 2] 
v = [-2, -1, -0, 1, 2, 3] 

# Середина (примечание: вместо '-' вставлять 0)
l = [
    [3, 4, 0, 0, 0, 0],
    [2, 20, 25, 0, 0, 0],
    [0, 2, 30, 40, 0, 0],
    [0, 0, 8, 15, 14, 12],
    [0, 0, 0, 15, 4, 4],
    [0, 0, 0, 0, 1, 1]
]


# Ниже не заполнять
n = sum(nu)
n_u = len(x)
n_v = len(y)

cu_i = u.index(0); hu = abs(x[0] - x[1]); 
cv_i = v.index(0); hv = abs(y[0] - y[1]); 

cu = x[cu_i]
cv = y[cv_i]


from math import sqrt as sqrt2

NuvUV = 0
for j in range(0, n_v):
    for i in range(0, n_u):
        NuvUV += l[j][i] * v[j] * u[i]

u_hat = sum([u[i]*nu[i] for i in range(n_u)]) / n
v_hat = sum([v[i]*nv[i] for i in range(n_v)]) / n
u_hat2 = sum([u[i]*u[i]*nu[i] for i in range(n_u)]) / n
v_hat2 = sum([v[i]*v[i]*nv[i] for i in range(n_v)]) / n
sig_u = sqrt2(u_hat2 - (u_hat*u_hat))
sig_v = sqrt2(v_hat2 - (v_hat*v_hat))
rb = (NuvUV - n * u_hat * v_hat) / (n * sig_u * sig_v)
x_hat = u_hat * hu + cu
y_hat = v_hat * hv + cv
sig_x = hu * sig_u
sig_y = hv * sig_v

temp = rb * (sig_y/sig_x)
temp2 = rb * (sig_x/sig_y)

print(f"n: {n}")
print(f"NuvUV: {NuvUV}")
print(f"h1: {hu}")
print(f"h2: {hv}")
print(f"c1: {cu}")
print(f"c2: {cv}")

print()

print("u_hat:", u_hat)
print("v_hat:", v_hat)
print("u_hat2:", u_hat2)
print("v_hat2:", v_hat2)
print("sig_u:", sig_u)
print("sig_v:", sig_v)
print("rb:", rb)
print("x_hat:", x_hat)
print("y_hat:", y_hat)
print("sig_x:", sig_x)
print("sig_y:", sig_y)

print()

print(f"Yx = {temp}x + {(temp * -x_hat) + y_hat }")
print(f"Xy = {temp2}y + {(temp2 * -y_hat) + x_hat}")

print(f"Программа {program} сработала успешно \n")