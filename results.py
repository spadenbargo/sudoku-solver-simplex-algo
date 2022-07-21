from scipy.interpolate import UnivariateSpline
import matplotlib
from matplotlib import pyplot as plt
import numpy as np
from generate_board import gen_board
from solver import sudoku_feasible

p = [0.005 *i for i in range(1, 60)]+[0.3 + 0.05*i for i in range(14)]
ev = []
num_samples = 100 # I have 16gb ram :')
#
for curr_p in p:
    curr_avg = 0
    for i in range( num_samples ):
        curr_board = gen_board( curr_p )
        curr_avg += 1 if sudoku_feasible( curr_board ) else 0
        ev.append(( curr_p , float( curr_avg ) / num_samples ))

plt.style.use('seaborn ')
plt.title(r" Sudoku feasibility of randomly filled 9$\ times$9 boards ")
x = [ g_p for g_p , E_p in ev]
y = [ E_p for g_p , E_p in ev]
plt.scatter(x, y, marker ='.', label =r"$g(p)$ samples ")
s = UnivariateSpline(x,y, s=0.05) # curve fitting
xs = np. linspace(0,1, 100 )
ys = s(xs)
plt.plot(xs , ys , 'r--', label =r"$\ mathbb {E} \;[ g(p)]$ fitted curve ")
h = plt.ylabel(r"$g(p)$")
plt.xlabel(r" $p$ ")
h.set_rotation(0)
plt.legend()
plt.show()
