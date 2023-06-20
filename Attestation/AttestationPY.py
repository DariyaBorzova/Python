import csv
import os.path
from datetime import datetime


def main():
    initFile()
    while True:
        print("Укажите номер действия\n")
        print("1 - Создать\n"
              "2 - Вывести список\n"
              "3 - Редактировать заметку\n"
              "4 - Удалить заметку\n"
              "5 - Вывести заметку\n"
              "6 - Вывести по дате\n"
              "q - Выход")
        action = input()
        if action == '1':
            createNote()
        elif action == '2':
            printList()
        elif action == '3':
            editNote()
        elif action == '4':
            deleteNote()
        elif action == '5':
            outputNote()
        elif action == '6':
            outputByDate()
        else:
            break


def initFile():
    if not os.path.exists('notes.csv'):
        f = open('notes.csv', 'w')
        f.close()


def createNote():
    print("Введите заголовок:")
    header = input()
    print("Введите заметку:")
    note = input()
    noteList = readDataFromFile()
    maxId = getMaxId(noteList)
    now = datetime.now().date()
    noteList.append({"id": str(maxId + 1), "title": header, "note": note, "date": now})
    writeDataToFile(noteList)


def readDataFromFile():
    f = open('notes.csv', 'r')
    reader = csv.DictReader(f, delimiter=';')
    noteList = list(reader)
    f.close()
    return noteList


def writeDataToFile(notelist):
    f = open('notes.csv', 'w')
    writer = csv.DictWriter(f, fieldnames=['id', 'title', 'note', 'date'], quoting=csv.QUOTE_NONNUMERIC, delimiter=';')
    writer.writeheader()
    writer.writerows(notelist)
    f.close()


def getMaxId(noteList):
    maxId = 0
    if noteList:
        lastNote = noteList[-1]
        maxId = int(lastNote.get('id'))

    return maxId

def printList():
    print("Список заметок:\n")
    noteList = readDataFromFile()
    for note in noteList:
        printNote(note)


def printNote(note):
    print('Id: ' + note.get('id'))
    print('Заголовок: ' + note.get('title'))
    print('Заметка: ' + note.get('note'))
    print('Дата изменения: ' + note.get('date'))


def editNote():
    print("Введите идентификатор заметки:")
    noteId = input()
    noteList = readDataFromFile()
    isNoteFound = False
    for note in noteList:
        if note.get('id') == noteId:
            isNoteFound = True
            printNote(note)
            print('Введите новый текст заметки:')
            newText = input()
            note['note'] = newText
            break
    if isNoteFound:
        writeDataToFile(noteList)
    else:
        print('Заметка не найдена')


def deleteNote():
    print("Введите идентификатор заметки:")
    noteId = input()
    noteList = readDataFromFile()
    note = getNoteById(noteList, noteId)
    if note:
        noteList.remove(note)
    else:
        print('Заметка не найдена')
    writeDataToFile(noteList)


def outputNote():
    print("Введите идентификатор заметки:")
    noteId = input()
    noteList = readDataFromFile()
    note = getNoteById(noteList, noteId)
    if note:
        printNote(note)
    else:
        print('Заметка не найдена')


def getNoteById(noteList, noteId):
    for note in noteList:
        if note['id'] == noteId:
            return note
    return None


def outputByDate():
    print('Введите дату(гггг-мм-дд):')
    date = input()
    noteList = readDataFromFile()
    for note in noteList:
        if note['date'] == date:
            printNote(note)


main()
