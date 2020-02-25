#######################################################################
# Copyright (C)                                                       #
# 2020 Hongjia Liu(piperliu@qq.com)                                   #
# Permission given to modify the code as long as you keep this        #
# declaration at the top                                              #
#######################################################################

"""
S -> E -> I -> R
beta, 1-14, mu
"""
import numpy as np

class Paras(object):
    def __init__(self):
        super().__init__()
        # infection rate when actioning with latent family
        self.BETA = 0.9
        # how family are willing to act with another
        self.THETA = 0.1
        # therapy
        self.MU = 0.1
        # R to S
        self.ETA = 0.01

paras = Paras()


class Calculator(object):
    def __init__(self, fam_list):
        super().__init__()
        self.fam_list = fam_list

    def next_iter(self, iterations=5):
        # [[], [], []]
        total_states = []
        for it in range(iterations):
            # firstly, next_iter's state stores in a new list()
            # when f ends itering, new_state.append(f's new state)
            # when this iteration ends, for f.state = new_state[i]
            new_state = list()
            # action and infect
            for i, f_1 in enumerate(self.fam_list):
                # print("Calculting..." + str(it) + "/" + str(iterations) + ":", end=" ")
                # print(str(i) + "/" + str(len(self.fam_list)), end="\r")
                state = f_1.state
                for f_2 in f_1.relations:
                    # S to E
                    if not f_1.seal and f_1.state == 0 and f_2.state > 0 and not f_2.seal:
                        # beta * theta
                        if np.random.binomial(1, paras.BETA) * np.random.binomial(1, paras.THETA):
                            state = f_1.infect()
                            break
                        else:
                            state = 0
                # E to I
                if f_1.state > 0:
                    state = f_1.state + 1
                    if state == 15:
                        state = -1
                # I to R
                if f_1.state == -1:
                    # mu
                    if np.random.binomial(1, paras.MU):
                        state = -2
                    else:
                        state = f_1.state
                # R to S
                if f_1.state == -2:
                    # eta
                    if np.random.binomial(1, paras.ETA):
                        state = 0
                    else:
                        state = f_1.state
                new_state.append(state)
            
            for i, f in enumerate(self.fam_list):
                f.state = new_state[i]
            
            total_states.append(new_state)
        # print("Calculting..." + str(iterations) + "/" + str(iterations) + ":", end=" ")
        # print(str(len((self.fam_list))) + "/" + str(len(self.fam_list)))
        return total_states
    
    def cls(self):
        for f in self.fam_list:
            f.state = 0
            f.seal = False
