#!/usr/bin/env python3
"""a simple pagiation"""
import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """pagination data"""
        start, end = self.index_range(page, page_size)
        dataset = self.dataset()
        data = []
        for i in range(start, end):
            if i >= len(dataset):
                break
            data.append(dataset[i])
        return data

    def index_range(self, page: int, page_size: int) -> tuple:
        """return in a list for
        those particular pagination parameters."""
        if (
            not isinstance(page, int)
            or not isinstance(page_size, int)
            or page < 0
            or page_size < 0
            or page == page_size == 0
        ):
            raise AssertionError
        return (page_size * (page - 1), page_size * page)

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """get_hyper"""
        start, end = self.index_range(page, page_size)
        dataset = self.dataset()
        data = self.get_page(page, page_size)
        self.size = len(self.dataset())
        ans = {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": page + 1
            if page < self.size and len(data) == page_size
            else None,
            "prev_page": page - 1 if page > 0 else None,
            "total_pages": math.ceil(self.size / page_size),
        }
        return ans


if __name__ == "__main__":
    server = Server()
    print(server.get_hyper(1, 2))
    print("---")
    print(server.get_hyper(2, 2))
    print("---")
    print(server.get_hyper(100, 3))
    print("---")
    print(server.get_hyper(3000, 100))
