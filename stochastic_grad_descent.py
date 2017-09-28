from bokeh.plotting import figure, output_file, show
from random import shuffle

def descent(b0, b1, etha, x, y, count):
    n = len(x)
    for i in range(1, count):
        temp_x = 0
        temp_y = 0
        j = i % n
        temp_x = 2 * (b0 + b1 * x[j] - y[j])
        temp_y = 2 * (b0 + b1 * x[j] - y[j]) * x[j]
        b0 = b0 - etha * temp_x
        b1 = b1 - etha * temp_y
    return {'a': b1, 'b': b0}

def getY(x, b0, b1):
    return b0 + b1 * x

def mixArrays(x, y):
    temp = [i for i in range(0, len(x) - 1)]
    shuffle(temp)
    temp_x = []
    temp_y = []
    for j in temp:
        temp_x.append(x[j])
        temp_y.append(y[j])
    x = temp_x
    y = temp_y

x=[10.0, 8.0, 13.0, 9.0, 11.0, 14.0, 6.0, 4.0, 12.0, 7.0, 5.0]
y=[8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68]

output_file("linreg.html")
p = figure(plot_width=400, plot_height=400)

b0 = 4
b1 = 4
etha = 0.00001
count = 100000

mixArrays(x, y)

b01 = descent(b0, b1, etha, x, y, count)

sorted_x = sorted(x)

#print(x)
#print(y)
#print(sorted_x)
#print("x[0] = " + str(x[0]))
#print("x[10] = " + str(x[10]))
#print("y[0] = " + str(y[0]))
#print("y[10] = " + str(y[10]))
#print("sorted_x[0] = " + str(sorted_x[0]))
#print("sorted_x[10] = " + str(sorted_x[10]))
#print("y0 = " + str(getY(sorted_x[0], b01['b'], b01['a'])))
#print("y10 = " + str(getY(sorted_x[10], b01['b'], b01['a'])))

print(b01['a'])
print(b01['b'])

p.line([sorted_x[0], sorted_x[10]],
       [getY(sorted_x[0], b01['b'], b01['a']), getY(sorted_x[10], b01['b'], b01['a'])],
       line_width=2)
p.circle(x, y, fill_color="blue", size=5)
show(p)
