from levenshtein import levenshtein_recursive, levenshtein_recursive_memo


def test_empty_strings() -> None:
    str1, str2 = '', ''
    correct_answer = 0

    assert correct_answer == levenshtein_recursive(str1, str2)
    assert correct_answer == levenshtein_recursive_memo(str1, str2)


def test_with_one_empty() -> None:
    str1, str2 = '', 'Бауманка'
    correct_answer = len(str2)

    assert correct_answer == levenshtein_recursive(str1, str2)
    assert correct_answer == levenshtein_recursive_memo(str1, str2)

    assert correct_answer == levenshtein_recursive(str2, str1)
    assert correct_answer == levenshtein_recursive_memo(str2, str1)


def test_equal_strings() -> None:
    str1, str2 = 'Бауманка', 'Бауманка'
    correct_answer = 0

    assert correct_answer == levenshtein_recursive(str1, str2)
    assert correct_answer == levenshtein_recursive_memo(str1, str2)


def test_equal_length() -> None:
    str1, str2 = 'Бауманка', 'Бауманкк'
    correct_answer = 1

    assert correct_answer == levenshtein_recursive(str1, str2)
    assert correct_answer == levenshtein_recursive_memo(str1, str2)


def test_equal_length_with_transpose() -> None:
    str1, str2 = 'Бауманка', 'Бауманак'
    correct_answer = 2

    assert correct_answer == levenshtein_recursive(str1, str2)
    assert correct_answer == levenshtein_recursive_memo(str1, str2)


def test_different_strings() -> None:
    str1, str2 = 'Бауманка', 'Бомонка'
    correct_answer = 3

    assert correct_answer == levenshtein_recursive(str1, str2)
    assert correct_answer == levenshtein_recursive_memo(str1, str2)


def test_very_different_strings() -> None:
    str1, str2 = 'Я студент МГТУ', 'Я в армии'
    correct_answer = 12

    assert correct_answer == levenshtein_recursive(str1, str2)
    assert correct_answer == levenshtein_recursive_memo(str1, str2)
