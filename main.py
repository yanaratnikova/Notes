import csv
from datetime import datetime
class Note:
    def __init__(self, id, title, body, created):
        self.id = id
        self.title = title
        self.body = body
        self.created = created
        self.updated = created
    def save_to_csv(self):
        with open('notes.csv', 'a', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow([self.id, self.title, self.body, self.created, self.updated])

    @staticmethod
    def load_from_csv():
        notes = []
        with open('notes.csv', 'r') as file:
            reader = csv.reader(file, delimiter=';')
            for row in reader:
                id, title, body, created,updated = row
                note = Note(id, title, body, created)
                note.updated = updated
                notes.append(note)
        return notes
    def update(self, title, body):
        self.title = title
        self.body = body
        self.updated = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    @staticmethod
    def delete_from_csv(note_id):
        notes = []
        with open('notes.csv', 'r') as file:
            reader = csv.reader(file, delimiter=';')
            for row in reader:
                notes.append(row)
        with open('notes.csv', 'w', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            for row in notes:
                if row[0] != note_id:
                    writer.writerow(row)
def main():
    while True:
        print("Меню")
        print("1. Сохранить заиетку")
        print("2. Прочитать заметку")
        print("3. Добавить заметку")
        print("4. Редактировать заметку")
        print("5. Удалить заметку")
        command = input("Выберите команду (1-5): ")
        if command == '1':
            notes = Note.load_from_csv()
            for note in notes:
                print(f"ID: {note.id}, Заголовок: {note.title}, Дата создания: {note.created}")
            note_id = input("Выберите ID заметки для сохранения: ")
            new_title = input("Введите новый заголовок: ")
            new_body = input("Введите новое содержимое: ")
            for note in notes:
                if note.id == note_id:
                    note.updated(new_title, new_body)
                    note.save_to_csv()
                    break
        elif command =='2':
            notes = Note.load_from_csv()
            for note in notes:
                print(f"ID: {note.id}, Заголовок: {note.title}, Дата создания: {note.created}")
            note_id = input("Выберите ID заметки для просмотра: ")
            for note in notes:
                if note.id == note_id:
                    print(f"Заголовок: {note.title}, Содержимое: {note.body}, Дата создания: {note.created}, Дата последнего изменения: {note.updated}")
                    break
        elif command == '3':
            new_id = input("Введите уникальный ID заметки: ")
            new_title = input("Введите заголовок: ")
            new_body = input("Введите содержимое: ")
            new_note = Note(new_id, new_title, new_body, datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            new_note.save_to_csv()
        elif command == '4':
            notes = Note.load_from_csv()
            for note in notes:
                print(f"ID: {note.id}, Заголовок: {note.title}, Дата создания: {note.created}")
            note_id = input("Выберите ID заметки для редактирования: ")
            for note in notes:
                if note.id == note_id:
                    new_title = input("Введите новый заголовок: ")
                    new_body = input("Введите новое содержание: ")
                    note.updated(new_title, new_body)
                    note.save_to_csv()
                    break
        elif command == '5':
            notes = Note.load_from_csv()
            for note in notes:
                print(f"ID: {note.id}, Заголовок: {note.title}, Дата создания: {note.created}")
            note_id = input("Выберите ID заметки для удаления: ")
            Note.delete_from_csv(note_id)
        else:
            print("Неверная команда!")
if __name__ == "__main__":
    main()
