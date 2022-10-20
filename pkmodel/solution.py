from ast import main
from unicodedata import name
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

    def dose(self,t):
        t = int(t)
        print('t is ', t)
        print(self.dose_dataframe)
        if self.dose_dataframe.iloc[t]['inst'] == 0:
            dose = self.dose_dataframe.iloc[t]['doses']
        else:
            dose = 0
        print('*****',dose)
        return dose

    def solve_dataframe(self, absorb, comp):
        # print('**',comp, absorb)

        if  comp == 0 and absorb == 0:
            y0 = [0]
        elif comp == 0 and absorb == 1: 
            y0 = [1,1]
        elif comp == 1 and absorb == 0:
            y0 = [0,0]
        elif comp == 1 and absorb == 1: 
            y0 = [0,0,0]
        elif comp == 2 and absorb == 0:
            y0 = [0,0,0]
        elif comp == 2 and absorb == 1: 
            y0 = [0,0,0,0]
        else :
            print("Invalid parameter values")

        sol_dataframe = []

        for i in range(self.dose_dataframe.shape[0]):
            #checks for instataneous
            if self.dose_dataframe.iloc[i][3] == 1:
                y0[0] += self.dose_dataframe.iloc[i][2]
                

            sol_row = self.solver(self.dose_dataframe.iloc[i], y0)
            # breakpoint()
            y0 = sol_row.y
            sol_dataframe.append(sol_row)
        
        return sol_dataframe

        
    
