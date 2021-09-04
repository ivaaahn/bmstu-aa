from typing import Callable, Optional

LevenshteinFunc = Callable[[str, str], int]

CacheMatrix = list[list[Optional[int]]]
