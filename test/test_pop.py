import sys
sys.path.append('../')

import unittest
from  queue_exp import init

class TestPopQueue(unittest.TestCase):
  def test_pop_list_empty(self):
    queue = init(0)
    self.assertEqual(queue.pop(), None)

  def test_pop(self):
    queue = init(10)
    pop = queue.pop()
    self.assertEqual(pop, 1)
    self.assertEqual(queue.get_len(), 9)

if __name__ == '__main__':
    unittest.main()
