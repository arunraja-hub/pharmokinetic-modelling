"""
Visualisation for the Pharmokinetic (PK) model
input: a list of models
output: figure
"""


# import libaray
import matplotlib.pylab as plt
import numpy as np
import scipy.integrate

# user defined time interval
# t_eval = np.linspace(0, 1, 1000)

# initial states, number of inputs depends on number of compartments
# y0 = np.array([0.0, 0.0])

def plot_figure(t_eval, y0, models):
    # line style list ('-' for central, '--' for peipheral1, ':' for peripheral2)
    linestyle_list = ['-', '--', ':']

    # only one figure
    fig = plt.figure()
    ## need models: [model1_args, model2_args]
    for i in range(len(models)):
        temp_model = models[i]

        # take args from input
        args = [temp_model['absorb'], temp_model['periph'], temp_model['V_c'],
        temp_model['CL'], temp_model['X'], temp_model['Q_p1'], temp_model['V_p1'],
        temp_model['Q_p2'], temp_model['V_p2'], temp_model['k_a'], 
        temp_model['q_0']]

        # solve an initial value problem for a system of ODEs
        sol = scipy.integrate.solve_ivp(
            fun=lambda t, y: rhs(t, y, *args),
            t_span=[t_eval[0], t_eval[-1]],
            y0=y0, t_eval=t_eval
        )

        # add different kind of lines according to number of systems
        for j in len(sol.y):
            plt.plot(sol.t, sol.y[j, :], label=f'model_{i+1}'+ f'- q_p{j}', 
            linestyle = linestyle_list[j], 
            color = plt.rcParams["axes.prop_cycle"][i])

    plt.legend()
    plt.title('Drug Mass [ng] versus Time [h]')
    plt.ylabel('drug mass [ng]')
    plt.xlabel('time [h]')
    #plt.savefig('../Figure/Drug Mass [ng] versus Time [h].png')
    plt.show()
