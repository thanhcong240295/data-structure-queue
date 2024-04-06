import sys
sys.path.append('../')

import unittest
from  queue_exp import init

class TestRevertQueue(unittest.TestCase):
  def test_revert_list_empty(self):
    queue = init(0)
    self.assertEqual(queue.revert(), None)

  def test_revert_list_empty(self):
    queue = init(10)
    res = queue.revert()
    self.assertEqual(res.get_len(), 10)
    self.assertEqual(res.peek(), 10)

if __name__ == '__main__':
    unittest.main()
