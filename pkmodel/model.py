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