#absorb, comp, V_c, CL, Q_p1, V_p1, Q_p2, V_p2, k_a, q_0
    def solver(self, dataframe_row, y0,):
        arguments = [
            self.model_instance.absorb, self.model_instance.comp, self.model_instance.V_c, self.model_instance.CL, 
            self.model_instance.Q_p1, self.model_instance.V_p1, self.model_instance.Q_p2, self.model_instance.V_p2,
            self.model_instance.k_a
        ]
        # breakpoint()
        sol = scipy.integrate.solve_ivp(
            fun=lambda t, y: self.rhs_10(t, y, *arguments),
            t_span=[dataframe_row[1], dataframe_row[2]],
            y0 = y0, t_eval = np.linspace(dataframe_row[1], dataframe_row[2], 2)
        )
        # breakpoint()
        return sol

    # def rhs_10(self, t, y, absorb, comp, V_c, CL, Q_p1, V_p1, Q_p2, V_p2, k_a):
    #     q_c, q_p1 = y
    #     transition = Q_p1 * (q_c / V_c - q_p1 / V_p1)
    #     dqc_dt = self.dose(t) - q_c / V_c * CL - transition
    #     dqp1_dt = transition
    #     return [dqc_dt, dqp1_dt]
    
    def rhs_10(self, t, y, absorb, comp, V_c, CL, Q_p1, V_p1, Q_p2, V_p2, k_a):
        # print(t, y, V_c, CL, V_p1, Q_p1)
        # breakpoint()
        q_c, q_p1 = y
        transition1 = Q_p1 * (q_c / V_c) - (q_p1 / V_p1)
        dqc_dt = self.dose(t) - (q_c / V_c) * CL - transition1 #1 needs replacing with dose
        dqp1_dt = transition1
        return [dqc_dt, dqp1_dt]

    def rhs(self, t, y, absorb, comp, V_c, CL, Q_p1, V_p1, Q_p2, V_p2, k_a):
        """
        rhs calculates the right hand side of the system of ODEs for the PK model which can
        then be used with an IPV solver to give the solution

        We have 6 cases for Absorbtion compartment denoted by 'absorb' on: 1 and off:0
        and number of peripharal compartments 0,1,2 denoted by 'comp'

        We take in all the possible parameters but depending on which case we are in 
        only the relavant parameters are read in

        The output is a vector of varying length depending on the case given 
        """
        
    
        def rhs_00(t, y, V_c, CL):
                q_c = y
                dqc_dt = self.dose(t) - (q_c / V_c) * CL
                return [dqc_dt]

        def rhs_01(t, y, V_c, CL, k_a):
                q_0, q_c = y
                dq0_dt = self.dose(t) - k_a * q_0
                dqc_dt = k_a * q_0 - (q_c / V_c) * CL
                return [dq0_dt , dqc_dt]
            
        def rhs_10(t, y, V_c, CL, V_p1, Q_p1):
                # print(t, y, V_c, CL, V_p1, Q_p1)
                # breakpoint()
                q_c, q_p1 = y
                transition1 = Q_p1 * (q_c / V_c) - (q_p1 / V_p1)
                dqc_dt = self.dose(t) - (q_c / V_c) * CL - transition1
                dqp1_dt = transition1
                # print([dqc_dt, dqp1_dt])
                return [dqc_dt, dqp1_dt]
                
        def rhs_11(t, y, V_c, CL, V_p1, Q_p1, k_a,):
                q_0, q_c, q_p1 = y
                transition1 = Q_p1 * (q_c / V_c) - (q_p1 / V_p1)
                dq0_dt = self.dose(t) - (k_a * q_0)
                dqc_dt = (k_a * q_0) - (q_c / V_c) * CL - transition1
                dqp1_dt = transition1
                return [dq0_dt , dqc_dt, dqp1_dt]
                

        def rhs_20(t, y, V_c, CL, V_p1, Q_p1, V_p2, Q_p2):
                    q_c, q_p1, q_p2= y
                    transition1 = Q_p1 * (q_c / V_c) - (q_p1 / V_p1)
                    transition2 = Q_p2 * (q_c / V_c) - (q_p2 / V_p2)
                    dqc_dt = self.dose(t) - (q_c / V_c) * CL - transition1 - transition2
                    dqp1_dt = transition1
                    dqp2_dt = transition2 
                    return [dqc_dt, dqp1_dt, dqp2_dt]

        def rhs_21 (t, y, V_c, CL, V_p1, Q_p1, V_p2, Q_p2, k_a):
                    q_0, q_c, q_p1, q_p2 = y
                    transition1 = Q_p1 * (q_c / V_c) - (q_p1 / V_p1)
                    transition2 = Q_p2 * (q_c / V_c) - (q_p2 / V_p2)
                    dq0_dt = self.dose(t) - k_a * q_0
                    dqc_dt = k_a * q_0 - (q_c / V_c) * CL - transition1 - transition2
                    dqp1_dt = transition1
                    dqp2_dt = transition2
                    return [dq0_dt , dqc_dt, dqp1_dt, dqp2_dt]

        if  comp == 0 and absorb == 0:
            rhs_00(t, y, V_c, CL)
        elif comp == 0 and absorb == 1: 
            rhs_01(t, y, V_c, CL, k_a)
        elif comp == 1 and absorb == 0:
            rhs_10( t, y, V_c, CL, V_p1, Q_p1)
            # breakpoint()
        elif comp == 1 and absorb == 1: 
            rhs_11(t, y, V_c, CL, V_p1, Q_p1, k_a)
        elif comp == 2 and absorb == 0:
            rhs_20(t, y, V_c, CL, V_p1, Q_p1, V_p2, Q_p2)
        elif comp == 2 and absorb == 1: 
            rhs_21(t, y, V_c, CL, V_p1, Q_p1, V_p2, Q_p2, k_a)
        else :
            print("Invalid parameter values")
            

# if __name__ == __main__:
dose_rec = Protocol('test_dosis_continuous.csv')
dose_df = dose_rec.read_dosage()
print(dose_df)
model_params = Model(absorb = 0, comp = 1.0, V_c = 1.0 , CL = 1.0, Q_p1 = 0.1, V_p1 = 0.1, Q_p2 = 1.0, V_p2 = 0.1, k_a = 0)
df_to_solve = Solution(dose_df, model_params)
print(model_params.absorb,model_params.comp)
sol_dataframe = df_to_solve.solve_dataframe(model_params.absorb,model_params.comp)
print(sol_dataframe)
    
    

