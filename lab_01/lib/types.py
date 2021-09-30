from typing import Callable, Optional, Union

CacheMatrix = list[list[Optional[int]]]

LevenshteinFunc = Union[
    Callable[[str, str], tuple[int, CacheMatrix]],
    Callable[[str, str, int], tuple[int, int]],
    Callable[[str, str, int], tuple[int, int, CacheMatrix]],
]
