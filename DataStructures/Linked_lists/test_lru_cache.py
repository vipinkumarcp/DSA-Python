import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from LRU_cache import LRUcache


class LRUCacheTests(unittest.TestCase):
    def test_capacity_is_respected(self):
        cache = LRUcache(2)
        cache.put(1, 10)
        cache.put(2, 20)
        cache.put(3, 30)

        self.assertEqual(cache.get
                         (1), -1)
        self.assertEqual(cache.get(2), 20)
        self.assertEqual(cache.get(3), 30)

    def test_existing_key_updates_value_and_keeps_recent_order(self):
        cache = LRUcache(2)
        cache.put(1, 10)
        cache.put(2, 20)
        cache.put(1, 15)
        cache.put(3, 30)

        self.assertEqual(cache.get(1), 15)
        self.assertEqual(cache.get(2), -1)
        self.assertEqual(cache.get(3), 30)


if __name__ == "__main__":
    unittest.main()
