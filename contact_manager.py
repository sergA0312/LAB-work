class ContactManager:
    def __init__(self):
        
        self.contacts = {}

    def _find_original_name(self, search_name):
        
        for name in self.contacts:
            if name.lower() == search_name.lower():
                return name
        return None

    def add_contact(self):
        print("\n--- Добавление нового контакта ---")
        name = input("Введите имя: ").strip()

        if not name:
            print("Ошибка: Имя не может быть пустым.")
            return

        
        existing_name = self._find_original_name(name)
        if existing_name:
            print(f"Контакт '{existing_name}' уже существует с номером {self.contacts[existing_name]}.")
            choice = input("Обновить его? (да/нет): ").lower()
            if choice != 'да': return

        phone = input("Введите номер телефона: ").strip()
        self.contacts[name] = phone
        print(f"Контакт '{name}' добавлен.")

    def show_all(self):
        print("\n--- Список контактов ---")
        if not self.contacts:
            print("Список контактов пуст.")
            return

        
        for name in sorted(self.contacts.keys()):
            print(f"{name}: {self.contacts[name]}")
        print("------------------------")

    def search_contact(self):
        print("\n--- Поиск контакта ---")
        search_name = input("Имя для поиска: ").strip()

        original_name = self._find_original_name(search_name)

        if original_name:
            print(f"Контакт '{original_name}': {self.contacts[original_name]}")
        else:
            print(f"Контакт '{search_name}' не найден")

    def edit_contact(self):
        print("\n--- Изменение контакта ---")
        search_name = input("Имя контакта для изменения: ").strip()

        original_name = self._find_original_name(search_name)

        if original_name:
            new_phone = input(f"Введите новый номер телефона для '{original_name}': ").strip()
            self.contacts[original_name] = new_phone
            print(f"Контакт '{original_name}' изменен на номер {new_phone}")
        else:
            print(f"Контакт '{search_name}' не найден")

    def delete_contact(self):
        print("\n--- Удаление контакта ---")
        search_name = input("Имя для удаления: ").strip()

        original_name = self._find_original_name(search_name)

        if original_name:
            del self.contacts[original_name]
            print(f"Контакт '{original_name}' удален")
        else:
            print(f"Контакт '{search_name}' не найден")

    def menu(self):
        while True:
            print("\nМеню управления контактами:")
            print("1. Добавить контакт")
            print("2. Просмотр всех контактов")
            print("3. Поиск контакта")
            print("4. Изменение контакта")
            print("5. Удаление контакта")
            print("6. Выход")

            choice = input("Выберите действие (1-6): ")
            if choice == '1':
                self.add_contact()
            elif choice == '2':
                self.show_all()
            elif choice == '3':
                self.search_contact()
            elif choice == '4':
                self.edit_contact()
            elif choice == '5':
                self.delete_contact()
            elif choice == '6':
                print("Программа завершена. До свидания!")
                break
            else:
                print("Ошибка: Выберите пункт от 1 до 6.")


if __name__ == "__main__":
    manager = ContactManager()
    manager.menu()
