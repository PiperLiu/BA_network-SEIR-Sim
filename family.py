#######################################################################
# Copyright (C)                                                       #
# 2020 Hongjia Liu(piperliu@qq.com)                                   #
# Permission given to modify the code as long as you keep this        #
# declaration at the top                                              #
#######################################################################

import matplotlib.pyplot as plt
from tqdm import trange
import numpy as np

class family(object):
    def __init__(self, x=0, y=0, state=0, label=0):
        super().__init__()
        self.x = x
        self.y = y
        self.state = state
        self.relations = set()
        self.label = label
        self.seal = False

    def relate(self, fam):
        """
        relate 2 families
        """
        self.relations.add(fam)
        fam.relations.add(self)
    
    def unrelate(self, fam):
        self.relations.discard(fam)
        fam.relations.discard(self)

    def isRelate(self, fam):
        if fam in self.relations:
            return True
        return False

    def infect(self):
        while True:
            latent = round(np.random.normal(7, 7))
            # latent ++ each day, if latent == 15, ill, state = -1
            if 1<= latent <= 14:
                return latent
