from .levenshtein import (
    levenshtein_recursive,
    levenshtein_recursive_memo,
)

from .damerau_levenshtein import (
    damerau_levenshtein_default,
    damerau_levenshtein_recursive_memo,
)

from .types import (
    LevenshteinFunc,
)

func_description: dict[LevenshteinFunc, str] = {
    # levenshtein_recursive: 'Левенштейна (Рекурсивный)',
    levenshtein_recursive_memo: 'Левенштейна (Рекурсивный с мемоизацией)',
    damerau_levenshtein_default: 'Дамерау-Левенштейна (Итеративный)',
    damerau_levenshtein_recursive_memo: 'Дамерау-Левенштейна (Рекурсивный с мемоизацией)',
}
