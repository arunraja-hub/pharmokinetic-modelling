#
# Model class
#

class Model:
    """A Pharmokinetic (PK) model
    This class acts as a medium to accept the user inputs for the pharmokinetic model

    Parameters
    ----------

    absorb: numeric, binary value where 1 means there is an absoption compartment and 0 vice versa
    comp: numeric, number of peripheral compartments
    V_c:  
    CL: 
    Q_p1:
    V_p1:
    Q_p2:
    V_p2:
    k_a:
        """
    
   

    def __init__(self, absorb, comp, V_c, CL, Q_p1 = 0, V_p1 = 0.1, Q_p2 = 0, V_p2 = 0.1, k_a = 0):
        self.absorb = absorb
        self.comp = comp
        self.V_c = V_c
        self.CL = CL
        self.Q_p1 = Q_p1
        self.V_p1 = V_p1
        self.Q_p2 = Q_p2
        self.V_p2 = V_p2
        self.k_a = k_a
