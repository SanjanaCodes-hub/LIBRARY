
# Library Fine Calculator
# DevOps Self-Study Project
# Phase 4 - Multiple Book Fine Calculator

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
    elif days <= 5:
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
    """Display the fine calculation report."""
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


# NEW FEATURE - PHASE 4

def calculate_multiple_fines(books):
    """Calculate fines for multiple books."""
    results = []
    total_fine = 0

    for book in books:
        days = days_late(book["due_date"], book["return_date"])
        amount = calculate_total_fine(days)

        results.append({
            "name": book["name"],
            "days_late": days,
            "fine": amount
        })

        total_fine += amount

    return results, total_fine


def main():
    print("\n===================================")
    print("       LIBRARY FINE CALCULATOR")
    print("===================================")

    print("1. Calculate Fine for One Book")
    print("2. Calculate Fine for Multiple Books")

    choice = input("Enter your choice: ")

    try:
        if choice == "1":
            due_date = input("Enter book due date (YYYY-MM-DD): ")
            return_date = input("Enter book return date (YYYY-MM-DD): ")

            datetime.strptime(due_date, "%Y-%m-%d")
            datetime.strptime(return_date, "%Y-%m-%d")

            if return_date < due_date:
                print("Return date cannot be before due date.")
                return

            display_result(due_date, return_date)

        elif choice == "2":
            books = []
            count = int(input("Enter number of books: "))

            if count <= 0:
                print("Number of books must be positive.")
                return

            for i in range(count):
                print(f"\nEnter details for Book {i + 1}")

                name = input("Enter book name: ").strip()
                if not name:
                    print("Book name cannot be empty.")
                    return

                due_date = input("Enter due date (YYYY-MM-DD): ")
                return_date = input("Enter return date (YYYY-MM-DD): ")

                due = datetime.strptime(due_date, "%Y-%m-%d")
                returned = datetime.strptime(return_date, "%Y-%m-%d")

                if returned < due:
                    print("Return date cannot be before due date.")
                    return

                books.append({
                    "name": name,
                    "due_date": due_date,
                    "return_date": return_date
                })

            results, total = calculate_multiple_fines(books)

            print("\n========== MULTIPLE BOOK FINE REPORT ==========")

            for book in results:
                print("\nBook Name :", book["name"])
                print("Days Late :", book["days_late"])
                print("Fine      : Rs.", book["fine"])

            print("\n-----------------------------------------------")
            print("TOTAL LIBRARY FINE: Rs.", total)
            print("===============================================")

        else:
            print("Invalid choice!")

    except ValueError:
        print("Invalid input! Please enter valid dates and numbers.")


if __name__ == "__main__":
    main()
