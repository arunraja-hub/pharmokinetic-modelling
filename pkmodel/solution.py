import matplotlib.pylab as plt
from protocol import Protocol
from model import Model
import scipy
# import model
import numpy as np
#
# Solution class
#

class Solution:
    """A Pharmokinetic (PK) model solution

    Parameters
    ----------

    value: numeric, optional
        an example paramter

    """
    def __init__(self, dose_dataframe,model_instance):
        self.dose_dataframe = dose_dataframe
        self.model_instance = model_instance

    def dose(self,t,row_index):
        t = int(t)
        if self.dose_dataframe.iloc[row_index]['tstart'] <= t <= self.dose_dataframe.iloc[row_index]['tend'] and self.dose_dataframe.iloc[row_index]['inst'] == 0 :#
            dose = self.dose_dataframe.iloc[row_index]['doses']
        else:
            dose = 0
        return dose

    def solve_dataframe(self, absorb, comp, ):

        if  comp == 0 and absorb == 0:
            y0 = [0]
        elif comp == 0 and absorb == 1: 
            y0 = [0,0]
        elif comp == 1 and absorb == 0:
            y0 = [0,0]
        elif comp == 1 and absorb == 1: 
            y0 = [0,0,0]
        elif comp == 2 and absorb == 0:
            y0 = [0,0,0]
        elif comp == 2 and absorb == 1: 
            y0 = [0,0,0,0]
        else :
            raise("Invalid parameter values")

        sol_dataframe = []

        for i in range(self.dose_dataframe.shape[0]):
            if self.dose_dataframe.iloc[i][3] == 1:
                y0[0] += self.dose_dataframe.iloc[i][2]
                

            sol_row = self.solver(self.dose_dataframe, i, y0)
            sol_y_flattened = sol_row.y.flatten()
            y0 = sol_y_flattened[len(sol_row.y[0])-1::len(sol_row.y[0])]
            sol_dataframe.append(sol_row)
        
        return sol_dataframe

        
    
    def solver(self, dose_df, row_index, y0):
        arguments = [
            self.model_instance.absorb, self.model_instance.comp, self.model_instance.V_c, self.model_instance.CL, 
            self.model_instance.Q_p1, self.model_instance.V_p1, self.model_instance.Q_p2, self.model_instance.V_p2,
            self.model_instance.k_a]

        if self.model_instance.comp == 0 and self.model_instance.absorb ==0:
            sol = scipy.integrate.solve_ivp(
            fun=lambda t, y: self.rhs_00(row_index,t, y, *arguments),
            t_span=[dose_df.iloc[row_index][0], dose_df.iloc[row_index][1]],
            y0 = y0, t_eval = np.linspace (dose_df.iloc[row_index][0], dose_df.iloc[row_index][1], 1000)
            )
        elif self.model_instance.comp == 0 and self.model_instance.absorb == 1: 
            sol = scipy.integrate.solve_ivp(
            fun=lambda t, y: self.rhs_01(row_index,t, y, *arguments),
            t_span=[dose_df.iloc[row_index][0], dose_df.iloc[row_index][1]],
            y0 = y0, t_eval = np.linspace (dose_df.iloc[row_index][0], dose_df.iloc[row_index][1], 1000)
        )
        elif self.model_instance.comp == 1 and self.model_instance.absorb == 0:
            sol = scipy.integrate.solve_ivp(
            fun=lambda t, y: self.rhs_10(row_index,t, y, *arguments),
            t_span=[dose_df.iloc[row_index][0], dose_df.iloc[row_index][1]],
            y0 = y0, t_eval = np.linspace (dose_df.iloc[row_index][0], dose_df.iloc[row_index][1], 1000)
        )
        elif self.model_instance.comp == 1 and self.model_instance.absorb == 1: 
            sol = scipy.integrate.solve_ivp(
            fun=lambda t, y: self.rhs_11(row_index,t, y, *arguments),
            t_span=[dose_df.iloc[row_index][0], dose_df.iloc[row_index][1]],
            y0 = y0, t_eval = np.linspace (dose_df.iloc[row_index][0], dose_df.iloc[row_index][1], 1000)
        )
        elif self.model_instance.comp == 2 and self.model_instance.absorb == 0:
            sol = scipy.integrate.solve_ivp(
            fun=lambda t, y: self.rhs_20(row_index,t, y, *arguments),
            t_span=[dose_df.iloc[row_index][0], dose_df.iloc[row_index][1]],
            y0 = y0, t_eval = np.linspace (dose_df.iloc[row_index][0], dose_df.iloc[row_index][1], 1000)
        )
        elif self.model_instance.comp == 2 and self.model_instance.absorb == 1: 
            sol = scipy.integrate.solve_ivp(
            fun=lambda t, y: self.rhs_21(row_index,t, y, *arguments),
            t_span=[dose_df.iloc[row_index][0], dose_df.iloc[row_index][1]],
            y0 = y0, t_eval = np.linspace (dose_df.iloc[row_index][0], dose_df.iloc[row_index][1], 1000)
        )
        else :
            print("Invalid parameter values")

        return sol


    
    def rhs_10(self, row_index, t, y, absorb, comp, V_c, CL, Q_p1, V_p1, Q_p2, V_p2, k_a):
        q_c, q_p1 = y
        transition1 = Q_p1 * (q_c / V_c) - (q_p1 / V_p1)
        dqc_dt = self.dose(t,row_index) - (q_c / V_c) * CL - transition1 #1 needs replacing with dose
        dqp1_dt = transition1
        return [dqc_dt, dqp1_dt]

    def rhs_00(self, row_index, t, y, absorb, comp, V_c, CL, Q_p1, V_p1, Q_p2, V_p2, k_a):
                q_c = y
                dqc_dt = self.dose(t,row_index) - (q_c / V_c) * CL
                return [dqc_dt]

    def rhs_01(self, row_index, t, y, absorb, comp, V_c, CL, Q_p1, V_p1, Q_p2, V_p2, k_a):
            q_0, q_c = y
            dq0_dt = self.dose(t,row_index) - k_a * q_0
            dqc_dt = k_a * q_0 - (q_c / V_c) * CL
            return [dq0_dt , dqc_dt]
        
            
    def rhs_11(self, row_index, t, y, absorb, comp, V_c, CL, Q_p1, V_p1, Q_p2, V_p2, k_a):
            q_0, q_c, q_p1 = y
            transition1 = Q_p1 * (q_c / V_c) - (q_p1 / V_p1)
            dq0_dt = self.dose(t,row_index) - (k_a * q_0)
            dqc_dt = (k_a * q_0) - (q_c / V_c) * CL - transition1
            dqp1_dt = transition1
            return [dq0_dt , dqc_dt, dqp1_dt]
            

    def rhs_20(self, row_index, t, y, absorb, comp, V_c, CL, Q_p1, V_p1, Q_p2, V_p2, k_a):
                q_c, q_p1, q_p2= y
                transition1 = Q_p1 * (q_c / V_c) - (q_p1 / V_p1)
                transition2 = Q_p2 * (q_c / V_c) - (q_p2 / V_p2)
                dqc_dt = self.dose(t,row_index) - (q_c / V_c) * CL - transition1 - transition2
                dqp1_dt = transition1
                dqp2_dt = transition2 
                return [dqc_dt, dqp1_dt, dqp2_dt]

    def rhs_21 (self,row_index, t, y, absorb, comp, V_c, CL, Q_p1, V_p1, Q_p2, V_p2, k_a):
                q_0, q_c, q_p1, q_p2 = y
                transition1 = Q_p1 * (q_c / V_c) - (q_p1 / V_p1)
                transition2 = Q_p2 * (q_c / V_c) - (q_p2 / V_p2)
                dq0_dt = self.dose(t,row_index) - k_a * q_0
                dqc_dt = k_a * q_0 - (q_c / V_c) * CL - transition1 - transition2
                dqp1_dt = transition1
                dqp2_dt = transition2
                return [dq0_dt , dqc_dt, dqp1_dt, dqp2_dt]


            

