import pandas as pd
#
# Protocol class
#

class Protocol:
    """A Pharmokinetic (PK) protocol

    Parameters
    ----------

    filename: the name of the csv file containing the dosage records

    """
    def __init__(self, filename):
        self.filename = filename

    def read_dosage(self,):
        return pd.read_csv(self.filename)

