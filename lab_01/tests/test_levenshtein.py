from lib import levenshtein_recurs, levenshtein_recurs_mem


def test_empty_strings() -> None:
    str1, str2 = '', ''
    correct_answer = 0

    assert correct_answer == levenshtein_recurs(str1, str2)[0]
    assert correct_answer == levenshtein_recurs_mem(str1, str2)[0]


def test_with_one_empty() -> None:
    str1, str2 = '', 'Бауманка'
    correct_answer = len(str2)

    assert correct_answer == levenshtein_recurs(str1, str2)[0]
    assert correct_answer == levenshtein_recurs_mem(str1, str2)[0]

    assert correct_answer == levenshtein_recurs(str2, str1)[0]
    assert correct_answer == levenshtein_recurs_mem(str2, str1)[0]


def test_equal_strings() -> None:
    str1, str2 = 'Бауманка', 'Бауманка'
    correct_answer = 0

    assert correct_answer == levenshtein_recurs(str1, str2)[0]
    assert correct_answer == levenshtein_recurs_mem(str1, str2)[0]


def test_equal_length() -> None:
    str1, str2 = 'Бауманка', 'Бвуманкк'
    correct_answer = 2

    assert correct_answer == levenshtein_recurs(str1, str2)[0]
    assert correct_answer == levenshtein_recurs_mem(str1, str2)[0]


def test_equal_length_with_transpose() -> None:
    str1, str2 = 'Бауманка', 'Бауманак'
    correct_answer = 2

    assert correct_answer == levenshtein_recurs(str1, str2)[0]
    assert correct_answer == levenshtein_recurs_mem(str1, str2)[0]


def test_different_strings() -> None:
    str1, str2 = 'Бауманка', 'Бомонка'
    correct_answer = 3

    assert correct_answer == levenshtein_recurs(str1, str2)[0]
    assert correct_answer == levenshtein_recurs_mem(str1, str2)[0]


def test_full_rewrite() -> None:
    str1, str2 = 'МГТУ', 'армии'
    correct_answer = 5

    assert correct_answer == levenshtein_recurs(str1, str2)[0]
    assert correct_answer == levenshtein_recurs_mem(str1, str2)[0]


def test_several_transposes() -> None:
    str1, str2 = 'Александр', 'Аелксанрд'
    correct_answer = 4

    assert correct_answer == levenshtein_recurs(str1, str2)[0]
    assert correct_answer == levenshtein_recurs_mem(str1, str2)[0]


def test_delete() -> None:
    str1, str2 = 'МГТУ', 'МГТ'
    correct_answer = 1

    assert correct_answer == levenshtein_recurs(str1, str2)[0]
    assert correct_answer == levenshtein_recurs_mem(str1, str2)[0]


def test_add() -> None:
    str1, str2 = 'МГТ', 'МГТУ'
    correct_answer = 1

    assert correct_answer == levenshtein_recurs(str1, str2)[0]
    assert correct_answer == levenshtein_recurs_mem(str1, str2)[0]


def test_replace() -> None:
    str1, str2 = 'МГТ', 'МГТУ'
    correct_answer = 1

    assert correct_answer == levenshtein_recurs(str1, str2)[0]
    assert correct_answer == levenshtein_recurs_mem(str1, str2)[0]


def test_eng() -> None:
    str1, str2 = 'Hello', 'Hi'
    correct_answer = 4

    assert correct_answer == levenshtein_recurs(str1, str2)[0]
    assert correct_answer == levenshtein_recurs_mem(str1, str2)[0]