dose_rec = Protocol('test_dosis_combined.csv')
dose_df = dose_rec.read_dosage()
print(dose_df)
model_params = Model(absorb = 1, comp = 0, V_c = 1.0 , CL = .1, Q_p1 = 1.1, V_p1 = 0.1, Q_p2 = 1.0, V_p2 = 0.1, k_a = 1.0)
df_to_solve = Solution(dose_df, model_params)
print(model_params.absorb,model_params.comp)
sol_dataframe = df_to_solve.solve_dataframe(model_params.absorb,model_params.comp)
print('----',sol_dataframe)

fig = plt.figure()

print(np.array(sol_dataframe).shape)

plt.plot(sol_dataframe[0].t, sol_dataframe[0].y[0, :])
plt.plot(sol_dataframe[1].t, sol_dataframe[1].y[0, :])
plt.plot(sol_dataframe[2].t, sol_dataframe[2].y[0, :])

plt.plot(sol_dataframe[0].t, sol_dataframe[0].y[1, :])
plt.plot(sol_dataframe[1].t, sol_dataframe[1].y[1, :])
plt.plot(sol_dataframe[2].t, sol_dataframe[2].y[1, :])

# plt.plot(sol_dataframe[0].t, sol_dataframe[0].y[2, :])
# plt.plot(sol_dataframe[1].t, sol_dataframe[1].y[2, :])
# plt.plot(sol_dataframe[2].t, sol_dataframe[2].y[2, :])


# plt.plot(sol_dataframe[0].t, sol_dataframe[0].y[3, :])
# plt.plot(sol_dataframe[1].t, sol_dataframe[1].y[3, :])
# plt.plot(sol_dataframe[2].t, sol_dataframe[2].y[3, :])

plt.legend()
plt.ylabel('drug mass [ng]')
plt.xlabel('time [h]')
plt.savefig('temp.png')
    
