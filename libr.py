
import sys
from datetime import datetime


def days_late(due_date, return_date):
    due = datetime.strptime(due_date, "%Y-%m-%d")
    returned = datetime.strptime(return_date, "%Y-%m-%d")
    return max(0, (returned - due).days)


def fine(days):
    if days <= 0:
        return 0
    elif days <= 5:
        return days * 2
    elif days <= 10:
        return days * 5
    else:
        return days * 10


def is_overdue(due_date, return_date):
    return days_late(due_date, return_date) > 0


def calculate_total_fine(days):
    return min(fine(days), 500)


def display_result(due_date, return_date):
    days = days_late(due_date, return_date)
    amount = calculate_total_fine(days)

    print("\n========== LIBRARY FINE REPORT ==========")
    print("Due Date       :", due_date)
    print("Return Date    :", return_date)
    print("Days Overdue   :", days)
    print("Overdue Status :", "Yes" if days > 0 else "No")
    print("Fine Amount    : Rs.", amount)
    print("=========================================")


def calculate_multiple_fines(books):
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
    if len(sys.argv) > 1:
        choice = sys.argv[1]
    else:
        print("\nLIBRARY FINE CALCULATOR")
        print("1. Single Book Fine")
        print("2. Multiple Book Fine")
        print("3. Exit")
        choice = input("Enter choice: ").strip()

    try:
        if choice == "1":
            if len(sys.argv) >= 4:
                due_date = sys.argv[2]
                return_date = sys.argv[3]
            else:
                due_date = input("Enter due date (YYYY-MM-DD): ")
                return_date = input("Enter return date (YYYY-MM-DD): ")

            if datetime.strptime(return_date, "%Y-%m-%d") < datetime.strptime(due_date, "%Y-%m-%d"):
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
                print(f"\nBook {i + 1}")
                name = input("Enter book name: ").strip()
                due_date = input("Enter due date: ")
                return_date = input("Enter return date: ")

                due = datetime.strptime(due_date, "%Y-%m-%d")
                returned = datetime.strptime(return_date, "%Y-%m-%d")

                if returned < due or not name:
                    print("Invalid book details.")
                    return

                books.append({
                    "name": name,
                    "due_date": due_date,
                    "return_date": return_date
                })

            results, total = calculate_multiple_fines(books)

            print("\n========== MULTIPLE BOOK REPORT ==========")
            for book in results:
                print(book["name"], "- Days late:",
                      book["days_late"], "- Fine: Rs.", book["fine"])

            print("TOTAL FINE: Rs.", total)

        elif choice == "3":
            print("Thank you for using Library Fine Calculator!")

        else:
            print("Invalid choice!")

    except ValueError:
        print("Invalid arguments, dates or numbers.")


if __name__ == "__main__":
    main()
