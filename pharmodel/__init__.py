"""pkmodel is a Pharmokinetic modelling library.

It contains functionality for creating, solving, and visualising the solution
of Parmokinetic (PK) models

"""
# Import version info
from .version_info import VERSION_INT, VERSION  # noqa

# Import main classes
from .protocol import Protocol    # noqa
from .solution import Solution     # noqa
from .visualisation import Visualisation     # noqa
from .model import Model    # noqa
