import random


class LibrarySystem:
    def __init__(self):
        self.books = {}

    def add_book(self):
        title = input("Введите название книги: ").strip()
        author = input("Введите имя автора: ").strip()
        year = input("Введите год издания: ").strip()

        book_id = str(random.randint(100000, 999999))
        self.books[book_id] = {
            "title": title,
            "author": author,
            "year": year,
            "available": True
        }

        print(f"\nКнига добавлена:")
        print(f"Идентификатор книги: {book_id}")
        print(f"Название: {title}")
        print(f"Автор: {author}")
        print(f"Год издания: {year}\n")

    def issue_book(self):
        book_id = input("Введите идентификатор книги: ").strip()
        if book_id not in self.books:
            print(f"\nОшибка: Книга с идентификатором {book_id} не найдена.\n")
            return

        if not self.books[book_id]["available"]:
            print(f"\nОшибка: Книга уже выдана.\n")
            return

        self.books[book_id]["available"] = False
        print(f"\nКнига выдана:")
        print(f"Идентификатор книги: {book_id}")
        print(f"Название: {self.books[book_id]['title']}\n")

    def return_book(self):
        book_id = input("Введите идентификатор книги: ").strip()
        if book_id not in self.books:
            print(f"\nОшибка: Книга с идентификатором {book_id} не найдена.\n")
            return

        if self.books[book_id]["available"]:
            print(
                f"\nОшибка: Книга с идентификатором {book_id} уже возвращена. Невозможно выполнить повторный возврат.\n")
            return

        self.books[book_id]["available"] = True
        print(f"\nКнига возвращена:")
        print(f"Идентификатор книги: {book_id}")
        print(f"Название: {self.books[book_id]['title']}\n")

    def check_availability(self):
        book_id = input("Введите идентификатор книги: ").strip()
        if book_id not in self.books:
            print(f"\nОшибка: Книга не найдена.\n")
            return

        book = self.books[book_id]
        status = "доступна" if book["available"] else "недоступна"
        print(f"\nКнига {status}:")
        print(f"Идентификатор книги: {book_id}")
        print(f"Название: {book['title']}\n")

    def menu(self):
        while True:
            print("Выберите действие:")
            print("1. Добавление новой книги")
            print("2. Выдача книги")
            print("3. Возврат книги")
            print("4. Проверка доступности книги")

            choice = input("Ваш выбор: ")
            if choice == '1':
                self.add_book()
            elif choice == '2':
                self.issue_book()
            elif choice == '3':
                self.return_book()
            elif choice == '4':
                self.check_availability()
            else:
                print("Ошибка выбора.")


if __name__ == "__main__":
    lib = LibrarySystem()
    lib.menu()
