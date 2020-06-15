import numpy as np
from scipy.optimize import curve_fit, least_squares
import csv
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


def mse(y, y_pred):
    mse = np.mean((y - y_pred) ** 2)
    return mse


def func(X, a, b, c):
    x,y = X
    return a + b*np.log(x) + c*np.log(y)


def func_with_args(a, b, c):
    def func(X):
        x, y = X
        return a + b * np.log(x) + c * np.log(y)

    return func

# some artificially noisy data to fit
# x = np.linspace(0.1,1.1,101)
# y = np.linspace(1.,2., 101)
# a, b, c = 10., 4., 6.
# z = func((x,y), a, b, c) * 1 + np.random.random(101) / 100


num_of_robots_full, num_of_robots_spiral, num_of_robots_straight, num_of_robots_zigzag = [], [], [], []
area_full, area_spiral, area_straight, area_zigzag = [], [], [], []
escaping_locust_full, escaping_locust_spiral, escaping_locust_straight, escaping_locust_zigzag = [], [], [], []

num_of_robots = []
polygon_parameter = []

current_number_of_robots = 0
with open('try2.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row["Row Labels"] == "10" or row["Row Labels"] == "20" or row["Row Labels"] == "30" or row["Row Labels"] == "40" or row["Row Labels"] == "50":
            current_number_of_robots = int(row["Row Labels"])
            # num_of_robots.extend([row["Row Labels"], row["Row Labels"], row["Row Labels"], row["Row Labels"], row["Row Labels"]])
            # num_of_robots_full.append(row[" Number of robots"])
            # area_full.append(row[" Polygon Area"])
            # escaping_locust_full.append(row[" Run away locusts"])
        else:
            num_of_robots.append(current_number_of_robots)
            polygon_parameter.append(float(row["Row Labels"]))
            escaping_locust_full.append(float(row["FullRound"]))
            escaping_locust_spiral.append(float(row["Spiral"]))
            escaping_locust_straight.append(float(row["Straight"]))
            escaping_locust_zigzag.append(float(row["ZigZag"]))

        # if row[" Algorithm"] == "Straight":
        #     num_of_robots_straight.append(row[" Number of robots"])
        #     area_straight.append(row[" Polygon Area"])
        #     escaping_locust_straight.append(row[" Run away locusts"])
        # if row[" Algorithm"] == "ZigZag":
        #     num_of_robots_zigzag.append(row[" Number of robots"])
        #     area_zigzag.append(row[" Polygon Area"])
        #     escaping_locust_zigzag.append(row[" Run away locusts"])
        # if row[" Algorithm"] == "Spiral":
        #     num_of_robots_spiral.append(row[" Number of robots"])
        #     area_spiral.append(row[" Polygon Area"])
        #     escaping_locust_spiral.append(row[" Run away locusts"])

# print(num_of_robots)
# print(area)
# print(escaping_locust_full)

# x = [10, 20, 30, 40, 50]
# y = [1896, 1896, 1896, 1896, 1896]
#
# z = [24.2625, 9.35, 3.8125, 1.575, 0.65]


# num_of_robots = [10, 10, 10, 10, 10, 20, 20, 20, 20, 20, 30, 30, 30, 30, 30, 40, 40, 40, 40, 40, 50, 50, 50, 50, 50]
# area = [878, 988, 1311.5, 1896, 2261.5, 878, 988, 1311.5, 1896, 2261.5, 878, 988, 1311.5, 1896, 2261.5, 878, 988, 1311.5, 1896, 2261.5, 878, 988, 1311.5, 1896, 2261.5]


# initial guesses for a,b,c:
p0 = 1., 1., 1.
print("FullRound")
print(curve_fit(func, (num_of_robots, polygon_parameter), escaping_locust_full, p0))
# area - (array([ 52.21743823, -14.94567112,   0.57499854])
# circumference - (array([ 63.36854217, -14.94567112,  -1.38128941])
# area loss: 5.314950350465948
# circumference loss: 5.33708043925289

area_prediction_function = func_with_args(52.21743823, -14.94567112,   0.57499854)
predictions = area_prediction_function((num_of_robots, polygon_parameter))
print("area loss:", mse(np.asarray(escaping_locust_full), predictions))


print("Straight")
print(curve_fit(func, (num_of_robots, polygon_parameter), escaping_locust_straight, p0))
# area - (array([ 51.7702535 , -39.83320095,  15.35789421])
# circumference - (array([-45.49306969, -39.83320093,  41.10552816])
# area loss: 7.3479264681523
# circumference loss: 19.39142107349724

area_prediction_function = func_with_args(51.7702535, -39.83320095,  15.35789421)
predictions = area_prediction_function((num_of_robots, polygon_parameter))
print("area loss:", mse(np.asarray(escaping_locust_straight), predictions))


print("ZigZag")
print(curve_fit(func, (num_of_robots, polygon_parameter), escaping_locust_zigzag, p0))
# area - (array([ 50.42416215, -21.12972722,   5.09328686])
# circumference - (array([ 21.45148578, -21.1297272 ,  12.98397435]
# area loss: 8.060771428170046
# circumference loss: 9.581999045621258

area_prediction_function = func_with_args(50.42416215, -21.12972722,   5.09328686)
predictions = area_prediction_function((num_of_robots, polygon_parameter))
print("area loss:", mse(np.asarray(escaping_locust_zigzag), predictions))


print("Spiral")
print(curve_fit(func, (num_of_robots, polygon_parameter), escaping_locust_spiral, p0))
# area - (array([ 67.11021586, -24.22799225,   4.31389882]
# circumference - (array([ 78.49708501, -24.22799228,   3.9048133 ])
# area loss: 6.711611897140354
# circumference loss: 9.007323535518262

area_prediction_function = func_with_args(67.11021586, -24.22799225,   4.31389882)
predictions = area_prediction_function((num_of_robots, polygon_parameter))
print("area loss:", mse(np.asarray(escaping_locust_spiral), predictions))


# *********************** Plot Area ***********************

robots = np.arange(1, 100, 1)
areas = [878, 988, 1311, 1896, 2261]

B, D = np.meshgrid(robots, areas)
nu = 52.21743823 - 14.94567112*np.log(B) + 0.57499854*np.log(D)

# fig = plt.figure()
# ax = Axes3D(fig)
# ax.plot_surface(B, D, nu)
# plt.xlabel('Number of robots')
# plt.ylabel('Polygon area')
# plt.show()