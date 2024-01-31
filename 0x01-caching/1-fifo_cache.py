#!/usr/bin/env python3
"""class FIFOCache that inherits from BaseCaching"""
from base_cache import BaseCaching


class FIFOCache(BaseCaching):
    """fifi cache"""

    def put(self, key, item):
        """Add an item in the cache"""
        if key and item:
            self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first = self.cache_data.keys()[0]
            self.cache_data.pop(first)
            print("DISCARD: {}".format(first))

    def get(self, key):
        """Get an item by key"""
        return self.cache_data[key] if key in self.cache_data else None
