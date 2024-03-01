import os, sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(SCRIPT_DIR, '../src'))

import unittest

class GeneralTests(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
