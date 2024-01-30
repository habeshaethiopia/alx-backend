#!/usr/bin/env python3
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
            type(page) != int
            or type(page_size) != int
            or page < 0
            or page_size < 0
            or page == page_size == 0
        ):
            raise AssertionError
        return (page_size * (page - 1), page_size * page)


if __name__ == "__main__":
    server = Server()

    try:
        should_err = server.get_page(-10, 2)
    except AssertionError:
        print("AssertionError raised with negative values")

    try:
        should_err = server.get_page(0, 0)
    except AssertionError:
        print("AssertionError raised with 0")

    try:
        should_err = server.get_page(2, "Bob")
    except AssertionError:
        print("AssertionError raised when page and/or page_size are not ints")

    print(server.get_page(1, 3))
    print(server.get_page(3, 2))
    print(server.get_page(3000, 100))
