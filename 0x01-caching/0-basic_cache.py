#!/usr/bin/env python3
"""class BasicCache that inherits from BaseCaching"""
from base_cache import BaseCaching


class BasicCache(BaseCaching):
    """basic dictionary"""

    def put(self, key, item):
        """Add an item in the cache"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """Get an item by key"""
        return self.cache_data[key] if key in self.cache_data else None
