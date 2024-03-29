#!/usr/bin/env python3
"""function named index_range that takes two
integer arguments page and page_size"""


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
