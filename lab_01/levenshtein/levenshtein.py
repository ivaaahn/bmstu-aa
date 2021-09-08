from .types import CacheMatrix


def levenshtein_recursive(word_1: str, word_2: str) -> int:
    if not (word_1 and word_2):
        return len(word_1) + len(word_2)

    if word_1[-1] == word_2[-1]:
        return levenshtein_recursive(word_1[:-1], word_2[:-1])

    return 1 + min(
        levenshtein_recursive(word_1[:-1], word_2),
        levenshtein_recursive(word_1, word_2[:-1]),
        levenshtein_recursive(word_1[:-1], word_2[:-1]),
    )


def levenshtein_recursive_memo(word_1: str, word_2: str) -> int:
    _CACHE: CacheMatrix = [[None for j in range(len(word_2) + 1)] for i in range(len(word_1) + 1)]

    def _inner(_word_1: str, _word_2: str) -> int:
        w1_len, w2_len = len(_word_1), len(_word_2)

        if _CACHE[w1_len][w2_len] is None:
            if not (_word_1 and _word_2):
                _CACHE[w1_len][w2_len] = w1_len + w2_len
            elif _word_1[-1] == _word_2[-1]:
                _CACHE[w1_len][w2_len] = _inner(_word_1[:-1], _word_2[:-1])
            else:
                _CACHE[w1_len][w2_len] = 1 + min(
                    _inner(_word_1[:-1], _word_2),
                    _inner(_word_1, _word_2[:-1]),
                    _inner(_word_1[:-1], _word_2[:-1]),
                )

        return _CACHE[w1_len][w2_len]

    return _inner(word_1, word_2)
