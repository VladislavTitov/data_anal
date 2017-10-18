import numpy as np
import random
from bokeh.plotting import figure, output_file, show

def hyper(w, x, y, b):
    return y * (w.transpose().dot(x) + b)

def NablaQ(w, x, y, b, lambd):
    if hyper(w, x, y, b) < 1:
        return lambd * w - y * x
    else:
        return lambd * w

def SGD(x, y, NablaLoss, w, b, C = 2, eta=0.1, iters=20):
    lambd = 2 / (C * len(x))
    for i in range(iters):
        for xi, yi in zip(x, y):
            xi = np.array(xi)
            w = w - eta * NablaLoss(w, xi, yi, b, lambd)
            print(w)
    return w



x = [[1, 2], [2, 3], [3, 3], [2, 1], [3, 2], [4, 3]]
y = [1, 1, 1, 0, 0, 0]

C = 2
b = 0
w = np.array([1, 1])

w = SGD(x, y, NablaQ, w, b, C)
print(w.dot(np.array([1, 2])) + b)
print(w.dot(np.array([3, 2])) + b)

#X =[]
#Y = []
#for xi in x:
#    X.append(x1[0])
#    Y.append(x1[1])
    
#output_file("linreg.html")
#p = figure(plot_width=400, plot_height=400)
#p.circle(X, Y, fill_color="blue", size=5)
#p.line([1, 2], )

#show(p)