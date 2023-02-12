import matplotlib.pyplot as plt
import numpy as np

a, b, c, d, e = -12, -18, 5, 10, -30
limit = 10
step =0.0001
line_style = "-"
color = "b"
direct_up = True

def switch_line():
    global line_style
    if line_style == "-":
        line_style = "--"
    else:
        line_style = "-"
    return line_style

def switch_color():
    global color
    if color == 'b':
        color = 'r'
    else:
        color == 'b'
    return color 

def func(x):
    f = a * x ** 4 * np.sin(np.cos(x)) + b * x ** 3 + c * x ** 2 + d * x + e
    return f 

x = np.arange(-limit, limit, step)
x_change = [(-limit, 'limit')]
for i in range(len(x)-1):
    if (func(x[i])>0 and func(x[i+1])<0) or (func(x[i])<0 and func(x[i+1])>0):
        x_acr = np.arange(x[i], x[i+1], 0.0001)
        for j in range(len(x_acr)-1):
            if (func(x_acr[j])>0 and func(x_acr[j+1])<0) or (func(x_acr[j])<0 and func(x_acr[j+1])>0):
                x_change.append((x_acr[j],'zero'))
    if direct_up:
        if func(x[i]) > func(x[i+1]):
            direct_up = False
            x_change.append((x[i], 'dir'))
    else:
        if func(x[i]) < func(x[i+1]):
            direct_up = True
            x_change.append((x[i], 'dir'))
print(x_change)
            
plt.grid()
plt.show()