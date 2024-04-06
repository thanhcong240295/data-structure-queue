import sys
sys.path.append('../')

import unittest
from  queue_exp import init

class TestEmptyQueue(unittest.TestCase):
  def test_empty_list_empty(self):
    queue = init(0)
    self.assertEqual(queue.is_empty(), True)

  def test_pop(self):
    queue = init(10)
    self.assertEqual(queue.is_empty(), False)

if __name__ == '__main__':
    unittest.main()
