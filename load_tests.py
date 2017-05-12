


import sys
import unittest2 as unittest

suite = unittest.defaultTestLoader.discover('test')
results = unittest.TextTestRunner(verbosity=2).run(suite)
if results.wasSuccessful():
    sys.exit(0)
else:
    sys.exit(1)
