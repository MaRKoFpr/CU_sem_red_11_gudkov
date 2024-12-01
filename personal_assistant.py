import csv
from datetime import datetime


class Task:
    def __init__(self, title, description, priority, due_date):
        self.title = title
        self.description = description
        self.priority = priority
        self.due_date = due_date
        self.completed = False


class FinanceRecord:
    def __init__(self, date, income, expense):
        self.date = date
        self.income = income
        self.expense = expense


class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone


class PersonalAssistant:
    def __init__(self):
        self.tasks = []
        self.finance_records = []
        self.contacts = []

    def add_task(self):
        title = input("Введите название задачи: ")
        description = input("Введите описание задачи: ")
        priority = input("Выберите приоритет (Высокий/Средний/Низкий): ")
        due_date = input("Введите срок выполнения (в формате ДД-ММ-ГГГГ): ")

        task = Task(title, description, priority, due_date)
        self.tasks.append(task)
        print("Задача успешно добавлена!")

    def generate_financial_report(self):
        start_date_str = input("Введите начальную дату (ДД-ММ-ГГГГ): ")
        end_date_str = input("Введите конечную дату (ДД-ММ-ГГГГ): ")

        start_date = datetime.strptime(start_date_str, "%d-%m-%Y")
        end_date = datetime.strptime(end_date_str, "%d-%m-%Y")

        total_income = sum(record.income for record in self.finance_records if start_date <= record.date <= end_date)
        total_expense = sum(record.expense for record in self.finance_records if start_date <= record.date <= end_date)

        balance = total_income - total_expense

        report_filename = f'report_{start_date_str}_{end_date_str}.csv'
        with open(report_filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Дата', 'Доход', 'Расход'])
            for record in self.finance_records:
                if start_date <= record.date <= end_date:
                    writer.writerow([record.date.strftime("%d-%m-%Y"), record.income, record.expense])

        print(f"Финансовый отчёт за период с {start_date_str} по {end_date_str}:")
        print(f"- Общий доход: {total_income} руб.")
        print(f"- Общие расходы: {total_expense} руб.")
        print(f"- Баланс: {balance} руб.")
        print(f"Подробная информация сохранена в файле {report_filename}")

    def import_contacts(self):
        filename = input("Введите имя CSV-файла для импорта: ")

        with open(filename, newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                contact = Contact(row[0], row[1])
                self.contacts.append(contact)

        print("Контакты успешно импортированы из CSV-файла.")

    def main_menu(self):
        while True:
            print("\nДобро пожаловать в Персональный помощник!")
            print("Выберите действие:")
            print("1. Управление заметками")
            print("2. Управление задачами")
            print("3. Управление контактами")
            print("4. Управление финансовыми записями")
            print("5. Калькулятор")
            print("6. Выход")

            choice = input()

            if choice == '1':
                pass
            elif choice == '2':
                self.task_menu()
            elif choice == '3':
                self.contact_menu()
            elif choice == '4':
                self.finance_menu()
            elif choice == '5':
                pass
            elif choice == '6':
                break

    def calculator(self, expression):
        return eval(expression)

    def task_menu(self):
        while True:
            print("\nУправление задачами:")
            print("1. Добавить новую задачу")
            print("2. Просмотреть задачи")
            print("3. Отметить задачу как выполненную")
            print("4. Редактировать задачу")
            print("5. Удалить задачу")
            print("6. Экспорт задач в CSV")
            print("7. Импорт задач из CSV")
            print("8. Назад")

            choice = input()

            if choice == '1':
                self.add_task()
            elif choice == '2':
                for task in self.tasks:
                    status = "Выполнена" if task.completed else "Не выполнена"
                    print(f"{task.title} - {status}, Приоритет: {task.priority}, Срок: {task.due_date}")
            elif choice == '8':
                break

    def contact_menu(self):
        while True:
            print("\nУправление контактами:")
            print("1. Добавить новый контакт")
            print("2. Поиск контакта")
            print("3. Редактировать контакт")
            print("4. Удалить контакт")
            print("5. Экспорт контактов в CSV")
            print("6. Импорт контактов из CSV")
            print("7. Назад")

            choice = input()

            if choice == '6':
                self.import_contacts()
            elif choice == '7':
                break

    def finance_menu(self):
        while True:
            print("\nУправление финансовыми записями:")
            print("1. Добавить новую запись")
            print("2. Просмотреть все записи")
            print("3. Генерация отчёта")
            print("4. Удалить запись")
            print("5. Экспорт финансовых записей в CSV")
            print("6. Импорт финансовых записей из CSV")
            print("7. Назад")

            choice = input()

            if choice == '3':
                self.generate_financial_report()
            elif choice == '7':
                break


assistant = PersonalAssistant()
assistant.main_menu()
