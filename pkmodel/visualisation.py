

# import libaray
import matplotlib.pylab as plt
import numpy as np

class visualisation():
    def __init__(self, model1, model2=None):
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

        # different models
        for i in range(len(self.models)):
            if self.models[i] == None:
                break
            # consider more than one dose
            for j in range(0, len(self.models[i])):
                # different linestyles according to number of systems
                for k in range(0, len(self.models[i].y)):
                    plt.plot(self.models[i][j].t, self.models[i][j].y[k, :], 
                    label=f'model_{i+1}-'+ f'mass in{legend_list[k]}', 
                    linestyle = linestyle_list[k], 
                    color = plt.rcParams["axes.prop_cycle"][i])

        plt.legend()
        plt.title('Drug Mass [ng] versus Time [h]')
        plt.ylabel('drug mass [ng]')
        plt.xlabel('time [h]')
        #plt.savefig('../Figure/Drug Mass [ng] versus Time [h].png')
        plt.show()
