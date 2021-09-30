from .levenshtein import (
    levenshtein_recurs,
    levenshtein_recurs_mem,
)

from .damerau_levenshtein import (
    damerau_levenshtein,
    damerau_levenshtein_recurs,
)

from .types import (
    LevenshteinFunc,
    CacheMatrix,
)

func_description: dict[LevenshteinFunc, str] = {
    levenshtein_recurs: 'Левенштейна (Рекурсивный)',
    levenshtein_recurs_mem: 'Левенштейна (Рекурсивный с кэшированием)',
    damerau_levenshtein: 'Дамерау-Левенштейна (Итеративный)',
    damerau_levenshtein_recurs: 'Дамерау-Левенштейна (Рекурсивный)',
}
