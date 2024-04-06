import sys
sys.path.append('../')

import unittest
from queue_exp import init

class TestPushQueue(unittest.TestCase):
  def test_push_list_empty(self):
    queue = init(0)
    queue.push(11)
    self.assertEqual(queue.get_len(), 1)

  def test_push(self):
    queue = init(10)
    queue.push(11)
    self.assertEqual(queue.get_len(), 11)

if __name__ == '__main__':
    unittest.main()
