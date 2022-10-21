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
        # if absorb == 0 or 1:
        #     self.absorb = absorb
        # else:
         #   raise ValueError('absorb should either take the value of 0 or 1')

        self.absorb = absorb 
        self.comp = comp
        self.V_c = V_c if (V_c > 0) else self.raiseValueErr('V_c should be greater than 0')
        self.CL = CL if (CL > 0) else self.raiseValueErr('CL should be greater than 0')
        self.Q_p1 = Q_p1 if (Q_p1 >= 0) else self.raiseValueErr('Q_p1 should be greater than or equal to 0')
        self.V_p1 = V_p1 if (V_p1 >= 0) else self.raiseValueErr('V_p1 should be greater than or equal to 0')
        self.Q_p2 = Q_p2 if (Q_p2 >= 0) else self.raiseValueErr('Q_p2 should be greater than or equal to 0')
        self.V_p2 = V_p2 if (V_p2 >= 0) else self.raiseValueErr('V_p2 should be greater than or equal to 0')
        self.k_a = k_a if (k_a >= 0) else self.raiseValueErr('k_a should be greater than or equal to 0')

    def raiseValueErr(self,stringexp):
        raise ValueError(stringexp)

