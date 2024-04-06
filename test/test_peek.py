import sys
sys.path.append('../')

import unittest
from  queue_exp import init

class TestPeekQueue(unittest.TestCase):
  def test_peek_list_empty(self):
    queue = init(0)
    self.assertEqual(queue.peek(), None)

  def test_peek(self):
    queue = init(10)
    queue.push(11)
    self.assertEqual(queue.peek(), 1)

if __name__ == '__main__':
    unittest.main()
