# import the get_gematria function from main.py
from main import (
    get_gematria,
    apply_functions_on_numbers,
    multiply_by_2,
    square,
    inverse,
)


# test the get_gematria function
def test_get_gematria():
    # test the get_gematria function with the word "א"
    assert get_gematria("א") == 1
    # test the get_gematria function with the word "ב"
    assert get_gematria("ב") == 2
    # test the get_gematria function with the word "ג"
    assert get_gematria("ג") == 3
    # test the get_gematria function with the word "ד"
    assert get_gematria("ד") == 4
    # test the get_gematria function with the word "ה"
    assert get_gematria("ה") == 5
    # test the get_gematria function with the word "ו"
    assert get_gematria("ו") == 6
    # test the get_gematria function with the word "ז"
    assert get_gematria("ז") == 7
    # test the get_gematria function with the word "ח"
    assert get_gematria("ח") == 8
    # test the get_gematria function with the word "ט"
    assert get_gematria("ט") == 9
    # test the get_gematria function with the word "י"
    assert get_gematria("י") == 10
    # test the get_gematria function with the word "כ"
    assert get_gematria("כ") == 20
    # test the get_gematria function with the word "ל"
    assert get_gematria("ל") == 30
    # test the get_gematria function with the word "מ"
    assert get_gematria("מ") == 40
    # test the get_gematria function with the word "נ"
    assert get_gematria("נ") == 50
    # test the get_gematria function with the word "ס"
    assert get_gematria("ס") == 60
    # test the get_gematria function with the word "ע"
    assert get_gematria("ע") == 70
    # test the get_gematria function with the word "פ"
    assert get_gematria("פ") == 80
    # test the get_gematria function with the word "צ"
    assert get_gematria("צ") == 90
    # test the get_gematria function with the word "ק"
    assert get_gematria("ק") == 100
    # test the get_gematria function with the word "ר"
    assert get_gematria("ר") == 200
    # test the get_gematria function with the word "ש"
    assert get_gematria("ש") == 300
    # test the get_gematria function with the word "ת"
    assert get_gematria("ת") == 400
    # test the get_gematria function with the word "טז"
    assert get_gematria("טז") == 16
    # test the get_gematria function with the word "טו"
    assert get_gematria("טו") == 15


def test_apply_function_on_numbers():
    numbers = [1, 2, 3, 4, 5]
    functions = [multiply_by_2, square, inverse]
    result = apply_functions_on_numbers(numbers, functions)
    assert result == {
        "multiply_by_2": [2, 4, 6, 8, 10],
        "square": [1, 4, 9, 16, 25],
        "inverse": [1.0, 0.5, 0.3333333333333333, 0.25, 0.2],
    }


if __name__ == "__main__":
    test_get_gematria()
    print("All tests passed")
