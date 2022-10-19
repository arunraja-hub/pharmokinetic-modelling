

# import libaray
import matplotlib.pylab as plt
import numpy as np

class visualisation():
    def __init__(self, model1, model2=None):
        self.model1 = model1
        self.model2 = model2
        self.models = [self.model1, self.model2]


    def plot_figure(self):
        """
        Visualisation for the Pharmokinetic (PK) model
        input: a list of model solutions
        output: figure
        """

        # line style list ('-' for central, '--' for peipheral1, ':' for peripheral2)
        linestyle_list = ['-', '--', ':']

        # legend list 
        legend_list = ['Central Compartment', 'Peripheral Compartment1', 
                        'Peripheral Compartment2']

        # only one figure
        fig = plt.figure()

        for i in range(len(self.models)):
            if self.models[i] == None:
                break
        
            # add different kind of lines according to number of systems
            for j in range(0, len(self.models[i].y)):
                plt.plot(self.models[i].t, self.models[i].y[j, :], 
                label=f'model_{i+1}-'+ f'mass in{legend_list[j]}', 
                linestyle = linestyle_list[j], 
                color = plt.rcParams["axes.prop_cycle"][i])

        plt.legend()
        plt.title('Drug Mass [ng] versus Time [h]')
        plt.ylabel('drug mass [ng]')
        plt.xlabel('time [h]')
        #plt.savefig('../Figure/Drug Mass [ng] versus Time [h].png')
        plt.show()
