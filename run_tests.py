import unittest

import subprocess
import time


#from tests.test1 import helloTest
#from tests.utils import *

from tests.ServerFunctional import InitialServerValuesSet

from tests.ServiceFunctional import InitialServiceValuesSet
from tests.ServiceFunctional import ServiceMonitorBindings

from tests.ServiceGroupFunctional import ServiceGroupMonitorBindings

from tests.ServiceCountAttributes import ServiceCountAttributes
from tests.LBVserverFunctional import FullInitialValues
from tests.LBVserverFunctional import MinimalInitialSetValues
from tests.LBMonitorFunctional import LBMonitorFullInitialValues
from tests.ServiceGroupFunctional import InitialServiceGroupValues
from tests.CSPolicyFunctional import CSPolicyFullInitialValues
from tests.CSActionFunctional import CSActionFullInitialValues



if __name__ == '__main__':
    unittest.main()
