# The Computer Language Benchmarks Game
# http://benchmarksgame.alioth.debian.org/
#
# originally by Kevin Carson
# modified by Tupteq, Fredrik Johansson, and Daniel Nanz
# modified by Maciej Fijalkowski
# 2to3

import itertools
import multiprocessing
import sys
import time

import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

positions = np.loadtxt('initial_positions.txt')
velocities = np.loadtxt('initial_velocities.txt')
masses = np.loadtxt('masses.txt')

dv = np.zeros_like(velocities)

def combinations(l):
    result = []
    for x in range(len(l) - 1):
        ls = l[x+1:]
        for y in ls:
            result.append((l[x],y))
    return result

def update_velocities(pair, dt):
    x1, x2 = positions[pair[0]], positions[pair[1]]
    v1, v2 = velocities[pair[0]], velocities[pair[1]]
    m1, m2 = masses[pair[0]], masses[pair[1]]
    dx = x1 - x2
    mag = dt * np.linalg.norm(dx)
    b1m = m1 * mag
    b2m = m2 * mag
    dv1 = dx * b2m
    dv2 = dx * b1m
    v1 += dv1
    v2 += dv2

def advance(dt, n, positions=positions, velocities=velocities):
    for step in range(n):
        for pair in itertools.combinations(range(N), 2):
            update_velocities(pair, dt)

        positions += dt * velocities

N = 50


ims = []

fig, ax = plt.subplots()

sc = plt.scatter([], [])

def step(i):
    positions[0, :] = 0

    t1 = time.time()
    advance(0.001, 5)
    t2 = time.time()

    x_list = positions[:, 0]
    y_list = positions[:, 1]

    sc.set_offsets(np.c_[x_list, y_list])
    plt.axis([-200, 200, -200, 200])
 
    print(t2-t1)

im_ani = animation.FuncAnimation(fig, step, 100, repeat=False)
plt.show()

print("Position of particle 5: {}".format(positions[5]))
