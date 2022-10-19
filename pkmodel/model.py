#
# Model class
#

class Model:
    """A Pharmokinetic (PK) model
    This model sets up the right hand side of the system of ODEs

    Parameters
    ----------

    value: numeric, optional
        an example paramter
        """
    
   

    def __init__(self, value=42):
        self.value = value

    def dose(self, t, X):
        return X

    def rhs(self, t, y, absorb, periph, V_c, CL, X, Q_p1, V_p1, Q_p2, V_p2, k_a, q_0):
        """
        rhs calculates the right hand side of the system of ODEs for the PK model which can
        then be used with an IPV solver to give the solution

        We have 6 cases for Absorbtion compartment denoted by 'absorb' on: 1 and off:0
        and number of peripharal compartments 0,1,2 denoted by 'periph'

        We take in all the possible parameters but depending on which case we are in 
        only the relavant parameters are read in

        The output is a vector of varying length depending on the case given 
        """
        if periph == 0:
            if absorb == 0:
                q_c = y
                dqc_dt = self.dose(t, X) - q_c / V_c * CL
                return [dq0_dt]

            elif absorb == 1:
                q_c = y
                dq0_dt = self.dose(t,X) - k_a * q_0
                dqc_dt = k_a * q_0 - q_c / V_c * CL
                return [dq0_dt , dqc_dt]
        
        elif periph == 1:
            if absorb == 0:
                q_c, q_p1 = y
                transition1 = Q_p1 * (q_c / V_c - q_p1 / V_p1)
                dqc_dt = self.dose(t, X) - q_c / V_c * CL - transition1
                dqp1_dt = transition1
                return [dqc_dt, dqp1_dt, dqp2_dt]
            
            elif absorb == 1:
                q_c, q_p1 = y
                transition1 = Q_p1 * (q_c / V_c - q_p1 / V_p1)
                dq0_dt = self.dose(t,X) - k_a * q_0
                dqc_dt = k_a * q_0 - q_c / V_c * CL - transition1
                dqp1_dt = transition1
                return [dq0_dt , dqc_dt, dqp1_dt]
            

        elif periph == 2:
            if absorb == 0:
                q_c, q_p1, q_p2= y
                transition1 = Q_p1 * (q_c / V_c - q_p1 / V_p1)
                transition2 = Q_p2 * (q_c / V_c - q_p2 / V_p2)
                dqc_dt = self.dose(t, X) - q_c / V_c * CL - transition1 - transition2
                dqp1_dt = transition1
                dqp2_dt = transition2 
                return [dqc_dt, dqp1_dt, dqp2_dt]

            elif absorb == 1:
                q_c, q_p1, q_p2 = y
                transition1 = Q_p1 * (q_c / V_c - q_p1 / V_p1)
                transition2 = Q_p2 * (q_c / V_c - q_p2 / V_p2)
                dq0_dt = self.dose(t,X) - k_a * q_0
                dqc_dt = k_a * q_0 - q_c / V_c * CL - transition1 - transition2
                dqp1_dt = transition1
                dqp2_dt = transition2
                return [dq0_dt , dqc_dt, dqp1_dt, dqp2_dt]
        
    

