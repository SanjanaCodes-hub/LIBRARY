
# Library Fine Calculator
# DevOps Self-Study Project - Phase 1

from datetime import datetime


def days_late(due_date, return_date):
    """Calculate the number of days a book is returned late."""
    due = datetime.strptime(due_date, "%Y-%m-%d")
    returned = datetime.strptime(return_date, "%Y-%m-%d")

    return max(0, (returned - due).days)


def fine(days):
    """Calculate library fine based on overdue days."""
    if days <= 0:
        return 0

    if days <= 5:
        return days * 2
    elif days <= 10:
        return days * 5
    else:
        return days * 10


def is_overdue(due_date, return_date):
    """Check whether a book is overdue."""
    return days_late(due_date, return_date) > 0


def calculate_total_fine(days):
    """Calculate total fine with a maximum fine limit."""
    return min(fine(days), 500)


def display_result(due_date, return_date):
    """Display the library fine calculation."""
    days = days_late(due_date, return_date)
    amount = calculate_total_fine(days)

    print("\n========== LIBRARY FINE REPORT ==========")
    print("Due Date       :", due_date)
    print("Return Date    :", return_date)
    print("Days Overdue   :", days)
    print("Overdue Status :", "Yes" if is_overdue(
        due_date, return_date) else "No")
    print("Fine Amount    : Rs.", amount)
    print("=========================================")


def main():
    print("\n===================================")
    print("       LIBRARY FINE CALCULATOR")
    print("===================================")

    print("Enter dates in YYYY-MM-DD format.")

    try:
        due_date = input("Enter book due date: ")
        return_date = input("Enter book return date: ")

        # Validate dates
        datetime.strptime(due_date, "%Y-%m-%d")
        datetime.strptime(return_date, "%Y-%m-%d")

        if datetime.strptime(return_date, "%Y-%m-%d") < datetime.strptime(
                due_date, "%Y-%m-%d"):
            print("Return date cannot be before due date.")
            return

        display_result(due_date, return_date)

    except ValueError:
        print("Invalid date! Please use YYYY-MM-DD format.")


if __name__ == "__main__":
    main()
