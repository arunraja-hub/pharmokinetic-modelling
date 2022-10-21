import pandas as pd
#
# Protocol class
#

class Protocol:
    """A Pharmokinetic (PK) protocol

    Parameters
    ----------

    value: numeric, optional
        an example paramter

    """
    def __init__(self, filename):
        self.filename = filename

    def read_dosage(self,):
        df = pd.read_csv(self.filename)
        # check heading names are correct
        if not all(item == True for item in df.columns == ['tstart','tend','doses','inst']):
            raise ValueError('Dataframe headings not match')
        
        # check if all instances are numeric
        if np.all(len(df.select_dtypes(include=["float", 'int']).columns) != len(df.columns)):
            raise ValueError('All input should be numeric')
        
        # check if all instances are non-negative
        if min(df.to_numpy().flatten()) < 0:
            raise ValueError('All input should be non-negative') 

        # inst column could only be 0 or 1
        if df['inst'].dtypes != int or (min(set(df['inst']))) < 0 or (max(set(df['inst']))) > 1:
            raise ValueError('Inst column could only contains 0 or 1')
        
        return df
