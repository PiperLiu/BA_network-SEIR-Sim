# #######################################################################
# # Copyright (C)                                                       #
# # 2020 Hongjia Liu(piperliu@qq.com)                                   #
# # Permission given to modify the code as long as you keep this        #
# # declaration at the top                                              #
# #######################################################################

import networkx as nx
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

from tqdm import trange
import numpy as np

# from __future__ import absolute_import
import os
import sys
this_dir = os.getcwd()
# this_dir = osp.dirname(__file__)
print(this_dir)
path = os.path.join(this_dir)
sys.path.append(path)

from family import *
# using ba network
def return_family_list(n=1000, m=5, seed=0):
    # generate fam_list
    G = nx.random_graphs.barabasi_albert_graph(n, m, seed)
    fam_list = list()
    adj = list(G.edges())
    for g in G:
        fam = family(label=g)
        fam_list.append(fam)
    for g_1, g_2 in adj:
        f_1 = fam_list[g_1]
        f_2 = fam_list[g_2]
        f_1.relate(f_2)
    return fam_list, G

from calculator import *
# @return:  illed people [runs:[theta:[day:[state]]]]
# /= runs for average
def experiment_1_THETA(fam_list, THETAs, INFECT_INIT=30, days=10, runs=30):
    cal = Calculator(fam_list)
    states_each_experiment = list()
    
    states_each_experiment = np.zeros((runs, THETAs.shape[0], days, len(fam_list)))
    for r in range(runs):
        for t in trange(len(THETAs)):
            theta = THETAs[t]
            # print("theta: " + str(theta))
            paras.THETA = theta
            cal.cls()
            infects = []
            while len(infects) < INFECT_INIT:
                i = np.random.randint(0, len(fam_list))
                infects.append(i)
            for i in infects:
                fam_list[i].state = 5
            # cal.next_iter(days) returns [day:[state, state, state]]
            each_experiment = np.array(cal.next_iter(days))
            # each_experiment = [sum(data!=0) for data in each_experiment]
            states_each_experiment[r, t] = states_each_experiment[r, t] + each_experiment
    return states_each_experiment

fam_list, G = return_family_list()

"""
Ex 1
"""
# experiment 1.0
days = 50
THETAs = np.asarray([0.0001, 0.0005, 0.001, 0.005, 0.01, 0.02, 0.03, 0.05, 0.1, 0.5])
ex_0_data = experiment_1_THETA(fam_list, days=days, THETAs=THETAs)

# experiment 1.0
# data
run_theta_day_state = np.where(ex_0_data==0, 0, 1)

# show results
theta_day = run_theta_day_state.mean(axis=0).mean(axis=2)

# fig, axes = plt.subplots(figsize=(13, 5))
# for t, theta in enumerate(THETAs):
#     plt.plot(np.arange(0, days+1), [30/1000] + list(theta_day[t, :]), '*-')
# plt.xlabel('days')
# plt.ylabel('percentage of infected people')
# plt.legend([r'$\theta=$' + str(theta) for theta in THETAs])
# plt.show()

# # show nx draw
# # plot nodes on plt based on networkx
# DAY = 10

# fig, axes = plt.subplots(2, 5, figsize=(15, 5))
# for i, t in enumerate(THETAs):
#     states = run_theta_day_state[:, i, DAY-1, :].mean(axis=0)
#     plt.subplot(2, 5, i+1)
#     nx.draw(G, node_size=5, node_color=states, width=0.3, pos=nx.spring_layout(G, random_state=1), cmap=plt.cm.OrRd)
# plt.show()

# make gif
# make day 0
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
print("making pngs.." + str(0) + " for gif")
THETAs = [0.0001, 0.0005, 0.001, 0.005, 0.01, 0.02, 0.03, 0.05, 0.1, 0.5]
fig, axes = plt.subplots(3, 3, figsize=(4, 5))
G = nx.random_graphs.barabasi_albert_graph(1000, 5, 0)
for i in range(9):
    plt.subplot(3, 3, i+1)
    states = np.asarray([0]*1000)
    nx.draw(G, node_size=5, node_color=states, width=0.3, pos=nx.spring_layout(G, random_state=1), cmap=plt.cm.OrRd)
    plt.title(r'$\theta=$' + str(THETAs[i+1]), fontsize=10)
fig.suptitle('day ' + str(0), fontsize=14, fontweight='bold')
plt.savefig('utils\\images_for_gif\\' + str(0) + '_exp_1.png')

# pngs
for day in range(30):
    print("making pngs.." + str(day+1) + " for gif")
    fig, axes = plt.subplots(3, 3, figsize=(4, 5))
    for i, t in enumerate(THETAs[1:]):
        plt.subplot(3, 3, i+1)
        states = run_theta_day_state[:, i, day, :].mean(axis=0)
        nx.draw(G, node_size=5, node_color=states, width=0.3, pos=nx.spring_layout(G, random_state=1), cmap=plt.cm.OrRd, alpha=0.5)
        plt.title(r'$\theta=$' + str(t), fontsize=10)
    fig.suptitle('day ' + str(day+1), fontsize=14, fontweight='bold')
    plt.savefig('utils\\images_for_gif\\' + str(day+1) + '_exp_1.png')
