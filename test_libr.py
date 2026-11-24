
from libr import (
    days_late,
    fine,
    is_overdue,
    calculate_total_fine,
    calculate_multiple_fines
)


def test_days_late():
    result = days_late("2026-11-10", "2026-11-15")
    expected = 5
    assert result == expected


def test_fine_five_days():
    result = fine(5)
    expected = 10
    assert result == expected


def test_fine_eight_days():
    result = fine(8)
    expected = 40
    assert result == expected


def test_fine_zero_days():
    result = fine(0)
    expected = 0
    assert result == expected


def test_is_overdue():
    result = is_overdue("2026-11-10", "2026-11-15")
    expected = True
    assert result == expected


def test_calculate_total_fine():
    result = calculate_total_fine(100)
    expected = 500
    assert result == expected


def test_multiple_book_fine():
    books = [
        {
            "name": "Python Basics",
            "due_date": "2026-11-10",
            "return_date": "2026-11-13"
        },
        {
            "name": "Data Structures",
            "due_date": "2026-11-10",
            "return_date": "2026-11-18"
        }
    ]

    result, total = calculate_multiple_fines(books)

    expected = 46

    assert total == expected
