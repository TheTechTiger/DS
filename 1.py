from collections import Counter

borrow_records = {
    'Book1': 5,
    'Book2': 0,
    'Book3': 10,
    'Book4': 2,
    'Book5': 10,
    'Book6': 0
}

# 1. Average
avg_borrowed = sum(borrow_records.values()) / len(borrow_records)

# 2. Max and Min
max_borrow = max(borrow_records.values())
min_borrow = min(borrow_records.values())
max_borrow_books = [book for book, count in borrow_records.items() if count == max_borrow]
min_borrow_books = [book for book, count in borrow_records.items() if count == min_borrow]

# 3. Zero borrow count
zero_borrow_count = sum(1 for count in borrow_records.values() if count == 0)

# 4. Mode borrow count
mode_borrow = Counter(borrow_records.values()).most_common(1)[0][0]

print(f"Average books borrowed: {avg_borrowed}")
print(f"Highest borrowed books: {max_borrow_books} with {max_borrow} borrowings")
print(f"Lowest borrowed books: {min_borrow_books} with {min_borrow} borrowings")
print(f"Members with zero borrowings: {zero_borrow_count}")
print(f"Most frequently borrowed book count (mode): {mode_borrow}")
