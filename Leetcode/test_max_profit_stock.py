import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from max_profit_stock import soloution


class MaxprofitTestcase(unittest.TestCase):
    def test_max_profit(self):
        self.assertEqual(soloution().maxProfit([7, 1, 5, 3, 6, 4]), 5)

    def test_no_profit(self):
        self.assertEqual(soloution().maxProfit([7, 6, 4, 3, 1]), 0)




if __name__ == '__main__':

    unittest.main()

        