

# import libaray
import matplotlib.pylab as plt
import numpy as np

class Visualisation():
    def __init__(self, model1, model2=None, absorb=[0,0]):
        self.models = [model1, model2]
        self.absorb = absorb

    def plot_figure(self):
        """
        Visualisation for the Pharmokinetic (PK) model
        input: a list of model solutions
        output: figure
        """

        # line style list ('-' for central, '--' for peipheral1, ':' for peripheral2)
        linestyle_list = ['-', '--', ':']

        # legend list 
        legend_list = ['C', 'P1', 'P2']
        # colour list
        colour_list = ['red', 'blue']

        # only one figure
        fig = plt.figure()

        # different models
        for i in range(len(self.models)):
            if self.models[i] == None:
                break
            # consider more than one dose

            for j in range(0, len(self.models[i])):
                # different linestyles according to number of systems

                #Check if absorption compartment exist, don't include in graph
                start_index = 0
                if self.absorb[i] == 1:
                    start_index =1
                for k in range(start_index, len(self.models[i][j].y)):
                    plt.plot(self.models[i][j].t, self.models[i][j].y[k, :], 
                    label=f'model_{i+1}-'+ f'mass in {legend_list[k-start_index]}' if j==0 else "", 
                    linestyle = linestyle_list[k-start_index], 
                    color = colour_list[i])

                # add vertical line for inst dose
                if j < len(self.models[i]) - 1:
                    plt.vlines(x = self.models[i][j].t[-1], 
                    ymin=self.models[i][j].y[0, -1], 
                    ymax=self.models[i][j+1].y[0, 0],
                    linestyle = linestyle_list[0], 
                    color = colour_list[i])



        plt.legend()
        plt.title('Drug Mass [ng] versus Time [h]')
        plt.ylabel('drug mass [ng]')
        plt.xlabel('time [h]')

        plt.savefig('Drug Mass [ng] versus Time [h].png')